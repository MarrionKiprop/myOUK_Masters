import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def reconstruct_matrix(A):
    
    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)

    # Form the diagonal matrix of eigenvalues
    D = np.diag(eigenvalues)

    # Compute the inverse of the matrix of eigenvectors
    P = np.linalg.inv(eigenvectors)

    # Reconstruct the matrix
    A_reconstructed = np.dot(np.dot(eigenvectors,D), P)

    return A_reconstructed, eigenvalues, eigenvectors

def visualize_eigenvectors(A):
    """
    
    """
    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)

    # Plot the heatmap of the matrix
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    sns.heatmap(A, annot=True, cmap="viridis", cbar=True)
    plt.title("Matrix A Heatmap")

    # Plot the eigenvectors
    plt.subplot(1, 2, 2)
    origin = np.array([0, 0])
    for i in range(len(eigenvalues)):
        eigenvector = eigenvectors[:, i]
        eigenvalue = eigenvalues[i]
        plt.quiver(*origin, eigenvector[0], eigenvector[1], angles='xy', scale_units='xy', scale=1, color=f'C{i}', label=f"\u03BB={eigenvalue:.2f}")

    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title("Eigenvectors")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    A = np.array([[4, 2],
                  [1, 3]])
    A_reconstructed, eigenvalues, eigenvectors = reconstruct_matrix(A)

    print("Original Matrix:")
    print(A)
    print("\nEigenvalues:")
    print(eigenvalues)
    print("\nEigenvectors:")
    print(eigenvectors)
    print("\nReconstructed Matrix:")
    print(A_reconstructed)

    visualize_eigenvectors(A)
