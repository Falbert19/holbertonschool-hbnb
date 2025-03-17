# HBnB Project
The HBnB project is a comprehensive web application that emulates the core functionalities of Airbnb. It integrates various components, including a command-line interpreter, data storage through both file and database systems, a web framework with dynamic content, and a RESTful API.

# 📌 Table of Contents

📁 Project Structure

⚙️ Installation

🚀 Running the API

🛠 API Endpoints

🔍 Testing the API

🤝 Contributors

📜 License


Create and manage Users

Register and update Places

Add and retrieve Amenities

Use a structured API with Blueprints and Namespaces

# 📁 Project Structure
```
holbertonschool-hbnb/
├── README.md
├── requirements.txt
├── config.py
├── run.py
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── amenities.py
│   │       ├── auth.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       └── users.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── amenity.py
│   │   ├── base_model.py
│   │   ├── place.py
│   │   ├── review.py
│   │   └── user.py
│   ├── persistence/
│   │   ├── __init__.py
│   │   ├── repository.py
│   │   └── user_repository.py
│   └── services/
│       ├── __init__.py
│       └── facade.py
└── instance/
    └── development.db

```
#⚙️ Installation

## 1️⃣ Clone the repository

git clone https://github.com/Falbert19/holbertonschool-hbnb.git
cd holbertonschool-hbnb

## 2️⃣ Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
### OR

venv\Scripts\activate  # On Windows

## 3️⃣ Install dependencies

pip install -r requirements.txt

## 4 Set up the database

Ensure MySQL is installed and running

# 🚀 Running the API

1️⃣ Set environment variables
export PYTHONPATH=$(pwd)/hbnb
export FLASK_APP=hbnb.run

## 2️⃣ Run the API

python3 hbnb/run.py
🚀 The API will be available at:
👉 http://127.0.0.1:5000/api/v1/

## 3️⃣ View registered routes
bash
Copiar
Editar
python3 -m flask r

# 🛠 API Endpoints
### Users
Method	Endpoint	Description


### Register a new user


POST	/api/v1/users/

### Register a all users


GET	/api/v1/users/

### Retrieve a user by ID
GET	/api/v1/users/<id>	#Retrieve a user by ID



### Places

POST	/api/v1/places/	Register a new place


GET	/api/v1/places/	Retrieve all places


GET	/api/v1/places/<id>	Retrieve a place by ID


PUT	/api/v1/places/<id>	Update place details

### Amenities
POST	/api/v1/amenities/	Register a new amenity


GET	/api/v1/amenities/	Retrieve all amenities


GET	/api/v1/amenities/<id>	Retrieve an amenity by ID


PUT	/api/v1/amenities/<id>	Update an amenity's details



# 📄 Swagger UI Documentation is available at:
👉 http://127.0.0.1:5000/api/v1/

# 🔍 Testing the API
## 1️⃣ Run unit tests
python3 -m unittest discover test/

## 2️⃣ Manually test with curl
### Create a User
curl -X POST http://127.0.0.1:5000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"}'

### Get All Users
curl -X GET http://127.0.0.1:5000/api/v1/users/

### Get a Specific User
curl -X GET http://127.0.0.1:5000/api/v1/users/<user_id>

# 🤝 Author/creator
Falbert19 (https://github.com/Falbert19) - Lead Developer
