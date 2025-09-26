import requests

# Step 1: Get your public IP
public_ip = requests.get("https://api.ipify.org").text
print("Public IP:", public_ip)

# Step 2: Get location info using ip-api
url = f"http://ip-api.com/json/{public_ip}"
response = requests.get(url).json()

# Step 3: Print location details
if response["status"] == "success":
    print(f"Country: {response['country']}")
    print(f"Region: {response['regionName']}")
    print(f"City: {response['city']}")
    print(f"Latitude: {response['lat']}, Longitude: {response['lon']}")
    print(f"ISP: {response['isp']}")
else:
    print("Error:", response)
