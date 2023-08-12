import unittest

import poser


Point = poser.point.Point

class TestPoint(unittest.TestCase):

    def test_init_empty(self) -> None:
        res = Point()
        self.assertIsInstance(res, Point)
        self.assertIsInstance(res.x, float)
        self.assertIsInstance(res.y, float)
        self.assertIsInstance(res.z, float)
        self.assertAlmostEqual(res.x, 0.0, places=4)
        self.assertAlmostEqual(res.y, 0.0, places=4)
        self.assertAlmostEqual(res.z, 0.0, places=4)

    def test_init_float(self) -> None:
        res = Point(x=1.0, y=2.0, z=3.0)
        self.assertIsInstance(res.x, float)
        self.assertIsInstance(res.y, float)
        self.assertIsInstance(res.z, float)
        self.assertAlmostEqual(res.x, 1.0, places=4)
        self.assertAlmostEqual(res.y, 2.0, places=4)
        self.assertAlmostEqual(res.z, 3.0, places=4)

    def test_init_integer(self) -> None:
        res = Point(x=1, y=2, z=3)
        self.assertIsInstance(res.x, float)
        self.assertIsInstance(res.y, float)
        self.assertIsInstance(res.z, float)
        self.assertAlmostEqual(res.x, 1.0, places=4)
        self.assertAlmostEqual(res.y, 2.0, places=4)
        self.assertAlmostEqual(res.z, 3.0, places=4)

    def test_init_string(self) -> None:
        res = Point(x="1", y="2", z="3")
        self.assertIsInstance(res.x, float)
        self.assertIsInstance(res.y, float)
        self.assertIsInstance(res.z, float)
        self.assertAlmostEqual(res.x, 1.0, places=4)
        self.assertAlmostEqual(res.y, 2.0, places=4)
        self.assertAlmostEqual(res.z, 3.0, places=4)

    def test_init_wrong(self) -> None:
        with self.assertRaises(ValueError):
            Point(x=1.0, y=2, z="drei")

    def test_as_tuple(self) -> None:
        res = Point()
        res.as_tuple = (1, 2, 3,)
        self.assertIsInstance(res.x, float)
        self.assertIsInstance(res.y, float)
        self.assertIsInstance(res.z, float)
        self.assertAlmostEqual(res.x, 1.0, places=4)
        self.assertAlmostEqual(res.y, 2.0, places=4)
        self.assertAlmostEqual(res.z, 3.0, places=4)
        self.assertTupleEqual(res.as_tuple, (1.0, 2.0, 3.0,))

    def test_as_list(self) -> None:
        res = Point()
        res.as_list = [1, 2, 3]
        self.assertIsInstance(res.x, float)
        self.assertIsInstance(res.y, float)
        self.assertIsInstance(res.z, float)
        self.assertAlmostEqual(res.x, 1.0, places=4)
        self.assertAlmostEqual(res.y, 2.0, places=4)
        self.assertAlmostEqual(res.z, 3.0, places=4)
        self.assertListEqual(res.as_list, [1.0, 2.0, 3.0])


if __name__ == "__main__":
    unittest.main()