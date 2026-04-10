import numpy as np
import matplotlib.pyplot as plt

def perform_svd(A):
    U, S, VT = np.linalg.svd(A, full_matrices=False)
    return U, S, VT

def plot_singular_values(S):
    plt.figure()
    plt.plot(range(1, len(S) + 1), S, 'o-', label="Singular Values")
    plt.xlabel("Index")
    plt.ylabel("Singular Value")
    plt.title("Singular Values of the Matrix")
    plt.grid()
    plt.legend()
    plt.show()

def reconstruct_with_truncation(U, S, VT, k):
    U_k = U[:, :k]
    S_k = np.diag(S[:k])
    VT_k = VT[:k, :]
    return U_k @ S_k @ VT_k

def visualize_approximations(A, U, S, VT):
    ranks = [1, 2]
    plt.figure(figsize=(10, 5))
    for i, k in enumerate(ranks, start=1):
        A_approx = reconstruct_with_truncation(U, S, VT, k)
        plt.subplot(1, len(ranks), i)
        plt.imshow(A_approx, cmap='viridis', aspect='auto')
        plt.colorbar()
        plt.title(f"SVD Approximation (k={k})")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    A = np.array([[3, 2, 2],
                  [2, 3, -2]])

    U, S, VT = perform_svd(A)
    A_reconstructed = U @ np.diag(S) @ VT

    print("Original Matrix A:\n", A)
    print("\nMatrix U:\n", U)
    print("\nSingular Values S:\n", S)
    print("\nMatrix VT:\n", VT)
    print("\nReconstructed Matrix A:\n", A_reconstructed)

    plot_singular_values(S)
    visualize_approximations(A, U, S, VT)
