import os
import google.generativeai as genai
from typing import Dict, Any
import json

def generate_summary(analytics_results: Dict[str, Any]) -> str:
    """
    Calls Google Gemini API to generate a professional executive summary.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is missing.")

    genai.configure(api_key=api_key)
    
    # Choose a robust model for text generation
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"""
Generate a professional, concise executive summary for leadership from the following sales analytics data.
Provide a short business narrative highlighting key performing areas, potential issues (like cancelled orders), 
and actionable insights. Keep it under 3 paragraphs. Do not use markdown headers, just plain text paragraphs.

Data:
{json.dumps(analytics_results, indent=2)}
"""

    response = model.generate_content(prompt)
    
    # Extract text and provide a generic fallback if needed
    if response and response.text:
       return response.text.strip()
    return "AI Summary could not be generated at this time. Please review the raw metrics instead."
