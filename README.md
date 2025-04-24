# WhatsApp Messaging via FastAPI

## Overview

This FastAPI application provides a robust API interface for sending messages via Meta's WhatsApp Business Manager API. It allows you to easily integrate WhatsApp messaging capabilities into your applications.

## Features

- Send text messages via WhatsApp
- Easy-to-use REST API endpoints
- Environment-based configuration
- Secure token handling
- Built with FastAPI for high performance

## Requirements

- Python 3.8+
- A WhatsApp Business Account with Meta
- Meta WhatsApp Business API credentials:
  - `WHATSAPP_ACCESS_TOKEN`
  - `WHATSAPP_PHONE_NUMBER_ID`

## Setup

1. Clone the repository:
```bash
git clone https://github.com/Vignesh-1101/whatsapp_fastapi_.git
cd whatsapp_fastapi_
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
   - Copy `.env_sample` to `.env`
   - Update the following variables in `.env`:
     - `WHATSAPP_ACCESS_TOKEN`: Your WhatsApp Business API access token
     - `WHATSAPP_PHONE_NUMBER_ID`: Your WhatsApp Business phone number ID

## Running the Application

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Send Message
- **Endpoint**: `/api/send_message`
- **Method**: POST
- **Request Body**:
```json
{
    "phone_number": "recipient_phone_number",
    "message": "Your message content"
}
```
- **Response**: Success/failure status with message details

## API Documentation

Once the server is running, you can access:
- Interactive API documentation: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

## Dependencies

Key dependencies include:
- FastAPI (0.115.12)
- Uvicorn (0.34.2)
- Python-dotenv (1.1.0)
- Requests (2.32.3)
- Pydantic (2.11.3)

## Error Handling

The API includes comprehensive error handling for:
- Invalid phone numbers
- Missing or invalid credentials
- WhatsApp API communication errors
- Rate limiting issues

## Security Considerations

- Never commit your `.env` file to version control
- Keep your WhatsApp access token secure
- Use HTTPS in production
- Implement rate limiting for production use

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open-source and available under the MIT License.
