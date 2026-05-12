from flask import Flask
from azampay import AzampayClient
import os

app = Flask(__name__)

# Load credentials kutoka environment variables
client_id = os.getenv("AZAMPAY_CLIENT_ID")
client_secret = os.getenv("AZAMPAY_CLIENT_SECRET")
app_name = os.getenv("AZAMPAY_APP_NAME")
environment = os.getenv("AZAMPAY_ENVIRONMENT", "sandbox")

# Initialize SDK client
azampay = AzampayClient(
    client_id=client_id,
    client_secret=client_secret,
    app_name=app_name,
    environment=environment
)

@app.route("/")
def home():
    return "Azampay SDK running on Render!"

@app.route("/checkout")
def checkout():
    # Mfano wa ku-call SDK method
    response = azampay.create_checkout_session(
        amount=5000,
        currency="TZS",
        redirect_url="https://yourdomain.com/success"
    )
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
