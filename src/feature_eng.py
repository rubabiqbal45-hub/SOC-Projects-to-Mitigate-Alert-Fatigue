"""
Module: feature_eng.py (Policy-Proof Native NMF Version)
Description: Executes custom Non-Negative Matrix Factorization (V ≈ WH) 
             using zero external compiled binaries to bypass system blocks.
Author: Umm-e-Rubab Muhammad Iqbal
Target Program: M.S. in Electrical Engineering and Computer Science (GIST)
"""
import random

def matrix_multiply(A, B):
    """Native helper tool to multiply two numerical matrices together."""
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    # Standard nested dot product loops
    result = [[0.0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

def run_native_nmf(V_matrix, k_components=2, iterations=100):
    """
    Decomposes incoming logs (V) into a Basis Matrix (W) and Component Matrix (H).
    Uses multiplicative update rules to ensure values stay positive.
    """
    m_samples = len(V_matrix)
    n_features = len(V_matrix[0])
    
    print(f"\n⚙️ Running custom NMF Core. Latent Feature Bottleneck (k) = {k_components}")
    
    # Step 1: Initialize matrices W and H with random small numbers
    random.seed(42)
    W = [[random.uniform(0.1, 1.0) for _ in range(k_components)] for _ in range(m_samples)]
    H = [[random.uniform(0.1, 1.0) for _ in range(n_features)] for _ in range(k_components)]
    
    # Step 2: Run Multiplicative Update Loops to minimize reconstruction error
    for _ in range(iterations):
        # Compute current approximation: V_prime = W x H
        V_prime = matrix_multiply(W, H)
        
        # Update Coefficient Matrix H
        for i in range(k_components):
            for j in range(n_features):
                numerator = 0.0
                denominator = 0.0
                for k in range(m_samples):
                    numerator += W[k][i] * V_matrix[k][j]
                    denominator += W[k][i] * V_prime[k][j]
                if denominator > 0:
                    H[i][j] *= (numerator / denominator)
                    
        # Update Basis Matrix W
        V_prime = matrix_multiply(W, H)
        for i in range(m_samples):
            for j in range(k_components):
                numerator = 0.0
                denominator = 0.0
                for k in range(n_features):
                    numerator += V_matrix[i][k] * H[j][k]
                    denominator += V_prime[i][k] * H[j][k]
                if denominator > 0:
                    W[i][j] *= (numerator / denominator)

    print("✅ Matrix Factorization Complete!")
    return W, H

def calculate_anomaly_scores(V, W, H):
    """Computes the squared error difference between raw data and the NMF model."""
    V_prime = matrix_multiply(W, H)
    scores = []
    
    for i in range(len(V)):
        row_error = 0.0
        for j in range(len(V[0])):
            row_error += (V[i][j] - V_prime[i][j]) ** 2
        scores.append(round(row_error, 4))
        
    return scores

if __name__ == "__main__":
    # Test Data block using output directly from our active loader layer
    mock_matrix = [
        [0.0, 0.0, 1.2, 0.0],
        [1.0, 1.0, 0.5, 0.0],
        [0.0, 2.0, 7.4, 12.0],  # Our hidden lock-picking attack signature
        [2.0, 3.0, 0.1, 0.0],
        [0.0, 0.0, 1.5, 1.0]
    ]
    
    W_mat, H_mat = run_native_nmf(mock_matrix, k_components=2)
    reconstruction_errors = calculate_anomaly_scores(mock_matrix, W_mat, H_mat)
    
    print("\n--- Model Reconstruction Anomaly Metrics ---")
    for index, error in enumerate(reconstruction_errors):
        print(f"• Log Line {index + 1} Anomaly Score: {error}")