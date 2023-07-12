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


if __name__ == "__main__":
    unittest.main()