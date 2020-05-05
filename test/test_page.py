
import unittest
from generalvector.vector2 import Vec2

class Vector2Test(unittest.TestCase):
    def test_vector2(self):
        self.assertRaises(TypeError, Vec2, "")
        self.assertRaises(TypeError, Vec2, None, 5)

        self.assertEqual(Vec2(5, 2).x, 5)
        self.assertEqual(Vec2(5, 2).y, 2)
        self.assertEqual(Vec2(5.2, 2).x, 5.2)
        self.assertEqual(Vec2(5.2, 2.5).y, 2.5)
        self.assertEqual(Vec2(5).x, 5)
        self.assertEqual(Vec2(5).y, 5)

    def test_equal(self):
        self.assertRaises(TypeError, Vec2.__eq__, "")

        self.assertTrue(Vec2(1) == Vec2(1))
        self.assertTrue(Vec2(1, 2) == Vec2(1, 2))
        self.assertTrue(Vec2(1, 1) == 1)
        self.assertTrue(Vec2(5.2, 5.2) == 5.2)

        self.assertFalse(Vec2(1, 2) == Vec2(1, 3))
        self.assertFalse(Vec2(1, 2) == Vec2(2, 2))
        self.assertFalse(Vec2(1, 1) == 2)
        self.assertFalse(Vec2(5.2, 5.2) == 5)

    def test_add(self):
        self.assertRaises(TypeError, Vec2.__add__, "")
        self.assertRaises(TypeError, Vec2.__add__, False)


        self.assertEqual(Vec2(5, 2) + Vec2(2, 4), Vec2(7, 6))
        self.assertEqual(Vec2(5, 2) + Vec2(2.5, 4.5), Vec2(7.5, 6.5))
        self.assertEqual(Vec2(5, 2) + Vec2(-2, -4), Vec2(3, -2))
        self.assertEqual(Vec2(5, 2) + 3, Vec2(8, 5))
        self.assertEqual(Vec2(5, 2) + -3, Vec2(2, -1))
        self.assertEqual(Vec2(5, 2) + 3.5, Vec2(8.5, 5.5))

    def test_sub(self):
        self.assertRaises(TypeError, Vec2.__sub__, "")
        self.assertRaises(TypeError, Vec2.__sub__, True)

        self.assertEqual(Vec2(5, 2) - Vec2(2, 4), Vec2(3, -2))
        self.assertEqual(Vec2(5, 2) - Vec2(-2, -4), Vec2(7, 6))
        self.assertEqual(Vec2(5, 2) - 3, Vec2(2, -1))
        self.assertEqual(Vec2(5, 2) - -3, Vec2(8, 5))
        self.assertEqual(Vec2(5, 2) - 3.5, Vec2(1.5, -1.5))

    def test_mul(self):
        self.assertRaises(TypeError, Vec2.__mul__, "")
        self.assertRaises(TypeError, Vec2.__mul__, True)
        self.assertRaises(NotImplementedError, Vec2(5, 2).__mul__, Vec2(5, 2))

        self.assertEqual(Vec2(5, 2) * 2, Vec2(10, 4))
        self.assertEqual(Vec2(5, 2) * 2.5, Vec2(12.5, 5))

    def test_div(self):
        self.assertRaises(TypeError, Vec2.__truediv__, "")
        self.assertRaises(TypeError, Vec2.__truediv__, False)
        self.assertRaises(NotImplementedError, Vec2(5, 2).__truediv__, Vec2(5, 2))

        self.assertEqual(Vec2(5, 2) / 2, Vec2(2.5, 1))
        self.assertEqual(Vec2(10, 5) / 2.5, Vec2(4, 2))

    def test_length(self):
        self.assertEqual(Vec2(10, 0).length(), 10)
        self.assertEqual(Vec2(0, 10).length(), 10)
        self.assertEqual(Vec2(0, 0.2).length(), 0.2)
        self.assertEqual(Vec2(0, 0).length(), 0)

    def test_normalized(self):
        self.assertEqual(Vec2(10, 0).normalized(), Vec2(1, 0))
        self.assertEqual(Vec2(0, 10).normalized(), Vec2(0, 1))
        self.assertEqual(Vec2(0, 0.2).normalized(), Vec2(0, 1))
        self.assertEqual(Vec2(0, 0).normalized(), Vec2(0, 0))
        self.assertEqual(Vec2(0, -10).normalized(), Vec2(0, -1))

