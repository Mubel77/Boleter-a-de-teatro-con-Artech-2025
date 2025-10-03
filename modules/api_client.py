# modules/api_client.py
import requests
from .config import N8N_URL, API_KEY

def enviar_a_n8n(query: str, timeout: int = 10):
    headers = {}
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"
    try:
        resp = requests.post(N8N_URL, json={"query": query}, headers=headers, timeout=timeout)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}