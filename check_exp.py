import time
import requests
import json
from print_event import eventCalendar
from access_the_token import load_tokens
from credentials import load_credentials

token_url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
url = "https://graph.microsoft.com/v1.0/me/events"  # Define the API URL

# Load tokens
access_token, refresh_token = load_tokens()

# Check access token can be access or not
headers = {"Authorization": f"Bearer {access_token}"}

def save_tokens(token_data, filename="tokens.json"):
    with open(filename, "w") as file:
        json.dump(token_data, file, indent=4)
    print("✅ Tokens saved to", filename)

def check_access_token():
    global access_token

    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    data = response.json()

    if "error" in data:
        error_code = data["error"]["code"]
        error_message = data["error"]["message"]
        
        print(f"❌ API Error: {error_code} - {error_message}")
    
        if error_code == "InvalidAuthenticationToken":
            print("🔄 Attempting to refresh the token...")
            refresh_access_token()  # Call your refresh function
        else:
            print("⚠️ Unhandled error. Please check the response.")
    else:
        print("✅ Token is valid! Running eventCalendar()...")
        eventCalendar()  # Call function from print_event.py

def refresh_access_token():
    global access_token, refresh_token  # Update global tokens

    client_id, client_secret, tenant_link, redirect_uri, code = load_credentials()
    
    refresh_payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token, 
        "grant_type": "refresh_token"
    }

    response = requests.post(token_url, data=refresh_payload)
    new_token_data = response.json()

    if "access_token" in new_token_data:
        access_token = new_token_data["access_token"]
        
        # ⚠️ Always update refresh_token if a new one is returned!
        refresh_token = new_token_data.get("refresh_token", refresh_token)
        
        print("✅ Successful get new Access Token")
        print("🔄 Updated Refresh Token")

        # Save new tokens
        save_tokens({"access_token": access_token, "refresh_token": refresh_token})
        print("✅ Token is renew! Running eventCalendar()...")
        eventCalendar()  # Call function from print_event.py
    else:
        print("❌ Error refreshing token:")

# ✅ Run the token check
check_access_token()