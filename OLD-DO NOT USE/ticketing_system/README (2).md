### **📌 Django REST API Documentation**

# **Wcjc IT Tech Capstone - Django REST API**
> **An IT Ticket Dashboard REST API built with Django and Django REST Framework (DRF)**

## **📖 Overview**
This Django REST API powers the **Wcjc IT Tech Capstone** project. It provides a structured and secure way to handle IT support tickets, user authentication, and ticket status updates. Built using **Django REST Framework (DRF)**, it follows RESTful best practices.

## **📦 Features**
✔ **CRUD Operations** - Create, Read, Update, and Delete IT tickets  
✔ **Authentication & Permissions** - Secure API using JWT authentication  
✔ **Pagination & Filtering** - Efficient data retrieval for tickets  
✔ **Django Admin Integration** - Manage API data via the Django admin panel  
✔ **Token-Based Authentication** - Secure access to protected endpoints  

---

## **⚙️ Installation & Setup**
To run this API locally, follow these steps:

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/WiseTechLTS/Wcjc_IT_Tech_Capstone.git
cd Wcjc_IT_Tech_Capstone
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run Database Migrations**
```sh
python manage.py migrate
```

### **5️⃣ Create a Superuser (For Admin Panel)**
```sh
python manage.py createsuperuser
```

### **6️⃣ Start the Django Server**
```sh
python manage.py runserver
```
Your API will now be accessible at **http://127.0.0.1:8000/api/**

---

## **🔗 API Endpoints**
| **Method** | **Endpoint**          | **Description**                            | **Authentication** |
|-----------|----------------------|--------------------------------|-----------------|
| `GET`     | `/api/tickets/`        | Retrieve all IT tickets           | ✅ Required |
| `POST`    | `/api/tickets/`        | Create a new IT ticket           | ✅ Required |
| `GET`     | `/api/tickets/{id}/`   | Retrieve a single ticket by ID   | ✅ Required |
| `PUT`     | `/api/tickets/{id}/`   | Update a ticket                  | ✅ Required |
| `DELETE`  | `/api/tickets/{id}/`   | Delete a ticket                   | ✅ Required |
| `POST`    | `/api/auth/login/`     | Authenticate user & get JWT token | ❌ Open |
| `POST`    | `/api/auth/register/`  | Create a new user                 | ❌ Open |

---

## **🔐 Authentication & Security**
This API uses **JWT Authentication** for securing endpoints.

### **🔑 Obtain a Token**
Send a `POST` request to `/api/auth/login/` with the following:
```json
{
  "username": "your_username",
  "password": "your_password"
}
```
Response:
```json
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```

### **🔒 Use Token in Requests**
Include the token in your request headers:
```sh
Authorization: Bearer your_access_token
```

### **🔄 Refresh Token**
To get a new access token, send a `POST` request to `/api/auth/token/refresh/`:
```json
{
  "refresh": "your_refresh_token"
}
```
Response:
```json
{
  "access": "new_access_token"
}
```

---

## **📊 Filtering & Pagination**
### **Filter Tickets by Status**
```sh
GET /api/tickets/?status=open
```

### **Paginate Ticket Results**
The API returns paginated results by default:
```sh
GET /api/tickets/?page=2
```

---

## **🛠️ Development & Contribution**
Want to contribute? Follow these steps:

1. **Fork the repository**  
2. **Create a feature branch** (`git checkout -b feature-name`)  
3. **Commit your changes** (`git commit -m "Add feature"`)  
4. **Push to your branch** (`git push origin feature-name`)  
5. **Create a pull request** 🎉  

---

## **📜 License**
This project is licensed under the **MIT License**.

---

## **📧 Contact**
📌 **Author:** WiseTechLTS  
📌 **GitHub:** [WiseTechLTS](https://github.com/WiseTechLTS)  
📌 **Email:** wisetechlts@example.com  

---

### 🚀 **Happy Coding!**
