import unittest

import poser


class TestInitializeRotation(unittest.TestCase):
    def test_init_empty(self) -> None:
        r = poser.rotation.Rotation()
        self.assertEqual(r.w, 1.0)
        self.assertIsInstance(r.w, float)
        self.assertEqual(r.x, 0.0)
        self.assertIsInstance(r.x, float)
        self.assertEqual(r.y, 0.0)
        self.assertIsInstance(r.y, float)
        self.assertEqual(r.z, 0.0)
        self.assertIsInstance(r.z, float)

    def test_init_not_normalized(self) -> None:
        r = poser.rotation.Rotation(
            w=5.0,
            x=4.0,
            y=3.0,
            z=2.0,
        )
        self.assertAlmostEqual(r.w, 0.6804, places=4)
        self.assertAlmostEqual(r.x, 0.5443, places=4)
        self.assertAlmostEqual(r.y, 0.4082, places=4)
        self.assertAlmostEqual(r.z, 0.2722, places=4)

class TestRotationConcatenation(unittest.TestCase):
    def setUp(self) -> None:
        self.rx30 = poser.rotation.Rotation(
            w=0.96593,
            x=0.25882,
            y=0.0,
            z=0.0,
        )
        self.ry60 = poser.rotation.Rotation(
            w=0.86603,
            x=0.0,
            y=0.5,
            z=0.0,
        )
        self.rzneg45 = poser.rotation.Rotation(
            w=0.92388,
            x=0.0,
            y=0.0,
            z=-0.38268,
        )

    def test_x_rotation(self) -> None:
        r = (
            self.rx30 
            * self.rx30 
            * self.rx30
            * self.rx30
            * self.rx30
            * self.rx30
            * self.rx30
            * self.rx30
            * self.rx30
            * self.rx30
            * self.rx30
            * self.rx30
        )
        self.assertAlmostEqual(r.w, -1.0, places=4)
        self.assertAlmostEqual(r.x, 0.0, places=4)
        self.assertAlmostEqual(r.y, 0.0, places=4)
        self.assertAlmostEqual(r.z, 0.0, places=4)

    def test_y_rotation(self) -> None:
        r = (
            self.ry60
            * self.ry60
            * self.ry60
            * self.ry60
            * self.ry60
            * self.ry60
        )
        self.assertAlmostEqual(r.w, -1.0, places=4)
        self.assertAlmostEqual(r.x, 0.0, places=4)
        self.assertAlmostEqual(r.y, 0.0, places=4)
        self.assertAlmostEqual(r.z, 0.0, places=4)

    def test_z_rotation(self) -> None:
        r = (
            self.rzneg45
            * self.rzneg45
            * self.rzneg45
            * self.rzneg45
            * self.rzneg45
            * self.rzneg45
            * self.rzneg45
            * self.rzneg45
        )
        self.assertAlmostEqual(r.w, -1.0, places=4)
        self.assertAlmostEqual(r.x, 0.0, places=4)
        self.assertAlmostEqual(r.y, 0.0, places=4)
        self.assertAlmostEqual(r.z, 0.0, places=4)


class TestRotationAbs(unittest.TestCase):
    def test_rotation_abs(self) -> None:
        r = poser.rotation.Rotation(
            w=5.0,
            x=4.0,
            y=3.0,
            z=2.0,
        )
        self.assertEqual(abs(r), 1.0)


class TestInvertRotation(unittest.TestCase):
    def test_invert(self) -> None:
        rot = poser.rotation.Rotation(
            w=5.0,
            x=4.0,
            y=3.0,
            z=2.0,
        )
        r = ~rot * rot
        self.assertAlmostEqual(r.w, 1.0, places=4)
        self.assertAlmostEqual(r.x, 0.0, places=4)
        self.assertAlmostEqual(r.y, 0.0, places=4)
        self.assertAlmostEqual(r.z, 0.0, places=4)


class TestGetMatrix(unittest.TestCase):
    def test_get_rotation_matrix(self) -> None:
        quaternion = {
            "w": 0.96593,
            "x": 0.25882,
            "y": 0.0,
            "z": 0.0
        }
        matrix = (
            (1.0, 0.0, 0.0,),
            (0.0, 0.8660, -0.5000,),
            (0.0, 0.5000, 0.8660),
        )
        r = poser.rotation.Rotation(**quaternion)
        for res_row, should_row in zip(r.matrix, matrix):
            for res_col, should_col in zip(res_row, should_row):
                self.assertAlmostEqual(
                    res_col, 
                    should_col, 
                    places=4,
                )

class TestSetMatrix(unittest.TestCase):
    def test_set_rotation_matrix(self) -> None:
        matrices = (
            (
                (0.7441, -0.3268, 0.5826,),
                (0.5826, 0.7441, -0.3268,),
                (-0.3268, 0.5827, 0.7441,)
            ),
            (
                (-0.9296, 0.2928, 0.2240,),
                (-0.0998, -0.7848, 0.6116,),
                (0.3549, 0.5461, 0.7588,),
            ),
            (
                (-0.9447, 0.0256, -0.3270,),
                (-0.0967, -0.9743, 0.2032,),
                (-0.3134, 0.2236, 0.9229,),
            ),
            # (
            #     (),
            #     (),
            #     (),
            # ),
        )
        for matrix in matrices:
            r = poser.rotation.Rotation()
            r.matrix = matrix
            for res_row, should_row in zip(r.matrix, matrix):
                for res_col, should_col in zip(res_row, should_row):
                    self.assertAlmostEqual(
                        res_col, 
                        should_col, 
                        places=3,
                    )



if __name__ == '__main__':
    unittest.main()
