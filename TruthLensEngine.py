from genlayer import *

@gl_contract
class TruthLensEngine:
    truth_records: Dict[str, dict]

    def __init__(self):
        self.truth_records = {}

    @gl_public
    def verify_content(self, claim_id: str, content_url: str, claim_text: str) -> dict:
        """
        Fetches web content from URL, analyzes sentiment and factual truth using AI consensus.
        """
        # Step 1: Fetch content from web via GenLayer Non-Deterministic Execution
        web_data = gl.web.get(content_url)
        
        # Step 2: Prompt AI models across execution nodes to evaluate FUD/Truth score
        prompt = f"""
        Analyze the following web content against the claim: '{claim_text}'.
        Web Content: {web_data.text[:1000]}
        
        Return a JSON with:
        1. "truth_score": int between 0 and 100 (100 being completely factual).
        2. "fud_index": int between 0 and 100 (100 being pure FUD/misinformation).
        3. "verdict": string ("VERIFIED", "UNVERIFIED", "FUD").
        """
        
        analysis_result = gl.ai.complete_json(prompt)
        
        # Step 3: Record consensus result state
        record = {
            "claim_id": claim_id,
            "url": content_url,
            "truth_score": analysis_result["truth_score"],
            "fud_index": analysis_result["fud_index"],
            "verdict": analysis_result["verdict"],
            "timestamp": gl.block.timestamp
        }
        
        self.truth_records[claim_id] = record
        return record

    @gl_public_view
    def get_verification(self, claim_id: str) -> dict:
        return self.truth_records.get(claim_id, {})
