"""
Module: main_pipeline.py (Self-Contained Architecture)
Description: Complete merged framework containing log ingestion, custom NMF 
             matrix loops, threshold checking, and simulated LLM triage.
Author: Umm-e-Rubab Muhammad Iqbal
Target Program: M.S. in Electrical Engineering and Computer Science (GIST)
"""
import os
import json
import random

# ==========================================
# LAYER 1: Native Data Loader
# ==========================================
def load_and_clean_logs(file_path: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Missing file: {file_path}")
        
    print(f"📖 Ingesting security logs using native OS tools from: {file_path}")
    with open(file_path, 'r') as file:
        logs_data = json.load(file)
        
    protocol_map = {"TCP": 0, "UDP": 1, "ICMP": 2}
    service_map = {"HTTP": 0, "DNS": 1, "SSH": 2, "PING": 3}
    
    numerical_matrix = []
    for log in logs_data:
        numeric_log = [
            float(protocol_map.get(log["protocol_type"], 99)),
            float(service_map.get(log["service_flag"], 99)),
            float(log["payload_entropy"]),
            float(log["login_failures"])
        ]
        numerical_matrix.append(numeric_log)
    return numerical_matrix, logs_data

# ==========================================
# LAYER 2: Value Scaling 
# ==========================================
def scale_matrix_data(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    scaled_matrix = [[0.0 for _ in range(num_cols)] for _ in range(num_rows)]
    
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

# ==========================================
# LAYER 3: Pure Python NMF Core Engine
# ==========================================
def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    cols_B = len(B[0])
    result = [[0.0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

def run_native_nmf(V_matrix, k_components=2, iterations=150):
    m_samples = len(V_matrix)
    n_features = len(V_matrix[0])
    
    random.seed(42)
    W = [[random.uniform(0.1, 1.0) for _ in range(k_components)] for _ in range(m_samples)]
    H = [[random.uniform(0.1, 1.0) for _ in range(n_features)] for _ in range(k_components)]
    
    for _ in range(iterations):
        V_prime = matrix_multiply(W, H)
        for i in range(k_components):
            for j in range(n_features):
                numerator = 0.0
                denominator = 0.0
                for k in range(m_samples):
                    numerator += W[k][i] * V_matrix[k][j]
                    denominator += W[k][i] * V_prime[k][j]
                if denominator > 0:
                    H[i][j] *= (numerator / denominator)
                    
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
    return W, H

def calculate_anomaly_scores(V, W, H):
    V_prime = matrix_multiply(W, H)
    scores = []
    for i in range(len(V)):
        row_error = 0.0
        for j in range(len(V[0])):
            row_error += (V[i][j] - V_prime[i][j]) ** 2
        scores.append(round(row_error, 4))
    return scores

# ==========================================
# LAYER 4: Local LLM Threat Triage Agent
# ==========================================
def generate_plain_english_summary(log_index: int, raw_log_data: dict):
    print(f"\n🧠 [Local LLM Engine] Parsing Escalated Incident Context for Log Line {log_index}...")
    protocol = raw_log_data.get("protocol_type", "Unknown")
    service = raw_log_data.get("service_flag", "Unknown")
    entropy = raw_log_data.get("payload_entropy", 0.0)
    failures = raw_log_data.get("login_failures", 0)
    
    summary = (
        f"[EXPLOIT VECTOR EVALUATION]: A critical anomaly was detected using the {protocol} protocol "
        f"targeting enterprise {service} infrastructure. [THREAT MATRIX HIGHLIGHT]: The payload exhibits an elevated "
        f"structural entropy score of {entropy}, indicating obfuscated payloads or unauthorized administrative command entry. "
        f"[SOC INCIDENT TRIAGE ACTION]: Systems registered {failures} consecutive authentication failures, pointing to a "
        f"Brute-Force lock-picking campaign. Recommendation: Instantly isolate host vectors and rotate access tokens."
    )
    return summary

# ==========================================
# COORDINTATOR: Master Orchestration Execution
# ==========================================
def execute_complete_soc_framework():
    print("🚀 Orchestrating Unified Master AI SOC Triage Infrastructure Pipeline...\n")
    
    raw_log_path = os.path.join("data", "raw", "sample_logs.json")
    numerical_matrix, raw_text_records = load_and_clean_logs(raw_log_path)
    
    scaled_data = scale_matrix_data(numerical_matrix)
    W_mat, H_mat = run_native_nmf(scaled_data, k_components=2, iterations=150)
    final_scores = calculate_anomaly_scores(scaled_data, W_mat, H_mat)
    
    print("\n🚨 Activating Central Master Threat Triage Engine")
    print("--------------------------------------------------")
    for index, score in enumerate(final_scores):
        if score < 0.001:
            status = "❌ CRITICAL THREAT DETECTED!"
            print(f"\n• Log Line {index + 1} [Mathematical Error Score: {score}]: {status}")
            llm_report = generate_plain_english_summary(index + 1, raw_text_records[index])
            print(f"📄 Auto-Generated Assessment:\n{llm_report}\n")
        else:
            status = "✅ BENIGN BACKDROP TRACE: (Safely Suppress from View)"
            print(f"• Log Line {index + 1} [Mathematical Error Score: {score}]: {status}")

if __name__ == "__main__":
    execute_complete_soc_framework()