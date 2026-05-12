# Cafe & Wifi API ☕📡

A RESTful Cafe API built using Flask and SQLAlchemy that allows users to search, add, update, and delete cafe data. This project focuses on API development, database integration, and HTTP request handling using Flask.

---

## 🚀 Features

- Get a random cafe
- Retrieve all cafes
- Search cafes by location
- Add a new cafe
- Update cafe coffee price
- Delete cafe using API key authentication
- JSON responses using Flask `jsonify`
- SQLite database integration using SQLAlchemy

---

## 🛠 Technologies Used

- Python
- Flask
- Flask SQLAlchemy
- SQLite
- REST API
- Postman
- JSON
- HTTP Methods (GET, POST, DELETE)

---

# 📂 Project Structure

```text
Cafe-Wifi-API/
│
├── main.py
├── cafes.db
├── templates/
│   └── index.html
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the repository

```bash
git clone <your-repository-url>
```

---

## 2️⃣ Navigate to project folder

```bash
cd Cafe-Wifi-API
```

---

## 3️⃣ Install dependencies

```bash
pip install flask flask_sqlalchemy
```

---

## 4️⃣ Run the application

```bash
python main.py
```

---

# 🌐 Base URL

```text
http://127.0.0.1:5000
```

---

# 📌 API Endpoints

## 🎲 Get Random Cafe

### Endpoint

```http
GET /random
```

### Example

```text
http://127.0.0.1:5000/random
```

---

## 📋 Get All Cafes

### Endpoint

```http
GET /all
```

### Example

```text
http://127.0.0.1:5000/all
```

---

## 🔍 Search Cafe by Location

### Endpoint

```http
GET /search?loc=London
```

### Example

```text
http://127.0.0.1:5000/search?loc=London
```

---

## ➕ Add New Cafe

### Endpoint

```http
POST /add
```

### Parameters

| Parameter | Type |
|---|---|
| id | Integer |
| name | String |
| map_url | String |
| img_url | String |
| location | String |
| seats | String |
| has_toilet | Boolean |
| has_wifi | Boolean |
| has_sockets | Boolean |
| can_take_calls | Boolean |
| coffee_price | String |

### Example

```text
http://127.0.0.1:5000/add?id=21&name=Aurora%20Beans&map_url=https://goo.gl/maps/example&img_url=https://images.unsplash.com/photo-example&location=London&seats=20-30&has_toilet=True&has_wifi=True&has_sockets=True&can_take_calls=True&coffee_price=£3.50
```

---

## ✏️ Update Coffee Price

### Endpoint

```http
GET /update/<id>?coffee_price=£4.20
```

### Example

```text
http://127.0.0.1:5000/update/5?coffee_price=£4.20
```

---

## ❌ Delete Cafe

### Endpoint

```http
DELETE /delete/<id>?api_key=yourapikey
```

### Example

```text
http://127.0.0.1:5000/delete/5?api_key=thisismysecretkey
```

---

# 🔐 API Authentication

The delete endpoint requires an API key for security.

Example:

```text
api_key=thisismysecretkey
```

---

# 🔐 API Documentation

The API Documentation is given below.

```text
https://documenter.getpostman.com/view/54681293/2sBXqQEHXn
```

---

# 🧠 What I Learned

- Building REST APIs with Flask
- Connecting Flask with SQLite databases
- Using SQLAlchemy ORM
- Handling HTTP methods
- Working with query parameters
- Returning JSON responses
- API testing using Postman
- CRUD operations
- Error handling in Flask

---

# 📮 Testing the API

You can test all endpoints using:

- Postman
- Thunder Client
- Browser (GET requests)

---

# 📷 Example JSON Response

```json
{
  "id": 8,
  "name": "Goswell Road Coffee",
  "map_url": "https://goo.gl/maps/example",
  "img_url": "https://images.unsplash.com/example",
  "location": "London",
  "seats": "10-20",
  "has_toilet": true,
  "has_wifi": true,
  "has_sockets": true,
  "can_take_calls": false,
  "coffee_price": "£2.10"
}
```

---

# 👨‍💻 Author

Ibunu Suhudhu