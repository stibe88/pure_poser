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


if __name__ == "__main__":
    unittest.main()
