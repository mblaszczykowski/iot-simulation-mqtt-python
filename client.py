import requests

BASE_URL = "http://localhost:8000"

def print_response(response):
    print(f"Status Code: {response.status_code}")
    print("Response Body:", response.json())
    print("-" * 50)

# 1. Get all items
response = requests.get(f"{BASE_URL}/items")
print("GET /items")
print_response(response)

# 2. Add a new item
new_item = {
    "id": 1,
    "name": "Sensor A",
    "value": 23.5
}
response = requests.post(f"{BASE_URL}/items", json=new_item)
print("POST /items")
print_response(response)

# 3. Get item by ID
response = requests.get(f"{BASE_URL}/items/1")
print("GET /items/1")
print_response(response)

# 4. Update the item
updated_item = {
    "id": 1,
    "name": "Sensor A+",
    "value": 25.0
}
response = requests.put(f"{BASE_URL}/items/1", json=updated_item)
print("PUT /items/1")
print_response(response)

# 5. Get items with value greater than 24
response = requests.get(f"{BASE_URL}/items/value/24")
print("GET /items/value/24")
print_response(response)
