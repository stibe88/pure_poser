import unittest

import poser


class TestRotationMatrix(unittest.TestCase):
    def test_init_empty(self) -> None:
        m = poser.RotationMatrix()
        self.assertEqual(m.r11, 1.0)
        self.assertIsInstance(m.r11, float)
        self.assertEqual(m.r12, 0.0)
        self.assertIsInstance(m.r12, float)
        self.assertEqual(m.r13, 0.0)
        self.assertIsInstance(m.r13, float)
        self.assertEqual(m.r21, 0.0)
        self.assertIsInstance(m.r21, float)
        self.assertEqual(m.r22, 1.0)
        self.assertIsInstance(m.r22, float)
        self.assertEqual(m.r23, 0.0)
        self.assertIsInstance(m.r23, float)
        self.assertEqual(m.r31, 0.0)
        self.assertIsInstance(m.r31, float)
        self.assertEqual(m.r32, 0.0)
        self.assertIsInstance(m.r32, float)
        self.assertEqual(m.r33, 1.0)
        self.assertIsInstance(m.r33, float)

    def test_post_init(self) -> None:
        m = poser.RotationMatrix(
            r11="1", r12="2", r13="3",
            r21="4", r22="5", r23="6",
            r31="7", r32="8", r33="9"
        )
        self.assertEqual(m.r11, 1.0)
        self.assertIsInstance(m.r11, float)
        self.assertEqual(m.r12, 2.0)
        self.assertIsInstance(m.r12, float)
        self.assertEqual(m.r13, 3.0)
        self.assertIsInstance(m.r13, float)
        self.assertEqual(m.r21, 4.0)
        self.assertIsInstance(m.r21, float)
        self.assertEqual(m.r22, 5.0)
        self.assertIsInstance(m.r22, float)
        self.assertEqual(m.r23, 6.0)
        self.assertIsInstance(m.r23, float)
        self.assertEqual(m.r31, 7.0)
        self.assertIsInstance(m.r31, float)
        self.assertEqual(m.r32, 8.0)
        self.assertIsInstance(m.r32, float)
        self.assertEqual(m.r33, 9.0)
        self.assertIsInstance(m.r33, float)

    def test_tuple_setter(self) -> None:
        m = poser.RotationMatrix()
        m.as_tuple = (
            (1.0, 2.0, 3.0,),
            (4.0, 5.0, 6.0,),
            (7.0, 8.0, 9.0,),
        )
        self.assertEqual(m.r11, 1.0)
        self.assertIsInstance(m.r11, float)
        self.assertEqual(m.r12, 2.0)
        self.assertIsInstance(m.r12, float)
        self.assertEqual(m.r13, 3.0)
        self.assertIsInstance(m.r13, float)
        self.assertEqual(m.r21, 4.0)
        self.assertIsInstance(m.r21, float)
        self.assertEqual(m.r22, 5.0)
        self.assertIsInstance(m.r22, float)
        self.assertEqual(m.r23, 6.0)
        self.assertIsInstance(m.r23, float)
        self.assertEqual(m.r31, 7.0)
        self.assertIsInstance(m.r31, float)
        self.assertEqual(m.r32, 8.0)
        self.assertIsInstance(m.r32, float)
        self.assertEqual(m.r33, 9.0)
        self.assertIsInstance(m.r33, float)

    def test_tuple_getter(self) -> None:
        m = poser.RotationMatrix()
        tpl = m.as_tuple
        self.assertIsInstance(tpl, tuple)
        self.assertTupleEqual(
            tpl, 
            ((1.0, 0.0, 0.0,), (0.0, 1.0, 0.0,), (0.0, 0.0, 1.0,),)
        )

    def test_list_setter(self) -> None:
        m = poser.RotationMatrix()
        m.as_list = [
            [1.0, 2.0, 3.0,],
            [4.0, 5.0, 6.0,],
            [7.0, 8.0, 9.0,],
        ]
        self.assertEqual(m.r11, 1.0)
        self.assertIsInstance(m.r11, float)
        self.assertEqual(m.r12, 2.0)
        self.assertIsInstance(m.r12, float)
        self.assertEqual(m.r13, 3.0)
        self.assertIsInstance(m.r13, float)
        self.assertEqual(m.r21, 4.0)
        self.assertIsInstance(m.r21, float)
        self.assertEqual(m.r22, 5.0)
        self.assertIsInstance(m.r22, float)
        self.assertEqual(m.r23, 6.0)
        self.assertIsInstance(m.r23, float)
        self.assertEqual(m.r31, 7.0)
        self.assertIsInstance(m.r31, float)
        self.assertEqual(m.r32, 8.0)
        self.assertIsInstance(m.r32, float)
        self.assertEqual(m.r33, 9.0)
        self.assertIsInstance(m.r33, float)

    def test_list_getter(self) -> None:
        m = poser.RotationMatrix()
        lst = m.as_list
        self.assertIsInstance(lst, list)
        self.assertListEqual(
            lst, 
            [[1.0, 0.0, 0.0,], [0.0, 1.0, 0.0,], [0.0, 0.0, 1.0,],]
        )

    def test_multiplication(self) -> None:
        m = poser.RotationMatrix(
            r11=1.0,
            r12=2.0,
            r13=3.0,
            r21=4.0,
            r22=5.0,
            r23=6.0,
            r31=7.0,
            r32=8.0,
            r33=9.0,
        )
        prod = m * m
        self.assertIsInstance(prod, poser.RotationMatrix)
        self.assertEqual(prod.r11, 30.0)
        self.assertIsInstance(prod.r11, float)
        self.assertEqual(prod.r12, 36.0)
        self.assertIsInstance(prod.r12, float)
        self.assertEqual(prod.r13, 42.0)
        self.assertIsInstance(prod.r13, float)
        self.assertEqual(prod.r21, 66.0)
        self.assertIsInstance(prod.r21, float)
        self.assertEqual(prod.r22, 81.0)
        self.assertIsInstance(prod.r22, float)
        self.assertEqual(prod.r23, 96.0)
        self.assertIsInstance(prod.r23, float)
        self.assertEqual(prod.r31, 102.0)
        self.assertIsInstance(prod.r31, float)
        self.assertEqual(prod.r32, 126.0)
        self.assertIsInstance(prod.r32, float)
        self.assertEqual(prod.r33, 150.0)
        self.assertIsInstance(prod.r33, float)

    def test_inversion(self) -> None:
        m = poser.RotationMatrix(
            r11=1.0,
            r12=2.0,
            r13=3.0,
            r21=4.0,
            r22=5.0,
            r23=6.0,
            r31=7.0,
            r32=8.0,
            r33=9.0,
        )
        inv = ~m
        self.assertIsInstance(inv, poser.RotationMatrix)
        self.assertEqual(inv.r11, 1.0)
        self.assertIsInstance(inv.r11, float)
        self.assertEqual(inv.r12, 4.0)
        self.assertIsInstance(inv.r12, float)
        self.assertEqual(inv.r13, 7.0)
        self.assertIsInstance(inv.r13, float)
        self.assertEqual(inv.r21, 2.0)
        self.assertIsInstance(inv.r21, float)
        self.assertEqual(inv.r22, 5.0)
        self.assertIsInstance(inv.r22, float)
        self.assertEqual(inv.r23, 8.0)
        self.assertIsInstance(inv.r23, float)
        self.assertEqual(inv.r31, 3.0)
        self.assertIsInstance(inv.r31, float)
        self.assertEqual(inv.r32, 6.0)
        self.assertIsInstance(inv.r32, float)
        self.assertEqual(inv.r33, 9.0)
        self.assertIsInstance(inv.r33, float)

    def test_transform_point(self) -> None:
        p = poser.Point(x=1.0, y=2.0, z=3.0)
        t = poser.Translation(x=1.0, y=2.0, z=3.0)
        r = poser.RotationMatrix(r11=-1, r22=-1, r33=-1)
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
        r = poser.RotationMatrix(r11=-1, r22=-1, r33=-1)
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
        r = poser.RotationMatrix(r11=-1, r22=-1, r33=-1)
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
        r = poser.RotationMatrix(r11=-1, r22=-1, r33=-1)
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


class TestRotationQuaternion(unittest.TestCase):
    def test_init(self) -> None:
        q = poser.RotationQuaternion()
        self.assertIsInstance(q, poser.RotationQuaternion)
        self.assertIsInstance(q.w, float)
        self.assertEqual(q.w, 1.0)
        self.assertIsInstance(q.x, float)
        self.assertEqual(q.x, 0.0)
        self.assertIsInstance(q.y, float)
        self.assertEqual(q.y, 0.0)
        self.assertIsInstance(q.z, float)
        self.assertEqual(q.z, 0.0)

    def test_post_init(self) -> None:
        q = poser.RotationQuaternion(
            w="1",
            x="0",
            y="0",
            z="0",
        )
        self.assertIsInstance(q, poser.RotationQuaternion)
        self.assertIsInstance(q.w, float)
        self.assertEqual(q.w, 1.0)
        self.assertIsInstance(q.x, float)
        self.assertEqual(q.x, 0.0)
        self.assertIsInstance(q.y, float)
        self.assertEqual(q.y, 0.0)
        self.assertIsInstance(q.z, float)
        self.assertEqual(q.z, 0.0)

    def test_abs(self) -> None:
        q = poser.RotationQuaternion(
            w=0.0,
            x=0.0,
            y=3.0,
            z=4.0
        )
        norm = abs(q)
        self.assertIsInstance(norm, float)
        self.assertEqual(norm, 5.0)

    def test_multiplication(self) -> None:
        q = poser.RotationQuaternion(
            w=0.9659,
            x=0.2588,
            y=0.0,
            z=0.0
        )
        prod = q * q
        self.assertIsInstance(prod, poser.RotationQuaternion)
        self.assertIsInstance(prod.w, float)
        self.assertAlmostEqual(prod.w, 0.8660, places=4)
        self.assertIsInstance(prod.w, float)
        self.assertAlmostEqual(prod.x, 0.5, places=4)
        self.assertIsInstance(prod.y, float)
        self.assertAlmostEqual(prod.y, 0.0, places=4)
        self.assertIsInstance(prod.z, float)
        self.assertAlmostEqual(prod.z, 0.0, places=4)

    def test_invert(self) -> None:
        rot = poser.RotationQuaternion(
            w=5.0,
            x=4.0,
            y=3.0,
            z=2.0,
        )
        r = ~rot * rot
        self.assertIsInstance(r, poser.RotationQuaternion)
        self.assertIsInstance(r.w, float)
        self.assertAlmostEqual(r.w, 1.0, places=4)
        self.assertIsInstance(r.x, float)
        self.assertAlmostEqual(r.x, 0.0, places=4)
        self.assertIsInstance(r.y, float)
        self.assertAlmostEqual(r.y, 0.0, places=4)
        self.assertIsInstance(r.z, float)
        self.assertAlmostEqual(r.z, 0.0, places=4)

    def test_interpolated_zero(self) -> None:
        a = poser.RotationQuaternion(
            w=0.7071,
            x=0.7071,
            y=0.0,
            z=0.0,
        )
        b = poser.RotationQuaternion() 
        r = a.interpolated(
            other=b,
            factor=0.0,
        )
        self.assertIsInstance(r, poser.RotationQuaternion)
        self.assertIsInstance(r.w, float)
        self.assertAlmostEqual(r.w, a.w, places=3)
        self.assertIsInstance(r.x, float)
        self.assertAlmostEqual(r.x, a.x, places=3)
        self.assertIsInstance(r.y, float)
        self.assertAlmostEqual(r.y, a.y, places=3)
        self.assertIsInstance(r.z, float)
        self.assertAlmostEqual(r.z, a.z, places=3)

    def test_interpolated_one(self) -> None:
        a = poser.RotationQuaternion(
            w=0.7071,
            x=0.7071,
            y=0.0,
            z=0.0,
        )
        b = poser.RotationQuaternion() 
        r = a.interpolated(
            other=b,
            factor=1.0,
        )
        self.assertIsInstance(r, poser.RotationQuaternion)
        self.assertIsInstance(r.w, float)
        self.assertAlmostEqual(r.w, b.w, places=3)
        self.assertIsInstance(r.x, float)
        self.assertAlmostEqual(r.x, b.x, places=3)
        self.assertIsInstance(r.y, float)
        self.assertAlmostEqual(r.y, b.y, places=3)
        self.assertIsInstance(r.z, float)
        self.assertAlmostEqual(r.z, b.z, places=3)

    def test_interpolated_half(self) -> None:
        a = poser.RotationQuaternion(
            w=0.7071,
            x=0.7071,
            y=0.0,
            z=0.0,
        )
        b = poser.RotationQuaternion() 
        r = a.interpolated(
            other=b,
            factor=0.5,
        )
        self.assertIsInstance(r, poser.RotationQuaternion)
        self.assertIsInstance(r.w, float)
        self.assertAlmostEqual(r.w, 0.9238, places=3)
        self.assertIsInstance(r.x, float)
        self.assertAlmostEqual(r.x, 0.3827, places=3)
        self.assertIsInstance(r.y, float)
        self.assertAlmostEqual(r.y, 0.0, places=3)
        self.assertIsInstance(r.z, float)
        self.assertAlmostEqual(r.z, 0.0, places=3)


class TestRotationOPKDeg(unittest.TestCase):
    def test_init(self) -> None:
        r = poser.RotationOPKDeg()
        self.assertIsInstance(r, poser.RotationOPKDeg)
        self.assertIsInstance(r.omega, float)
        self.assertEqual(r.omega, 0.0)
        self.assertIsInstance(r.phi, float)
        self.assertEqual(r.phi, 0.0)
        self.assertIsInstance(r.kappa, float)
        self.assertEqual(r.kappa, 0.0)

    def test_post_init(self) -> None:
        r = poser.RotationOPKDeg(
            omega=1,
            phi=2,
            kappa=3,
        )     
        self.assertIsInstance(r, poser.RotationOPKDeg)
        self.assertIsInstance(r.omega, float)
        self.assertEqual(r.omega, 1.0)
        self.assertIsInstance(r.phi, float)
        self.assertEqual(r.phi, 2.0)
        self.assertIsInstance(r.kappa, float)
        self.assertEqual(r.kappa, 3.0)


if __name__ == "__main__":
    unittest.main()
