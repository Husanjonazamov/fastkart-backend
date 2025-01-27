import requests

url = "http://127.0.0.1:8085/accounts/auth/token/"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM3OTY2MDgyLCJpYXQiOjE3Mzc5NjI0ODIsImp0aSI6IjNiYzM4ZDFkNDA4MjRlYzJhYWRhMjczNDg0NjMxMDNkIiwidXNlcl9pZCI6MX0.VHsWeATb5BiO56xX26dbEwhJMfgMdhf1_oIIgEhSuhM"
}

response = requests.get(url, headers=headers)
print(response.json())
