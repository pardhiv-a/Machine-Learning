# A1
import numpy as np

A= np.array([[20, 6, 2],[16, 3, 6],[27, 6, 2],[19, 1, 2],[24, 4, 2],[22, 1, 5],[15, 4, 2],[18, 4, 2],[21, 1, 4],[16, 2, 4]])
C = np.array([[386],[289],[393],[110],[280],[167],[271],[274],[148],[198]])
cols = A.shape[1]
rows = C.shape[0]

_, singular_vals, _ = np.linalg.svd(C)
matrix_rank = sum(val > 1e-10 for val in singular_vals)

pseudo_inv = np.linalg.pinv(products)
costs = pseudo_inv @ payments

print("RESULTS:")
print(f"Dimensionality of vector space : {cols}")
print(f"Number of vectors              : {rows}")
print(f"Rank of Matrix A               : {matrix_rank}")
print("\nEstimated cost of each product:")
print(f"Cost of 1 Candy       : Rs {costs[0][0]:.2f}")
print(f"Cost of 1 Kg Mango    : Rs {costs[1][0]:.2f}")
print(f"Cost of 1 Milk Packet : Rs {costs[2][0]:.2f}")