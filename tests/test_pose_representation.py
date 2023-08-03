import unittest

import poser


class TestPoseInit(unittest.TestCase):
    def test_init_empty(self) -> None:
        pose = poser.Pose(
            translation=poser.Translation(),
            rotation=poser.Rotation(),
        )
        self.assertIsInstance(pose, poser.Pose)
        self.assertIsInstance(pose.rotation, poser.Rotation)
        self.assertIsInstance(pose.translation, poser.Translation)


class TestPoseMagics(unittest.TestCase):
    def test_invert(self) -> None:
        pose = poser.Pose(
            translation=poser.Translation(x=1.0),
            rotation=poser.Rotation(
                rotation=poser.RotationOPKDeg(omega=10.0)
            )
        )
        res = ~pose
        self.assertIsInstance(res, poser.Pose)
        self.assertAlmostEqual(res.translation.x, -1.0, places=4)
        self.assertAlmostEqual(res.rotation.opk_deg.omega, -10.0, places=4)

    def test_multiply(self) -> None:
        pose = poser.Pose(
            translation=poser.Translation(x=1.0, y=2.0, z=3.0),
            rotation=poser.Rotation(
                rotation=poser.RotationOPKDeg(
                    omega=10.0, phi=20.0, kappa=30.0,
                )
            ),
        )
        res = ~pose * pose
        self.assertIsInstance(res, poser.Pose)
        self.assertAlmostEqual(res.translation.x, 0.0, places=4)
        self.assertAlmostEqual(res.translation.y, 0.0, places=4)
        self.assertAlmostEqual(res.translation.z, 0.0, places=4)
        self.assertAlmostEqual(res.rotation.opk_deg.omega, 0.0, places=4)
        self.assertAlmostEqual(res.rotation.opk_deg.phi, 0.0, places=4)
        self.assertAlmostEqual(res.rotation.opk_deg.kappa, 0.0, places=4)

class TestPoseProperties(unittest.TestCase):
    def test_as_tuple_getter(self) -> None:
        pose = poser.Pose(
            translation=poser.Translation(), 
            rotation=poser.Rotation(
                rotation=poser.RotationQuaternion(),
            )
        )
        matrix = pose.as_tuple
        self.assertIsInstance(matrix, tuple)
        self.assertTupleEqual(
            matrix,
            (
                (1.0, 0.0, 0.0, 0.0), 
                (0.0, 1.0, 0.0, 0.0), 
                (0.0, 0.0, 1.0, 0.0), 
                (0.0, 0.0, 0.0, 1.0),
            )
        )
        
    def test_as_tuple_setter(self) -> None:
        pose = poser.Pose(
            translation=poser.Translation(), 
            rotation=poser.Rotation(
                rotation=poser.RotationQuaternion(),
            )
        )
        pose.as_tuple = (
            (1.0, 0.0, 0.0, 1.0), 
            (0.0, 0.0, -1.0, 2.0), 
            (0.0, 1.0, 0.0, 3.0), 
            (0.0, 0.0, 0.0, 1.0)
        )
        self.assertIsInstance(pose, poser.Pose)
        self.assertAlmostEqual(pose.translation.x, 1.0, places=4)
        self.assertAlmostEqual(pose.translation.y, 2.0, places=4)
        self.assertAlmostEqual(pose.translation.z, 3.0, places=4)
        self.assertAlmostEqual(pose.rotation.opk_deg.omega, 90.0, places=4)
        self.assertAlmostEqual(pose.rotation.opk_deg.phi, 0.0, places=4)
        self.assertAlmostEqual(pose.rotation.opk_deg.kappa, 0.0, places=4)


if __name__ == "__main__":
    unittest.main()
