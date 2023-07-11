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
        self.assertIsInstance(obj=opk, cls=poser.RotationOPKDeg)
        self.assertIsInstance(opk.omega, float)
        self.assertIsInstance(opk.phi, float)
        self.assertIsInstance(opk.kappa, float)
        self.assertAlmostEqual(opk.omega, -12.417, places=3)
        self.assertAlmostEqual(opk.phi, -19.001, places=3)
        self.assertAlmostEqual(opk.kappa, -178.448, places=3)



if __name__ == '__main__':
    unittest.main()
