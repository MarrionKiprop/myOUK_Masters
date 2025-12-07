import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def pca_with_svd(data, k=2):
    U, S, VT = np.linalg.svd(data, full_matrices=False)
    V_k = VT[:k, :]
    projected_data = data @ V_k.T
    return projected_data

def plot_2d_projection(projected_data, labels):
    plt.figure(figsize=(8, 6))
    plt.scatter(projected_data[:, 0], projected_data[:, 1], c=labels, cmap='viridis', edgecolor='k', s=100)
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.title("2D Projection of Iris Dataset (PCA using SVD)")
    plt.colorbar(label='Species')
    plt.show()

iris = load_iris()
data = iris.data
labels = iris.target

data_centered = data - np.mean(data, axis=0)

projected_data = pca_with_svd(data_centered, k=2)

plot_2d_projection(projected_data, labels)
