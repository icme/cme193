import numpy as np
import scipy
import scipy.sparse
import matplotlib.pyplot as plt


# part 2 - read sparse matrix from csv file
def read_coo(fname):
    Y = np.loadtxt(fname, delimiter=',')
    rows = np.array(Y[:, 0], int)
    cols = np.array(Y[:, 1], int)
    V = Y[:, 2]
    return scipy.sparse.coo_matrix((np.array(V), (rows, cols)))


A = read_coo("../sbm.csv")


# part 3 - create sparse + Rank-1 class
class sparse_rank1(object):
    def __init__(self, S, alpha, u, v):
        self.S = S
        self.alpha = alpha
        self.u = u
        self.v = v
        self.shape = S.shape

    def dot(self, x):
        return self.S.dot(x) + self.alpha*self.u*self.v.dot(x)


# part 4 - power method

# compute power method
# tol is a key-word argument for convergence tolerance
def power_method(A, tol=1e-8):

    # rayleigh quotient
    # returns v^T*Av
    def rq(v, A):
        return v.dot(A.dot(v))

    n = A.shape[1]
    # generate random vector with unit length
    v = np.random.normal(0, 1, n)
    v /= np.linalg.norm(v)

    rqs = []  # keep track of rayleigh quotients as we progress
    rqs.append(rq(v, A))

    while True:

        # v <- A*v
        v = A.dot(v)
        # normalize v
        v /= np.linalg.norm(v)

        rqs.append(rq(v, A))
        # check if rayleigh quotient has converged
        if np.abs(rqs[-1] - rqs[-2]) < tol:
            break

    # set eigenvalue
    lam = rqs[-1]

    return v, lam


# part 5 - spectral embedding
v, lam = power_method(A)

B = sparse_rank1(A, -lam, v, v)
v2, lam2 = power_method(B)

fig, ax = plt.subplots(1, 1, figsize=(10, 8))

ax.scatter(v, v2)
ax.set_xlabel(r'$v_1$')
ax.set_ylabel(r'$v_2$')
ax.set_title("Spectral Embedding")


plt.savefig('sbm.png')
plt.show()
