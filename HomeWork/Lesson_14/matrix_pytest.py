from HomeWork.Lesson_11.matrix import Matrix
import pytest


@pytest.fixture
def matrix_1():
    return Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 2, 1]])


@pytest.fixture
def matrix_2():
    return Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 2, 0]])


@pytest.fixture
def matrix_3():
    return Matrix([[1, 2], [3, 4]])


@pytest.fixture
def matrix_4():
    return Matrix([[5, 6], [7, 8]])


@pytest.fixture
def matrix_5():
    return Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 2, 1]])


def test_sum_matrix(matrix_1, matrix_2):
    assert matrix_1 + matrix_2 == Matrix([[2, 4, 6], [8, 10, 12], [2, 4, 6], [6, 4, 1]])


def test_sub_matrix(matrix_3, matrix_4):
    assert matrix_4 - matrix_3 == Matrix([[4, 4], [4, 4]])


def test_mul_matrix(matrix_3, matrix_4):
    assert matrix_3 * matrix_4 == Matrix([[19, 22], [43, 50]])


def test_gt_matrix(matrix_4, matrix_3):
    assert matrix_4 > matrix_3


def test_eq_matrix(matrix_1, matrix_5):
    assert matrix_1 == matrix_5


def test_not_eq(matrix_1, matrix_2):
    assert matrix_1 != matrix_2


if __name__ == '__main__':
    pytest.main(['-vv'])
