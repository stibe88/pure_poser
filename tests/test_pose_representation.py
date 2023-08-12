import unittest

import poser
import poser.rotation.representations


Matrix = poser.rotation.representations.Matrix
Quaternion = poser.rotation.representations.Quaternion
OPKDeg = poser.rotation.representations.OPKDeg


class TestPoseInit(unittest.TestCase):
    def test_init_empty(self) -> None:
        pose = poser.Pose()
        self.assertIsInstance(pose, poser.Pose)
        self.assertIsInstance(pose.rotation, poser.Rotation)
        self.assertIsInstance(pose.translation, poser.Translation)


class TestPoseMagics(unittest.TestCase):
    def test_invert(self) -> None:
        pose = poser.Pose(
            translation=poser.Translation(x=1.0),
            rotation=poser.Rotation(
                rotation=OPKDeg(omega=10.0)
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
                rotation=OPKDeg(
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
        pose = poser.Pose()
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
                rotation=Quaternion(),
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

    def test_as_list_getter(self) -> None:
        pose = poser.Pose()
        matrix = pose.as_list
        self.assertIsInstance(matrix, list)
        self.assertListEqual(
            matrix,
            [
                [1.0, 0.0, 0.0, 0.0], 
                [0.0, 1.0, 0.0, 0.0], 
                [0.0, 0.0, 1.0, 0.0], 
                [0.0, 0.0, 0.0, 1.0],
            ]
        )
        
    def test_as_list_setter(self) -> None:
        pose = poser.Pose()
        pose.as_list = [
            [1.0, 0.0, 0.0, 1.0], 
            [0.0, 0.0, -1.0, 2.0], 
            [0.0, 1.0, 0.0, 3.0], 
            [0.0, 0.0, 0.0, 1.0],
        ]
        self.assertIsInstance(pose, poser.Pose)
        self.assertAlmostEqual(pose.translation.x, 1.0, places=4)
        self.assertAlmostEqual(pose.translation.y, 2.0, places=4)
        self.assertAlmostEqual(pose.translation.z, 3.0, places=4)
        self.assertAlmostEqual(pose.rotation.opk_deg.omega, 90.0, places=4)
        self.assertAlmostEqual(pose.rotation.opk_deg.phi, 0.0, places=4)
        self.assertAlmostEqual(pose.rotation.opk_deg.kappa, 0.0, places=4)


class TestPoseMethods(unittest.TestCase):
    def test_interpolated(self) -> None:
        p1 = poser.Pose(
            translation=poser.Translation(x=1.0),
        )
        p2 = poser.Pose(
            translation=poser.Translation(x=2.0),
            rotation=poser.Rotation(
                rotation=OPKDeg(omega=90.0)
            )
        )
        p_i = p1.interpolated(other=p2, factor=0.5)
        self.assertIsInstance(p_i, poser.Pose)
        self.assertAlmostEqual(p_i.translation.x, 1.5, places=4)
        self.assertAlmostEqual(p_i.rotation.opk_deg.omega, 45.0, places=4)

    def test_transform_point(self) -> None:
        point = poser.Point(x=0.0, y=1.414, z=1.414)
        pose = poser.Pose(
            translation=poser.Translation(z=1.0),
            rotation=poser.Rotation(
                rotation=OPKDeg(omega=45.0)
            )
        )
        pose.transform_point(point=point)
        self.assertIsInstance(point, poser.Point)
        self.assertAlmostEqual(point.z, 3.0, places=2)

    def test_transform_points(self) -> None:
        points = [poser.Point(x=0.0, y=1.414, z=1.414)]
        pose = poser.Pose(
            translation=poser.Translation(z=1.0),
            rotation=poser.Rotation(
                rotation=OPKDeg(omega=45.0)
            )
        )
        pose.transform_points(points=points)
        self.assertIsInstance(points[0], poser.Point)
        self.assertAlmostEqual(points[0].z, 3.0, places=2)

    def test_transformed_point(self) -> None:
        point = poser.Point(x=0.0, y=1.414, z=1.414)
        pose = poser.Pose(
            translation=poser.Translation(z=1.0),
            rotation=poser.Rotation(
                rotation=OPKDeg(omega=45.0)
            )
        )
        new_point = pose.transformed_point(point=point)
        self.assertIsInstance(new_point, poser.Point)
        self.assertAlmostEqual(new_point.z, 3.0, places=2)

    def test_transformed_points(self) -> None:
        points = [poser.Point(x=0.0, y=1.414, z=1.414)]
        pose = poser.Pose(
            translation=poser.Translation(z=1.0),
            rotation=poser.Rotation(
                rotation=OPKDeg(omega=45.0)
            )
        )
        new_points = pose.transformed_points(points=points)
        self.assertIsInstance(new_points[0], poser.Point)
        self.assertAlmostEqual(new_points[0].z, 3.0, places=2)             


if __name__ == "__main__":
    unittest.main()
