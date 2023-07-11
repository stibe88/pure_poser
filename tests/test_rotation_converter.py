import unittest

import poser


class TestRotationConverter(unittest.TestCase):
    def test_matrix_to_opk_deg(self) -> None:
        m = poser.RotationMatrix()
        m.matrix = (
            (-0.9447, 0.0256, -0.3270,),
            (-0.0967, -0.9743, 0.2032,),
            (-0.3134, 0.2236, 0.9229,),
        )
        opk = poser.RotationConverter.matrix_to_opk_deg(
            matrix=m,
        )
        self.assertIsInstance(opk, poser.RotationOPKDeg)
        self.assertIsInstance(opk.omega, float)
        self.assertIsInstance(opk.phi, float)
        self.assertIsInstance(opk.kappa, float)
        self.assertAlmostEqual(opk.omega, -12.4170, places=4)
        self.assertAlmostEqual(opk.phi, -19.0871, places=4)
        self.assertAlmostEqual(opk.kappa, -178.4477, places=4)

    def test_matrix_to_opk_deg_gimbal_lock(self) -> None:
        m = poser.RotationMatrix()
        m.matrix = (
            (0.0000, 0.0000, 1.0000,),
            (0.3420, 0.9397, 0.0000,),
            (-0.9397, 0.3420, 0.0000,),
        )
        opk = poser.RotationConverter.matrix_to_opk_deg(
            matrix=m,
        )
        self.assertIsInstance(opk, poser.RotationOPKDeg)
        self.assertIsInstance(opk.omega, float)
        self.assertIsInstance(opk.phi, float)
        self.assertIsInstance(opk.kappa, float)
        self.assertAlmostEqual(opk.omega, 0.0, places=4)
        self.assertAlmostEqual(opk.phi, 90.0, places=4)
        self.assertAlmostEqual(opk.kappa, 19.9988, places=4)

    def test_opk_deg_to_matrix(self) -> None:
        m = poser.RotationConverter.opk_deg_to_matrix(
            opk_deg=poser.RotationOPKDeg(
                omega=-12.4170,
                phi=-19.0871,
                kappa=-178.4477,
            )
        )
        self.assertIsInstance(m, poser.RotationMatrix)
        self.assertIsInstance(m.r11, float)
        self.assertIsInstance(m.r12, float)
        self.assertIsInstance(m.r13, float)
        self.assertIsInstance(m.r21, float)
        self.assertIsInstance(m.r22, float)
        self.assertIsInstance(m.r23, float)
        self.assertIsInstance(m.r31, float)
        self.assertIsInstance(m.r32, float)
        self.assertIsInstance(m.r33, float)
        self.assertAlmostEqual(m.r11, -0.9447, places=4)
        self.assertAlmostEqual(m.r12, 0.0256, places=4)
        self.assertAlmostEqual(m.r13, -0.3270, places=4)
        self.assertAlmostEqual(m.r21, -0.0967, places=4)
        self.assertAlmostEqual(m.r22, -0.9743, places=4)
        self.assertAlmostEqual(m.r23, 0.2032, places=4)
        self.assertAlmostEqual(m.r31, -0.3134, places=4)
        self.assertAlmostEqual(m.r32, 0.2236, places=4)
        self.assertAlmostEqual(m.r33, 0.9229, places=4)



if __name__ == '__main__':
    unittest.main()
