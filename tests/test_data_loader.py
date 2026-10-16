import os
import sys
import unittest

# 1. Path Safety Hook: Ensure Python can see the code inside the 'src' folder
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Import the specific functions and asset map we want to test
from data_loader import enrich_alert_context, MOCK_CMDB

class TestSecurityDataLoader(unittest.TestCase):
    """Automated verification suite testing our SOC asset matching logic rules."""

    def test_critical_asset_matching(self):
        """VERIFICATION 1: Ensure the Finance IP sets a Critical score of 10."""
        sample_alert = {
            "source_ip": "10.0.0.12",
            "signature": "Test Database Scan",
            "mitre_technique": "T1059"
        }
        
        # Execute the code logic
        result = enrich_alert_context(sample_alert)
        
        # Assert checks (Self-verifying checkpoints)
        self.assertEqual(result["asset_name"], "Fin-SQL-Prod-01")
        self.assertEqual(result["department"], "Finance & Payroll")
        self.assertEqual(result["calculated_risk_score"], 10)
        self.assertIn("IMMEDIATE ESCALATION", result["triage_priority_tier"])

    def test_medium_asset_matching(self):
        """VERIFICATION 2: Ensure the HR IP sets a Medium score of 5."""
        sample_alert = {
            "source_ip": "192.168.1.45",
            "signature": "Test PowerShell Execution",
            "mitre_technique": "T1059"
        }
        
        result = enrich_alert_context(sample_alert)
        
        self.assertEqual(result["asset_name"], "HR-Laptop-01")
        self.assertEqual(result["calculated_risk_score"], 5)

    def test_unknown_asset_fallback(self):
        """VERIFICATION 3: Ensure an unmapped IP safely drops to Low score of 1."""
        sample_alert = {
            "source_ip": "8.8.8.8", # Random external IP not in our network map
            "signature": "Unregistered Traffic",
            "mitre_technique": "T1059"
        }
        
        result = enrich_alert_context(sample_alert)
        
        # Verify the safety fallback logic caught the mystery IP
        self.assertEqual(result["asset_name"], "Unknown Asset")
        self.assertEqual(result["calculated_risk_score"], 1)
        self.assertEqual(result["triage_priority_tier"], "LOW-RISK MONITORING")

if __name__ == "__main__":
    unittest.main()
