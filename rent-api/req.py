import requests

response = requests.post(
    'http://localhost:5000/predict',
    json={
        "Location": "F-6, Islamabad",
        "Area": 20.0,  # 1 Kanal = 20 Marla
        "Beds": 4
    }
)
print(response.json())