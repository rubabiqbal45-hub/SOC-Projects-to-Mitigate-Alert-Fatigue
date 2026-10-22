"""
Module: anomaly_detector.py
Description: Scales raw matrix data to ensure fair math, and implements 
             an automated threshold checker to filter out background noise.
Author: Umm-e-Rubab Muhammad Iqbal
"""

def scale_matrix_data(matrix):
    """
    Teacher Trick: Scales all matrix values between 0.0 and 1.0.
    This prevents columns with large numbers from breaking our NMF models.
    """
    if not matrix:
        return matrix
        
    num_cols = len(matrix[0])
    num_rows = len(matrix)
    
    # Initialize a blank matrix of the exact same size
    scaled_matrix = [[0.0 for _ in range(num_cols)] for _ in range(num_rows)]
    
    # Scale each column independently
    for col in range(num_cols):
        col_values = [matrix[row][col] for row in range(num_rows)]
        min_val = min(col_values)
        max_val = max(col_values)
        val_range = max_val - min_val
        
        for row in range(num_rows):
            if val_range > 0:
                scaled_matrix[row][col] = (matrix[row][col] - min_val) / val_range
            else:
                scaled_matrix[row][col] = 0.0
                
    return scaled_matrix

def run_threshold_alert_checker(anomaly_scores, threshold=0.35):
    """
    Automated Checker: Compares anomaly scores against a mathematical baseline.
    Filters out background noise and flags true threats to reduce alert fatigue.
    """
    print(f"\n🚨 Activating Automated Threshold Checker (Limit Baseline = {threshold})")
    
    triage_results = []
    for index, score in enumerate(anomaly_scores):
        if score >= threshold:
            status = "❌ CRITICAL THREAT (Escalate to Tier-1 Analyst)"
        else:
            status = "✅ BENIGN BACKGROUND NOISE (Safely Suppress)"
            
        print(f"• Log Line {index + 1} [Score: {score}]: {status}")
        triage_results.append(status)
        
    return triage_results

if __name__ == "__main__":
    # Test data processing cycle
    raw_mock_matrix = [
        [0.0, 0.0, 1.2, 0.0],
        [1.0, 1.0, 0.5, 0.0],
        [0.0, 2.0, 7.4, 12.0],  # Lock-picking dragon attack signature
        [2.0, 3.0, 0.1, 0.0],
        [0.0, 0.0, 1.5, 1.0]
    ]
    
    # 1. Scale data smoothly first
    from src.Project_1_NMF_Mitigation.feature_eng import run_native_nmf, calculate_anomaly_scores
    scaled_data = scale_matrix_data(raw_mock_matrix)
    
    # 2. Re-run matrix mathematical logic over adjusted fields
    W_mat, H_mat = run_native_nmf(scaled_data, k_components=2)
    corrected_scores = calculate_anomaly_scores(scaled_data, W_mat, H_mat)
    
    # 3. Triage through alert filter logic bounds
    run_threshold_alert_checker(corrected_scores)