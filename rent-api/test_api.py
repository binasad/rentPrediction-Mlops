import requests

# 1. The Address
url = 'http://127.0.0.1:5000/predict'

# 2. The Data (The "Order")
# Note: For this first test, we are sending the CLEAN numbers directly
# (Area: 20.0 represents 1 Kanal)
data = {
    "Location": "F-6, Islamabad",
    "Area": 20.0, 
    "Beds": 4
}

# 3. Send the POST Request
try:
    response = requests.post(url, json=data)
    print("--------------------------------")
    print(f"Status Code: {response.status_code}")
    print(f"Server Says: {response.json()}")
    print("--------------------------------")
except Exception as e:
    print(f"Connection Failed: {e}")