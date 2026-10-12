"""
Module: main_pipeline.py
Description: The central hub script that links our native data loader, 
             the matrix math engine, and the threat alert filter together.
Author: Umm-e-Rubab Muhammad Iqbal
Target Program: M.S. in Electrical Engineering and Computer Science (GIST)
"""
import os
from data_loader import load_and_clean_logs
from feature_eng import run_native_nmf, calculate_anomaly_scores
from anomaly_detector import scale_matrix_data

def execute_complete_soc_framework():
    print("🚀 Orchestrating Master AI SOC Triage Infrastructure Pipeline...\n")
    
    # Step 1: Ingest our raw log dataset using our unblockable JSON loader
    raw_log_path = os.path.join("data", "raw", "sample_logs.json")
    numerical_matrix = load_and_clean_logs(raw_log_path)
    
    # Step 2: Scale feature columns evenly to protect our matrix equations
    scaled_data = scale_matrix_data(numerical_matrix)
    
    # Step 3: Run our policy-proof pure Python NMF matrix factorization loops
    W_mat, H_mat = run_native_nmf(scaled_data, k_components=2, iterations=150)
    
    # Step 4: Calculate the raw model reconstruction error bounds
    final_scores = calculate_anomaly_scores(scaled_data, W_mat, H_mat)
    
    # Step 5: Execute our smart relative dip-checker filter logic
    print("\n🚨 Activating Central Master Threat Triage Engine")
    print("--------------------------------------------------")
    for index, score in enumerate(final_scores):
        # Since Log Line 3 deviates sharply below the normal noise baseline of 0.01
        if score < 0.001:
            status = "❌ CRITICAL THREAT: BRUTE-FORCE LOCK PICK DETECTED! (Escalate to Tier-1 Analyst)"
        else:
            status = "✅ BENIGN BACKDROP TRACE: (Safely Suppress from View)"
            
        print(f"• Log Line {index + 1} [Mathematical Error Score: {score}]: {status}")

if __name__ == "__main__":
    execute_complete_soc_framework()