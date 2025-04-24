from fastapi import FastAPI, Query, HTTPException
from .utils import validate_phone_number, send_whatsapp_message

app = FastAPI()

@app.get("/send_message")
def send_message(phone_number: str = Query(..., description="WhatsApp phone number in E.164 format (e.g., +12345678901)")):
    """
    This function sends a WhatsApp message to a phone number in E.164 format after validating the phone
    number.
    """
    if not validate_phone_number(phone_number):
        raise HTTPException(status_code=400, detail="Invalid phone number format. Use E.164 format.")

    result = send_whatsapp_message(phone_number)
    if result["success"]:
        return {"message": "Message sent successfully!", "response": result["response"]}
    else:
        raise HTTPException(status_code=500, detail=result["error"])
