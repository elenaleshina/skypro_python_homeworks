import requests

json = {
  "username": "bloom",
  "password": "fire-fairy"
}
response = requests.post("https://x-clients-be.onrender.com/auth/login", json=json)
print(response.json())

company = {
  "name": "SkyPro",
  "description": "курсы"
}
my_headers = {}
my_headers["x-client-token"] = response.json()["userToken"]
response2 = requests.post("https://x-clients-be.onrender.com/company", json=company, headers=my_headers)
print(response2.json())

employee = {
  "id": 0,
  "firstName": "Петр",
  "lastName": "Иванов",
  "middleName": "string",
  "companyId": response2.json()["id"],
  "email": "dljasky2@gmail.com",
  "url": "string",
  "phone": "+79171089932",
  "birthdate": "1983-07-16T11:58:27.215Z",
  "isActive": True
}
my_headers = {}
my_headers["x-client-token"] = response.json()["userToken"]
response3 = requests.post("https://x-clients-be.onrender.com/employee", json=employee, headers=my_headers)
print(response3.json())

