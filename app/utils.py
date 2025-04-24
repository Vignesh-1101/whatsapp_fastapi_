import re
import requests
from .config import ACCESS_TOKEN, API_URL

def validate_phone_number(phone_number: str) -> bool:
    # Basic E.164 format check
    return bool(re.fullmatch(r'\+\d{10,15}', phone_number))

def send_whatsapp_message(phone_number: str) -> dict:
    """
    The function `send_whatsapp_message` sends a WhatsApp message using a specified phone number and
    returns the response.
    it returns a dictionary with key "success" set to False and the error response in
    """
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "template",
        "template": {"name": "tmbc_test", "language": {"code": "en_US"}}
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    if response.ok:
        return {"success": True, "response": response.json()}
    else:
        return {"success": False, "error": response.json()}
