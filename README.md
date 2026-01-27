🏥 Health+ — Hospital Appointment Booking System

  A modern Hospital Appointment Booking Web Application built with Django, allowing patients to book appointments with doctors across multiple departments through a clean and responsive interface.

✨ Features =>

  🧑‍⚕️ Department-wise doctor selection
  
  📅 Appointment booking with date picker
  
  📝 Patient details collection
  
  🎨 Clean UI using Bootstrap & Tailwind utility classes

📋 Django Admin panel for managing:

  Departments
  
  Doctors
  
  Appointments

✅ Form validation using Django Crispy Forms

🔔 Success message after booking

📱 Responsive design

🛠 Tech Stack
  Technology	Usage
  Python	Backend language
  Django	Web framework
  SQLite	Database (default)
  Bootstrap 5	UI styling
  Tailwind (utility classes)	Custom layout
  Crispy Forms	Beautiful Django forms
  HTML5 / CSS3	Templates
📂 Project Structure
  Project/
  │
  ├── djenv/                     # Virtual environment (not tracked in git)
  │
  ├── Project/                   # Django project root
  │   │
  │   ├── home/                  # Main application
  │   │   ├── migrations/
  │   │   │   └── __init__.py
  │   │   ├── __pycache__/
  │   │   ├── admin.py           # Admin configuration
  │   │   ├── apps.py
  │   │   ├── forms.py           # Booking forms
  │   │   ├── models.py          # Departments, Doctors, Booking models
  │   │   ├── tests.py
  │   │   ├── urls.py            # App-level URLs
  │   │   └── views.py           # Application views
  │   │
  │   ├── Project/               # Django configuration folder
  │   │   ├── __pycache__/
  │   │   ├── __init__.py
  │   │   ├── asgi.py
  │   │   ├── settings.py        # Project settings
  │   │   ├── urls.py            # Main URL configuration
  │   │   └── wsgi.py
  │   │
  │   ├── static/                # Static files
  │   │   ├── css/
  │   │   ├── images/
  │   │   └── js/
  │   │
  │   ├── templates/             # HTML templates
  │   │   ├── base.html
  │   │   ├── index.html
  │   │   ├── about.html
  │   │   ├── booking.html
  │   │   ├── confirmation.html
  │   │   ├── contact.html
  │   │   ├── department.html
  │   │   └── doctors.html
  │   │
  │   ├── uploads/               # Media uploads
  │   │   └── doctors/           # Doctor profile images
  │   │
  │   ├── db.sqlite3             # SQLite database
  │   ├── manage.py              # Django management script
  │   └── requirements.txt       # Project dependencies
  │
  └── README.md                  # Project documentation


⚙️ Installation & Setup
  1️⃣ Clone the Repository
  git clone 
  cd health-appointment-system
  
  2️⃣ Create Virtual Environment
  python -m venv venv
  venv\Scripts\activate   # Windows
  # source venv/bin/activate  # macOS/Linux
  
  3️⃣ Install Dependencies
  pip install django django-crispy-forms crispy-bootstrap5
  
  4️⃣ Configure settings.py
  INSTALLED_APPS = [
      ...
      'crispy_forms',
      'crispy_bootstrap5',
      'home',
  ]
  
  CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
  CRISPY_TEMPLATE_PACK = "bootstrap5"
  
  5️⃣ Run Migrations
  python manage.py makemigrations
  python manage.py migrate
  
  6️⃣ Create Superuser
  python manage.py createsuperuser
  
  7️⃣ Start Server
  python manage.py runserver


Open:

  http://127.0.0.1:8000/

📅 Appointment Booking Flow

  User opens Booking page
  
  Enters patient details
  
  Selects department & doctor
  
  Chooses booking date
  
  Submits form
  
  Success message is displayed
  
  Appointment saved in database

🔐 Admin Panel

Access:

  http://127.0.0.1:8000/admin/


Admin can:

  Add Departments
  
  Add Doctors
  
  View all Appointments
  
  Manage bookings easily

📸 Screenshots

<img width="1898" height="968" alt="image" src="https://github.com/user-attachments/assets/f44cd89a-aac6-4de6-af17-d9aa95cd4a7d" />
<img width="1897" height="969" alt="image" src="https://github.com/user-attachments/assets/6817a7e7-373d-4536-838b-5355b122031b" />
<img width="1902" height="968" alt="image" src="https://github.com/user-attachments/assets/6bdedf8e-bd7f-4eb8-9470-30b1e7a54f46" />




🚀 Future Enhancements  =>

  🔄 Filter doctors based on department (AJAX)
  
  📧 Email confirmation for appointments
  
  ⏰ Time-slot booking
  
  👤 User authentication (patient login)
  
  📊 Dashboard analytics

🤝 Contributing

  Contributions are welcome!
  Feel free to fork the repository and submit a pull request.

📜 License

  This project is for learning and educational purposes.

👨‍💻 Author

  Mohammed Swalih N K
  Frontend & Django Developer
  🌐 Portfolio: https://nkswalih-portfolio.vercel.app/
  📫 GitHub: https://github.com/nkswalih
