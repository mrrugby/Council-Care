
# CouncilCare - IT Repair Request Management System

CouncilCare is a Django-based web application designed to streamline IT repair request processes within organizations. The system aims to enhance transparency, improve communication, and replace traditional paper-based processes with a digital, user-friendly solution.

---

## 🚀 Features

## **User Roles**

1. **Regular Users**  
   - Register and log in securely.
   - Submit IT repair requests with detailed descriptions and attachments.
   - View the status of their submitted requests.

2. **IT Technicians**  
   - View all pending repair requests.
   - Accept or claim requests for resolution.
   - Update request statuses (e.g., "In Progress," "Resolved").

3. **Administrators**  
   - Manage users (add, edit, deactivate accounts).
   - Assign repair requests to technicians.
   - Monitor system activity and generate reports.
   - Oversee and ensure smooth functionality of the system.

---

### **Core Features**

- **Request Submission Form**  
  Users can describe their IT issues, select a category (e.g., hardware, software), and upload images of damaged equipment.

- **Role-Specific Dashboards**  
  - Each user type has a customized dashboard:
  - Users: Track submitted requests and view their statuses.
  - Technicians: Manage claimed requests and update progress.
  - Admins: Oversee the entire system's activities, assign tasks, and generate reports.

- **File Uploads**  
  Users can upload images or documents related to their repair requests.

- **Responsive Design**  
  The system is accessible on both desktop and mobile devices for seamless use.

---

## 🛠️ Tech Stack

- **Backend:** Django Framework
- **Frontend:** Django Templates, HTML5, CSS3, JavaScript, Bootstrap
- **Database:** SQLite (development) / PostgreSQL (production)
- **Authentication & Authorization:** Django's built-in system with role-based access control
- **Version Control:** Git and GitHub

---

## ⚙️ Installation Guide

1. **Clone the Repository**  

   ```bash
   git clone https://github.com/mrrugby/councilcare.git
   cd councilcare
   ```

2. **Set Up Virtual Environment**  

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**  
   Create a `.env` file in the project root with the following:

   ```text
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   EMAIL_HOST=your_email_host
   EMAIL_PORT=your_email_port
   EMAIL_HOST_USER=your_email@example.com
   EMAIL_HOST_PASSWORD=your_email_password
   ```

5. **Apply Migrations**  

   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**  

   ```bash
   python manage.py runserver
   ```

7. **Access the Application**  
   Open your browser and go to `http://127.0.0.1:8000`.

---

## 🧩 App Structure

The project is organized into two main apps:  

1. **app** - Core functionality of the system
2. **councilcare** - project settings.py

Each app follows the Django MVC (Model-View-Controller) architecture.

---

## ✨ Contribution Guidelines

I'd like contributions! Please follow these steps:

1. Fork the repository and clone it locally.
2. Create a new feature branch:

   ```bash
   git checkout -b feature-name
   ```

3. Commit your changes and push them to your fork.
4. Create a pull request for review.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 👥 Authors & Acknowledgements

- **Primary Developer:** Shaka ([GitHub: mrrugby](https://github.com/mrrugby))
- **Special Thanks:** Nairobi Municipal Council ICT Department for the inspiration.

---

## 📞 Contact

For questions, suggestions, or feedback, reach out via:  

- **Email:** <snjishaka@gmail.com>
- **GitHub Issues:** [CouncilCare Issues](https://github.com/mrrugby/councilcare/issues)

---
