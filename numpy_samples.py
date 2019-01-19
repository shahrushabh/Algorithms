import numpy as np

""" Mathematical & statistical computations in python with NumPy """


""" Matricies computations """

m = np.array([[1,5,2],
            [4,7,4],
            [2,0,9]])

print('Matrix is :\n', m)
print('Matrix with shape : ', m.shape)

# Matrix determinent prior
print('Matrix determinent : ', np.linalg.det(m))

# Matrix transpose
print('Matrix transpose : ', m.transpose())

# Matrix inverse
print('Matrix inverse : ', np.linalg.inv(m))

# Transposed Matrix determinent
print('Matrix determinent : ', np.linalg.det(m))





""" Eigen Vactors and values """
eigen_vals,eigen_vecs = np.linalg.eig(m)

print('Eigne values : ' , eigen_vals)
print('Eigen Vectors : ' , eigen_vecs)
