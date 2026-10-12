"""
Module: data_loader.py (Policy Fallback Version)
Description: Ingests raw JSON security data using native Python standard libraries 
             to safely bypass strict Windows Application Control policies.
Author: Umm-e-Rubab Muhammad Iqbal
"""
import os
import json

def load_and_clean_logs(file_path: str):
    """Safely reads and tokenizes JSON log sequences using zero external binaries."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The target log file could not be found at: {file_path}")
        
    print(f"📖 Reading raw security logs using native OS tools from: {file_path}")
    
    # Using Python's native built-in JSON parser (Completely trusted by Windows Policy)
    with open(file_path, 'r') as file:
        logs_data = json.load(file)
        
    print("\n--- Raw Log Array View (Bypassed Windows Policy!) ---")
    print(json.dumps(logs_data, indent=2))
    
    # Manual categorical transformation mapping
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
        
    print("\n--- Clean Numerical Matrix View (Ready for AI Brain) ---")
    for row in numerical_matrix:
        print(row)
        
    return numerical_matrix

if __name__ == "__main__":
    test_path = os.path.join("data", "raw", "sample_logs.json")
    try:
        load_and_clean_logs(test_path)
    except Exception as e:
        print(f"❌ Error encountered: {e}")