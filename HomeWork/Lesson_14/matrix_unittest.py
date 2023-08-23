from HomeWork.Lesson_11.matrix import Matrix
import unittest


class TestMatrix(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 2, 1]])
        self.matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 2, 0]])
        self.matrix_3 = Matrix([[1, 2], [3, 4]])
        self.matrix_4 = Matrix([[5, 6], [7, 8]])
        self.matrix_5 = Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 2, 1]])

    def test_sum(self):
        self.assertEqual(self.matrix_1 + self.matrix_2, Matrix([[2, 4, 6], [8, 10, 12], [2, 4, 6], [6, 4, 1]]))

    def test_sub(self):
        self.assertEqual(self.matrix_4 - self.matrix_3, Matrix([[4, 4], [4, 4]]))

    def test_mul(self):
        self.assertEqual(self.matrix_3 * self.matrix_4, Matrix([[19, 22], [43, 50]]))

    def test_gt(self):
        self.assertGreater(self.matrix_4, self.matrix_3, True)

    def test_eq(self):
        self.assertEquals(self.matrix_1 == self.matrix_2, False)
        self.assertEquals(self.matrix_1 == self.matrix_5, True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
