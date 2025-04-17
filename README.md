# 🏨 python-mmrsh-back — Backend for Phymmr.com

**python-mmrsh-back** is the backend server for [Phymmr.com](https://phymmr.com), a **real-time accommodation management platform** that helps hosts and guests coordinate bookings, availability, and property data in a fast and scalable way.

This backend is implemented using **Python Django**, providing secure APIs and real-time updates for frontend integrations and third-party services.

---

## 🚀 Key Features

- 🧾 **Real-time booking management** for rooms and accommodations
- 🔐 **Authentication & access control** (host, guest, admin roles)
- 📅 **Calendar-based availability tracking**
- 📡 **RESTful API** for seamless frontend communication
- 🌐 **Scalable Django architecture** for future expansion

---

## 🛠 Tech Stack

| Layer              | Tech                         |
|-------------------|------------------------------|
| Backend Framework | Django 4.x                   |
| API Style         | Django REST Framework (DRF)  |
| Real-Time Logic   | Custom logic & signals       |
| DB Engine         | PostgreSQL / SQLite (local)  |
| Auth              | Django Auth + Token-based    |
| Deployment        | Docker / AWS / Gunicorn (optional) |

---

## 📁 Project Structure

```bash
python-mmrsh-back/
├── phymmr/                  # Main Django app for bookings & logic
├── mmrsh_backend/          # Django settings and URL configs
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🔐 Environment Setup

Create a `.env` file (or set up securely with `python-decouple` / `python-dotenv` if used):

```env
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1,phymmr.com

# Database config (example)
DATABASE_URL=sqlite:///db.sqlite3
```

---

## 💻 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/saebyeokchu/python-mmrsh-back.git
cd python-mmrsh-back
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

---

## 🔗 API Overview (Sample)

| Method | Endpoint               | Description                      |
|--------|------------------------|----------------------------------|
| GET    | `/api/rooms/`          | List all available rooms         |
| POST   | `/api/book/`           | Create a new booking             |
| GET    | `/api/calendar/`       | Retrieve room availability       |
| POST   | `/api/login/`          | Authenticate user                |

> Full API documentation coming soon (e.g., Swagger or ReDoc)

---

## 📌 Core Modules

- **Booking system**: Reserve, cancel, and track stays
- **Availability engine**: Syncs room calendars in real-time
- **User roles**: Host vs Guest access level logic
- **Admin panel**: Django admin with custom model views (optional)

---

## 🧩 Future Plans

- [ ] Real-time sync with external booking platforms (e.g., Airbnb, Booking.com)
- [ ] Payment gateway integration
- [ ] Host dashboard with analytics
- [ ] Notification system (email/SMS)

---

## 🙌 Contributing

Whether you're a Django enthusiast, real-time systems developer, or just curious — contributions are welcome! Feel free to fork, issue, or PR.

---

## 📄 License

MIT License

---

Made with 🛏️ and Django by [@saebyeokchu](https://github.com/saebyeokchu)  
Powering [Phymmr.com](https://phymmr.com) — Smart & Simple Room Management System.
