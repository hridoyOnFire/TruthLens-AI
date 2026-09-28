import unittest
from unittest.mock import MagicMock, patch
from contract import TruthLensEngine

class TestTruthLensEngine(unittest.TestCase):

    def setUp(self):
        self.contract = TruthLensEngine()

    @patch('contract.gl')
    def test_verify_content_success(self, mock_gl):
        # Mocking Web Response from GenLayer Web Connector
        mock_web_response = MagicMock()
        mock_web_response.text = "Breaking News: Major crypto partnership officially announced."
        mock_gl.web.get.return_value = mock_web_response

        # Mocking AI Consensus Response
        mock_gl.ai.complete_json.return_value = {
            "truth_score": 95,
            "fud_index": 5,
            "verdict": "VERIFIED"
        }

        # Execute Contract Method
        claim_id = "claim_001"
        url = "https://example.com/news/1"
        claim_text = "Partnership announced"

        result = self.contract.verify_content(claim_id, url, claim_text)

        # Assertions
        self.assertEqual(result["truth_score"], 95)
        self.assertEqual(result["fud_index"], 5)
        self.assertEqual(result["verdict"], "VERIFIED")
        
        # Verify State Persistence
        stored_record = self.contract.get_verification(claim_id)
        self.assertEqual(stored_record["claim_id"], claim_id)

    def test_get_non_existing_claim(self):
        result = self.contract.get_verification("invalid_id")
        self.assertEqual(result, {})

if __name__ == '__main__':
    unittest.main()
