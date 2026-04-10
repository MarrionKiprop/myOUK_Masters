import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate a random matrix A and add noise
np.random.seed(0)
A = np.random.rand(5, 5)  # Original matrix
noise = np.random.normal(0, 0.1, A.shape)  # Random noise
A_noisy = A + noise  # Noisy matrix

# Step 2: Perform SVD on the noisy matrix
U, S, VT = np.linalg.svd(A_noisy, full_matrices=False)

# Step 3: Reconstruct a low-rank approximation of A using top singular values
k = 2
U_k = U[:, :k]
S_k = np.diag(S[:k])
VT_k = VT[:k, :]
A_denoised = U_k @ S_k @ VT_k

# Step 4: Compare matrices using visualizations and Frobenius norm
frobenius_original = np.linalg.norm(A, 'fro')
frobenius_noisy = np.linalg.norm(A_noisy, 'fro')
frobenius_denoised = np.linalg.norm(A_denoised, 'fro')

# Plot the matrices
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(A, cmap='viridis')
axes[0].set_title('Original Matrix')
axes[1].imshow(A_noisy, cmap='viridis')
axes[1].set_title('Noisy Matrix')
axes[2].imshow(A_denoised, cmap='viridis')
axes[2].set_title('Denoised Matrix')

for ax in axes:
    ax.axis('off')

plt.show()

# Output Frobenius norms
print("Frobenius norm of original matrix:", frobenius_original)
print("Frobenius norm of noisy matrix:", frobenius_noisy)
print("Frobenius norm of denoised matrix:", frobenius_denoised)
