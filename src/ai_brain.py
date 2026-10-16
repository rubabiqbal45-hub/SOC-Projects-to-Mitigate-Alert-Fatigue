import os
import json

class FreeAIBrainSimulation:
    """
    A local, deterministic simulation matrix that mimics an LLM endpoint.
    Ensures the student pipeline executes perfectly without requiring premium API keys.
    """
    def __init__(self):
        print("🚀 Success: Open-Source AI Simulation Engine active and ready!")

    def invoke(self, data_dict):
        # Read incoming data points dynamically
        signature = data_dict.get('signature', 'Unknown Threat')
        mitre = data_dict.get('mitre_technique', 'T1059')
        asset = data_dict.get('asset_name', 'Endpoint Host')
        dept = data_dict.get('department', 'General Operations')
        criticality = data_dict.get('criticality', 'Low')
        
        # Calculate dynamic triage playbook outputs based on your data structures
        if criticality == "Critical":
            threat_rationale = f"CRITICAL THREAT. This activity targets {asset} within the {dept} division. Immediate isolation required."
            countermeasure = "Isolate the host from the network trunk line immediately and revoke active domain tokens."
        else:
            threat_rationale = f"MEDIUM THREAT. Activity detected on standard corporate asset ({asset}) in {dept}."
            countermeasure = "Schedule a full host antivirus scan and clear the temporary script execution cache files."

        # Construct a perfectly formatted 3-sentence natural language report
        report = f"""- SUMMARY: A suspicious automation instance ({signature}) matching MITRE technique {mitre} was flagged on your network endpoint.
- THREAT LEVEL: {threat_rationale}
- INITIAL COUNTERMEASURE: {countermeasure}"""
        
        return report

# Expose the simulation instance to keep the pipeline intact
ai_analysis_chain = FreeAIBrainSimulation()
