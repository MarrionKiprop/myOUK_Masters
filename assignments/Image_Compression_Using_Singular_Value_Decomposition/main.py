import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

def perform_svd_compression(image, k_values):
   
    # Perform SVD on the image matrix
    U, S, VT = np.linalg.svd(image, full_matrices=False)
    compressed_images = {}

    for k in k_values:
        # Truncate U, S, and VT for rank k
        U_k = U[:, :k]
        S_k = np.diag(S[:k])
        VT_k = VT[:k, :]

        # Reconstruct the image with reduced rank
        compressed_image = U_k @ S_k @ VT_k
        compressed_images[k] = compressed_image

    return compressed_images

def plot_images(original_image, compressed_images):
   
    num_images = len(compressed_images) + 1
    plt.figure(figsize=(15, 5))

    # Plot the original image
    plt.subplot(1, num_images, 1)
    plt.imshow(original_image, cmap='gray')
    plt.title("Original Image")
    plt.axis('off')

    # Plot compressed images
    for i, (k, img) in enumerate(compressed_images.items(), start=2):
        plt.subplot(1, num_images, i)
        plt.imshow(img, cmap='gray')
        plt.title(f"Compressed (k={k})")
        plt.axis('off')

    plt.tight_layout()
    plt.show()

# Main Functionality
if __name__ == "__main__":
    # Load the image as a grayscale matrix
    image = imread('image_compresionjpg.jpg')
    if len(image.shape) == 3:  # Convert to grayscale if not already
        image = image.mean(axis=-1)

    # Define k values for testing
    k_values = [5, 20, 50]

    # Perform SVD compression
    compressed_images = perform_svd_compression(image, k_values)

    # Plot the original and compressed images
    plot_images(image, compressed_images)

    
    

