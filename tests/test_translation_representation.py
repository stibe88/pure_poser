import unittest

import poser


class TestTranslation(unittest.TestCase):
    def test_init_empty(self) -> None:
        t = poser.Translation()
        self.assertIsInstance(t, poser.Translation)
        self.assertIsInstance(t.x, float)
        self.assertIsInstance(t.y, float)
        self.assertIsInstance(t.z, float)
        self.assertEqual(t.x, 0.0)
        self.assertEqual(t.y, 0.0)
        self.assertEqual(t.z, 0.0)

    def test_invert(self) -> None:
        t = poser.Translation(
            x=1,
            y=2,
            z=3,
        )
        inv = ~t
        self.assertIsInstance(inv, poser.Translation)
        self.assertIsInstance(inv.x, float)
        self.assertIsInstance(inv.y, float)
        self.assertIsInstance(inv.z, float)
        self.assertEqual(inv.x, -1.0)
        self.assertEqual(inv.y, -2.0)
        self.assertEqual(inv.z, -3.0)

    def test_abs(self) -> None:
        t = poser.Translation(
            x=3.0,
            y=4.0,
            z=0.0,
        )
        length = abs(t)
        self.assertIsInstance(length, float)
        self.assertAlmostEqual(length, 5.0, places=3)

    def test_add(self) -> None:
        t1 = poser.Translation(
            x=1,
            y=2,
            z=3,
        )
        t2 = poser.Translation(
            x=-2,
            y=2,
            z=2,
        )
        res = t1 + t2
        self.assertIsInstance(res, poser.Translation)
        self.assertIsInstance(res.x, float)
        self.assertIsInstance(res.y, float)
        self.assertIsInstance(res.z, float)
        self.assertEqual(res.x, -1.0)
        self.assertEqual(res.y, 4.0)
        self.assertEqual(res.z, 5.0)

    def test_interpolated(self) -> None:
        t1 = poser.Translation(
            x=1,
            y=2,
            z=3,
        )
        t2 = poser.Translation(
            x=-2,
            y=2,
            z=2,
        )
        res = t1.interpolated(
            other=t2,
            factor=0.0
        )
        self.assertIsInstance(res, poser.Translation)
        self.assertIsInstance(res.x, float)
        self.assertIsInstance(res.y, float)
        self.assertIsInstance(res.z, float)
        self.assertEqual(res.x, 1.0)
        self.assertEqual(res.y, 2.0)
        self.assertEqual(res.z, 3.0)
        res = t1.interpolated(
            other=t2,
            factor=1.0
        )
        self.assertIsInstance(res, poser.Translation)
        self.assertIsInstance(res.x, float)
        self.assertIsInstance(res.y, float)
        self.assertIsInstance(res.z, float)
        self.assertEqual(res.x, -2.0)
        self.assertEqual(res.y, 2.0)
        self.assertEqual(res.z, 2.0)
        res = t1.interpolated(
            other=t2,
            factor=0.5
        )
        self.assertIsInstance(res, poser.Translation)
        self.assertIsInstance(res.x, float)
        self.assertIsInstance(res.y, float)
        self.assertIsInstance(res.z, float)
        self.assertEqual(res.x, -0.5)
        self.assertEqual(res.y, 2.0)
        self.assertEqual(res.z, 2.5)

    def test_transform_point(self) -> None:
        res = poser.Point(x=1.0, y=2.0, z=3.0)
        t = poser.Translation(x=2.0, y=4.0, z=6.0)
        t.transform_point(point=res)
        self.assertIsInstance(res, poser.Point)
        self.assertIsInstance(res.x, float)
        self.assertIsInstance(res.y, float)
        self.assertIsInstance(res.z, float)
        self.assertEqual(res.x, 3.0)
        self.assertEqual(res.y, 6.0)
        self.assertEqual(res.z, 9.0)
        t.transform_point(point=t)
        self.assertEqual(t.x, 4.0)
        self.assertEqual(t.y, 8.0)
        self.assertEqual(t.z, 12.0)

    def test_transform_point_wrong_type(self) -> None:
        res = poser.RotationMatrix()
        t = poser.Translation(x=2.0, y=4.0, z=6.0)
        with self.assertRaises(TypeError):
            t.transform_point(point=res)

    def test_transform_points(self) -> None:
        res = [poser.Point(x=1.0, y=2.0, z=3.0)]
        t = poser.Translation(x=2.0, y=4.0, z=6.0)
        t.transform_points(points=res)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], poser.Point)
        self.assertIsInstance(res[0].x, float)
        self.assertIsInstance(res[0].y, float)
        self.assertIsInstance(res[0].z, float)
        self.assertEqual(res[0].x, 3.0)
        self.assertEqual(res[0].y, 6.0)
        self.assertEqual(res[0].z, 9.0)
        res = (poser.Point(x=1.0, y=2.0, z=3.0),)
        t.transform_points(points=res)
        self.assertIsInstance(res, tuple)
        self.assertIsInstance(res[0], poser.Point)
        self.assertIsInstance(res[0].x, float)
        self.assertIsInstance(res[0].y, float)
        self.assertIsInstance(res[0].z, float)
        self.assertEqual(res[0].x, 3.0)
        self.assertEqual(res[0].y, 6.0)
        self.assertEqual(res[0].z, 9.0)

    def test_transformed_point(self) -> None:
        p = poser.Point(x=1.0, y=2.0, z=3.0)
        t = poser.Translation(x=2.0, y=4.0, z=6.0)
        res = t.transformed_point(point=p)
        self.assertIsInstance(res, poser.Point)
        self.assertIsInstance(res.x, float)
        self.assertIsInstance(res.y, float)
        self.assertIsInstance(res.z, float)
        self.assertEqual(res.x, 3.0)
        self.assertEqual(res.y, 6.0)
        self.assertEqual(res.z, 9.0)
        res = t.transformed_point(point=t)
        self.assertEqual(res.x, 4.0)
        self.assertEqual(res.y, 8.0)
        self.assertEqual(res.z, 12.0)

    def test_transformed_point_wrong_type(self) -> None:
        res = poser.RotationMatrix()
        t = poser.Translation(x=2.0, y=4.0, z=6.0)
        with self.assertRaises(TypeError):
            t.transformed_point(point=res)

    def test_transformed_points(self) -> None:
        pts = [poser.Point(x=1.0, y=2.0, z=3.0)]
        t = poser.Translation(x=2.0, y=4.0, z=6.0)
        res = t.transformed_points(points=pts)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], poser.Point)
        self.assertIsInstance(res[0].x, float)
        self.assertIsInstance(res[0].y, float)
        self.assertIsInstance(res[0].z, float)
        self.assertEqual(res[0].x, 3.0)
        self.assertEqual(res[0].y, 6.0)
        self.assertEqual(res[0].z, 9.0)
        pts = (poser.Point(x=1.0, y=2.0, z=3.0),)
        res = t.transformed_points(points=pts)
        self.assertIsInstance(res, tuple)
        self.assertIsInstance(res[0], poser.Point)
        self.assertIsInstance(res[0].x, float)
        self.assertIsInstance(res[0].y, float)
        self.assertIsInstance(res[0].z, float)
        self.assertEqual(res[0].x, 3.0)
        self.assertEqual(res[0].y, 6.0)
        self.assertEqual(res[0].z, 9.0)


if __name__ == "__main__":
    unittest.main()
