from util import test, summary
from matrix import Matrix

if __name__ == '__main__':
	M = Matrix(shape=(4, 5))

	test(M.shape() == (4, 5), 'M.shape() test')

	test(M[0, 0] == 0, 'M[0, 0] == 0 test')

	M[0, 0] = 3

	test(M[0, 0] == 3, 'M[0, 0] == 3 (setter) test')

	a = M[0, 0]

	test(a == 3, 'a == 3 (getter) test')

	summary()

