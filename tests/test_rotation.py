import unittest

import poser
import poser.rotation.representations


Matrix = poser.rotation.representations.Matrix
Quaternion = poser.rotation.representations.Quaternion
OPKDeg = poser.rotation.representations.OPKDeg


class TestRotationInitialization(unittest.TestCase):
    def test_init_empty(self) -> None:
        rot = poser.Rotation()
        self.assertIsInstance(rot, poser.Rotation)
        self.assertIsInstance(rot.matrix, Matrix)
        self.assertIsInstance(rot.quaternion, Quaternion)
        self.assertIsInstance(rot.opk_deg, OPKDeg)

    def test_init_opk_deg(self) -> None:
        opk_deg = OPKDeg(
            omega=90, 
            phi=0, 
            kappa=0,
        )
        rot = poser.Rotation(
            rotation=opk_deg,
        )
        self.assertIsInstance(rot, poser.Rotation)
        self.assertIsInstance(rot.matrix, Matrix)
        self.assertAlmostEqual(rot.matrix.r23, -1.0, places=3)
        self.assertAlmostEqual(rot.matrix.r33, 0.0, places=3)
        self.assertIsInstance(rot.quaternion, Quaternion)
        self.assertAlmostEqual(rot.quaternion.w, 0.7071, places=4)
        self.assertAlmostEqual(rot.quaternion.x, 0.7071, places=4)
        self.assertIsInstance(rot.opk_deg, OPKDeg)

    def test_init_matrix(self) -> None:
        matrix = Matrix(
            r22=0.0,
            r23=-1.0,
            r32=1.0,
            r33=0.0,
        )
        rot = poser.Rotation(
            rotation=matrix,
        )
        self.assertIsInstance(rot, poser.Rotation)
        self.assertIsInstance(rot.matrix, Matrix)
        self.assertIsInstance(rot.quaternion, Quaternion)
        self.assertAlmostEqual(rot.quaternion.w, 0.7071, places=4)
        self.assertAlmostEqual(rot.quaternion.x, 0.7071, places=4)
        self.assertIsInstance(rot.opk_deg, OPKDeg)
        self.assertAlmostEqual(rot.opk_deg.omega, 90.0, places=3)

    def test_init_quaternion(self) -> None:
        quaternion = Quaternion(
            w=0.7071,
            x=0.7071,
        )
        rot = poser.Rotation(
            rotation=quaternion
        )
        self.assertIsInstance(rot, poser.Rotation)
        self.assertIsInstance(rot.matrix, Matrix)
        self.assertAlmostEqual(rot.matrix.r23, -1.0, places=3)
        self.assertAlmostEqual(rot.matrix.r33, 0.0, places=3)
        self.assertIsInstance(rot.quaternion, Quaternion)
        self.assertIsInstance(rot.opk_deg, OPKDeg)
        self.assertAlmostEqual(rot.opk_deg.omega, 90.0, places=3)

    def test_init_wrong_type(self) -> None:
        with self.assertRaises(TypeError):
            poser.Rotation((1.0, 2.0, 3.0))


class TestRotationMagic(unittest.TestCase):
    def test_invert(self) -> None:
        rot = poser.Rotation(
            rotation=OPKDeg(omega=30)
        )
        res = ~rot
        self.assertIsInstance(res, poser.Rotation)
        self.assertAlmostEqual(res.opk_deg.omega, -30.0, places=4)

    def test_multiply(self) -> None:
        rot_1 = poser.Rotation(
            rotation=OPKDeg(omega=40.0)
        )
        rot_2 = poser.Rotation(
            rotation=OPKDeg(omega=-30.0)
        )
        res = rot_1 * rot_2
        self.assertIsInstance(res, poser.Rotation)
        self.assertAlmostEqual(res.opk_deg.omega, 10.0, places=4)


class TestRotationProperties(unittest.TestCase):
    def test_get_as_tuple(self) -> None:
        rot = poser.Rotation()
        self.assertIsInstance(rot.as_tuple, tuple)
        self.assertTupleEqual(
            rot.as_tuple, 
            (
                (1.0, 0.0, 0.0,),
                (0.0, 1.0, 0.0,),
                (0.0, 0.0, 1.0,),
            )
        )

    def test_set_as_tuple(self) -> None:
        rot = poser.Rotation()
        rot.as_tuple = (
            (1.0, 0.0, 0.0,),
            (0.0, 0.0, -1.0,),
            (0.0, 1.0, 0.0,),
        )
        self.assertIsInstance(rot, poser.Rotation)
        self.assertIsInstance(rot.matrix, Matrix)
        self.assertIsInstance(rot.quaternion, Quaternion)
        self.assertAlmostEqual(rot.quaternion.w, 0.7071, places=4)
        self.assertAlmostEqual(rot.quaternion.x, 0.7071, places=4)
        self.assertIsInstance(rot.opk_deg, OPKDeg)
        self.assertAlmostEqual(rot.opk_deg.omega, 90.0, places=3)

    def test_get_as_list(self) -> None:
        rot = poser.Rotation()
        self.assertIsInstance(rot.as_list, list)
        self.assertListEqual(
            rot.as_list, 
            [
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0],
            ]
        )

    def test_set_as_list(self) -> None:
        rot = poser.Rotation()
        rot.as_list = [
            [1.0, 0.0, 0.0],
            [0.0, 0.0, -1.0],
            [0.0, 1.0, 0.0],
        ]
        self.assertIsInstance(rot, poser.Rotation)
        self.assertIsInstance(rot.matrix, Matrix)
        self.assertIsInstance(rot.quaternion, Quaternion)
        self.assertAlmostEqual(rot.quaternion.w, 0.7071, places=4)
        self.assertAlmostEqual(rot.quaternion.x, 0.7071, places=4)
        self.assertIsInstance(rot.opk_deg, OPKDeg)
        self.assertAlmostEqual(rot.opk_deg.omega, 90.0, places=3)


class TestRotationTransformations(unittest.TestCase):
    def test_transform_point(self) -> None:
        p = poser.Point(x=1.0, y=2.0, z=3.0)
        t = poser.Translation(x=1.0, y=2.0, z=3.0)
        r = poser.Rotation(
            rotation=Matrix(r11=-1, r22=-1, r33=-1)
        )
        r.transform_point(point=p)
        self.assertIsInstance(p, poser.Point)
        self.assertIsInstance(p.x, float)
        self.assertIsInstance(p.y, float)
        self.assertIsInstance(p.z, float)
        self.assertEqual(p.x, -1.0)
        self.assertEqual(p.y, -2.0)
        self.assertEqual(p.z, -3.0)
        r.transform_point(point=t)
        self.assertEqual(t.x, -1.0)
        self.assertEqual(t.y, -2.0)
        self.assertEqual(t.z, -3.0)

    def test_transform_points(self) -> None:
        p = [poser.Point(x=1.0, y=2.0, z=3.0)]
        t = (poser.Translation(x=1.0, y=2.0, z=3.0),)
        r = poser.Rotation(
            rotation=Matrix(r11=-1, r22=-1, r33=-1)
        )
        r.transform_points(points=p)
        self.assertIsInstance(p, list)
        self.assertIsInstance(p[0], poser.Point)
        self.assertIsInstance(p[0].x, float)
        self.assertIsInstance(p[0].y, float)
        self.assertIsInstance(p[0].z, float)
        self.assertEqual(p[0].x, -1.0)
        self.assertEqual(p[0].y, -2.0)
        self.assertEqual(p[0].z, -3.0)
        r.transform_points(points=t)
        self.assertIsInstance(t, tuple)
        self.assertIsInstance(t[0], poser.Translation)
        self.assertIsInstance(t[0].x, float)
        self.assertIsInstance(t[0].y, float)
        self.assertIsInstance(t[0].z, float)
        self.assertEqual(t[0].x, -1.0)
        self.assertEqual(t[0].y, -2.0)
        self.assertEqual(t[0].z, -3.0)

    def test_transformed_point(self) -> None:
        p = poser.Point(x=1.0, y=2.0, z=3.0)
        t = poser.Translation(x=1.0, y=2.0, z=3.0)
        r = poser.Rotation(
            rotation=Matrix(r11=-1, r22=-1, r33=-1)
        )
        res = r.transformed_point(point=p)
        self.assertIsInstance(res, poser.Point)
        self.assertIsInstance(res.x, float)
        self.assertIsInstance(res.y, float)
        self.assertIsInstance(res.z, float)
        self.assertEqual(res.x, -1.0)
        self.assertEqual(res.y, -2.0)
        self.assertEqual(res.z, -3.0)
        res = r.transformed_point(point=t)
        self.assertIsInstance(res, poser.Translation)
        self.assertEqual(res.x, -1.0)
        self.assertEqual(res.y, -2.0)
        self.assertEqual(res.z, -3.0)

    def test_transformed_points(self) -> None:
        p = [poser.Point(x=1.0, y=2.0, z=3.0)]
        t = (poser.Translation(x=1.0, y=2.0, z=3.0),)
        r = poser.Rotation(
            rotation=Matrix(r11=-1, r22=-1, r33=-1)
        )
        res = r.transformed_points(points=p)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], poser.Point)
        self.assertIsInstance(res[0].x, float)
        self.assertIsInstance(res[0].y, float)
        self.assertIsInstance(res[0].z, float)
        self.assertEqual(res[0].x, -1.0)
        self.assertEqual(res[0].y, -2.0)
        self.assertEqual(res[0].z, -3.0)
        res = r.transformed_points(points=t)
        self.assertIsInstance(res, tuple)
        self.assertIsInstance(res[0], poser.Translation)
        self.assertIsInstance(res[0].x, float)
        self.assertIsInstance(res[0].y, float)
        self.assertIsInstance(res[0].z, float)
        self.assertEqual(res[0].x, -1.0)
        self.assertEqual(res[0].y, -2.0)
        self.assertEqual(res[0].z, -3.0)


if __name__ == "__main__":
    unittest.main()
    