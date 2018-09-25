'''
CME 193, HW #1 
'''

# Import things you might need here.
# I recommend array...
import array


class Matrix(object):
	"""
	Instructions: fill out the sections of code marked with 

		pass #IMPLEMENT

	and MAKE SURE and read all of the comments in the code here.

	*****
	DONT FORGET to remove all pass statements
	*****

	"""
	
	def __init__(self, data=None, shape=None, dtype='f'):
		'''
		data: can be some initial data that you pass in the form of 
		something like a list of lists.

		shape: can be a tuple of length 2 describing (nb_rows, nb_columns) 
		of your matrix. 

		dtype: can be one of 'f' or 'i' for float or int

		logically, you can have three scenarios for instantiation:

		1)	someone passes data, but no shape. If the data is nested, i.e., a
			list of lists, it checks to make sure the dimensions make a 
			rectangle. If this fails, raise a ValueError!
			If just a list, then makes a (nb_elements, 1) shaped matrix

		2) 	someone passes data and a shape. We need to make sure that the 
			dimensions of the data match the shape if the data is a list
			of lists. If the data is one list of numbers, we need to make 
			sure that nb_elements = shape[0] * shape[1]. If anything fails, 
			raise a ValueError

		3)	Someone passes just a shape. In this case, we'll assume we want
			to initialize the matrix with all zeros.

		Internally, you can represent your matrix with anything that is not a 
		matrix class itself (i.e., no numpy!) I recommend using the array 
		built-in from python. https://docs.python.org/2/library/array.html

		Read on for more specifications...
		'''
		pass #IMPLEMENT

	def shape(self):
		'''
		Return the shape of the current matrix
		'''
		pass #IMPLEMENT

	def __getitem__(self, indices):
		'''
		This method will implement A[i, j] of the matrix, and will return a 
		copy of the element. Note that the perfect way of doing this would allow
		for slices, but we won't do that for simplicity. This is one of those 
		special functions that python implicitly calls.

		Example:
		>>> M = Matrix(...)
		>>> a = M[0, 3]

		REQUIRED: **Return** the i, j element. Raise an IndexError if i, j is not valid
		for the given matrix size.
		'''
		assert len(indices) == 2
		i, j = indices # can unpack two indices!
		pass #IMPLEMENT

	def __setitem__(self, indices, value):
		'''
		This method will implement the set method of A[i, j] of the matrix.
		Note that the perfect way of doing this would allow
		for slices, but we won't do that for simplicity. This is one of those 
		special functions that python implicitly calls.

		Example:
		>>> M = Matrix(...)
		>>> M[0, 3] = value

		REQUIRED: **Set** the i, j element with value. Raise an 
		IndexError if i, j is not valid for the given matrix size.
		'''
		assert len(indices) == 2
		i, j = indices
		pass #IMPLEMENT

	def __add__(self, X):
		'''
		Perform M + X, where X is either another matrix or a number.

		Raise a ValueError if the dimensions don'm match in the case 
		of a Matrix
		'''
		pass #IMPLEMENT

	def __radd__(self, X):
		'''
		Perform x + M, where x is a number.
		'''
		pass #IMPLEMENT

	def __mul__(self, X):
		'''
		Perform M * X (a matrix product!), where X is either another 
		matrix or a number.

		Raise a ValueError if the dimensions don'm match in the case 
		of a Matrix Matrix multiplication. 

		For documentation on how to do a matrix multiplication, consult
		with https://en.wikipedia.org/wiki/Matrix_multiplication
		'''
		pass #IMPLEMENT

	def __rmul__(self, X):
		'''
		Perform X * M where X is a number.
		'''
		pass #IMPLEMENT










		