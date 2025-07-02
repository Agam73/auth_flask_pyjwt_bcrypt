# 🔒 Secure Authentication System

A professional and scalable secure login system built with:
- 🐍 Python (Flask)
- 🛡️ JWT authentication & encryption (PyJWT, bcrypt)
- 🐘 PostgreSQL
- 📦 SQLAlchemy

Supports secure user registration, authentication, and session management.

---

## 🚀 Features
✅ Register new users securely (passwords are hashed with bcrypt)  
✅ Login returns a signed JWT token  
✅ Store and verify data in PostgreSQL  
✅ Modular Flask structure, ready for scaling  
✅ Easy to add protected routes (using JWT)

---

## 🛠️ Tech Stack
- **Backend:** Flask, Flask-SQLAlchemy, PyJWT, bcrypt
- **Database:** PostgreSQL
- **Other:** python-dotenv (for environment configs)

---

## 📦 Project Structure
```
.
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── utils.py
│   └── extensions.py
├── manage.py
├── init_db.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repo & create virtual environment
```bash
git clone https://github.com/yourusername/secure-auth-system.git
cd secure-auth-system
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

---

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure environment variables

Create a `.env` file at the root:
```
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/authdb
JWT_SECRET_KEY=your_jwt_secret_key_here
```

Replace with your actual password & secret key.

---

### 4️⃣ Create database & tables
Make sure PostgreSQL is running and database `authdb` is created.
Then run:
```bash
python init_db.py
```

---

### 5️⃣ Run the server
```bash
python manage.py
```

App will run at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 API Endpoints

| Method | Endpoint      | Body (JSON)                                      | Response |
|-------|---------------|--------------------------------------------------|---------|
| POST  | `/register`   | `{ "username": "john", "email": "john@x.com", "password": "pass123" }` | Success / error message |
| POST  | `/login`      | `{ "username": "john", "password": "pass123" }` | `{ "access_token": "<JWT>" }` |

---

## 🛠️ Testing

Use [Postman](https://www.postman.com/) or curl:

```bash
curl -X POST http://127.0.0.1:5000/register \
  -H "Content-Type: application/json" \
  -d '{"username":"john","email":"john@x.com","password":"pass123"}'
```

---

## 📌 Note

✅ Passwords are **never stored in plain text**.  
✅ JWT tokens expire automatically (default: 1 hour).  
✅ You can easily add protected routes using `@jwt_required` logic.

---

## ✨ License
MIT License

Copyright (c) 2025 [Agam Bansal]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 🙏 Thanks
Built as a secure, real-world practice project for learning & demonstration.

