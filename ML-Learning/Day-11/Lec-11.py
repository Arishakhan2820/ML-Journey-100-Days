# ==========================================================
# Day 11: Comprehensive Tensor Creation & Manipulation Script
# ==========================================================

import numpy as np

print("=" * 60)
print(" 1. EXPLORING TENSOR RANKS, SHAPES, AND SIZES")
print("=" * 60)

# --- Scalar (0D Tensor) ---
scalar_tensor = np.array(42)
print(f"Scalar Value       : {scalar_tensor}")
print(f"Scalar Rank (Dim)  : {scalar_tensor.ndim}")
print(f"Scalar Shape       : {scalar_tensor.shape}")
print(f"Scalar Size        : {scalar_tensor.size}\n")

# --- Vector (1D Tensor) ---
# Example: Student features [CGPA, IQ, Test Score]
vector_tensor = np.array([3.6, 115, 88])
print(f"Vector Data        : {vector_tensor}")
print(f"Vector Rank (Dim)  : {vector_tensor.ndim}")
print(f"Vector Shape       : {vector_tensor.shape}")
print(f"Vector Size        : {vector_tensor.size}\n")

# --- Matrix (2D Tensor) ---
# Example: Dataset of 3 students with 3 features each
matrix_tensor = np.array([
    [3.6, 115, 88],
    [3.9, 130, 95],
    [2.8, 95, 60]
])
print(f"Matrix Shape (Students x Features): {matrix_tensor.shape}")
print(f"Matrix Rank (Dims)                : {matrix_tensor.ndim}")
print(f"Matrix Total Size (Elements)      : {matrix_tensor.size}\n")

print("=" * 60)
print(" 2. SIMULATING COMPUTER VISION & NLP TENSORS")
print("=" * 60)

# --- 3D Tensor: Color Image (Height x Width x RGB Channels) ---
# Simulating a miniature 3x3 pixel RGB image
rgb_image_tensor = np.random.randint(0, 256, size=(3, 3, 3))
print(f"3D RGB Image Tensor Shape         : {rgb_image_tensor.shape}")
print(f"-> Explanation: 3 rows, 3 columns, 3 color channels (R, G, B)")

# --- 4D Tensor: Video Data (Frames x Height x Width x Channels) ---
# Simulating a short video clip of 10 frames, each 64x64 pixels with 3 color channels
video_tensor = np.random.rand(10, 64, 64, 3)
print(f"4D Video Tensor Shape             : {video_tensor.shape}")
print(f"-> Explanation: 10 frames, 64x64 spatial resolution, 3 channels")

print("=" * 60)
print(" 3. BASIC TENSOR OPERATIONS & RESHAPING")
print("=" * 60)

# Reshaping a 1D vector into a 2D Matrix
flat_array = np.array([1, 2, 3, 4, 5, 6])
reshaped_matrix = flat_array.reshape(2, 3)

print(f"Original 1D Array : {flat_array}")
print(f"Reshaped 2D Matrix (2x3):\n{reshaped_matrix}")
print(f"New Shape         : {reshaped_matrix.shape}")
print("=" * 60)
