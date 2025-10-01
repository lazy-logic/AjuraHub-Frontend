# TalentConnect Africa Platform

A digital platform designed to connect trainees from various institutions across Africa with potential employers. Built with NiceGUI and Tailwind CSS, ready for FastAPI integration.

## 🌍 Overview

TalentConnect Africa provides a centralized space where:
- **Trainees** can showcase their skills, portfolios, and certifications
- **Employers** can search, filter, and connect with qualified candidates
- **Institutions** can track trainee employment progress and manage visibility
- **Admins** can manage the platform and generate insights

## ✨ Features

### For Trainees
- Create and manage professional profiles
- Upload portfolio projects and CVs
- Showcase skills and certifications
- Receive interview requests from employers
- Track job applications

### For Employers
- Search and filter talent by skills, location, and experience
- Post job opportunities
- View detailed trainee profiles
- Send interview invitations
- Manage applications

### For Institutions
- Onboard and verify trainees
- Track employment progress
- Manage institution-specific data
- Generate reports on trainee success

### For Admins
- Manage all users and roles
- Moderate platform activity
- Generate comprehensive reports
- Ensure platform compliance

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory:**
```bash
cd "TalentKonnect Project Designs and Code"
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
python main.py
```

4. **Open your browser:**
The application will automatically open at `http://localhost:8080`

## 📁 Project Structure

```
TalentConnect Africa/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── app/
    ├── __init__.py        # App package initialization
    ├── state.py           # Global state management
    ├── data.py            # Sample data (temporary)
    ├── shared/            # Shared components
    │   ├── __init__.py
    │   ├── header.py      # Navigation header
    │   └── footer.py      # Footer component
    └── pages/             # Page modules
        ├── __init__.py
        ├── home.py        # Landing page
        ├── auth.py        # Login/signup pages
        ├── search.py      # Talent search
        ├── jobs.py        # Job listings
        └── dashboard.py   # Role-specific dashboards
```

## 🎨 Technology Stack

- **Frontend Framework:** NiceGUI (Python-based UI framework)
- **Styling:** Tailwind CSS (utility-first CSS)
- **Backend (Ready for):** FastAPI
- **Future:** Database integration (PostgreSQL/MongoDB)

## 🔐 User Roles

1. **Trainee** - Students and graduates looking for opportunities
2. **Employer** - Companies searching for talent
3. **Institution** - Educational institutions managing trainees
4. **Admin** - Platform administrators

## 📝 Current Status

**Phase 1: Frontend & UI (Current)**
- ✅ Modular application structure
- ✅ Responsive design with Tailwind CSS
- ✅ Role-based navigation
- ✅ Landing page with features
- ✅ Authentication pages (UI only)
- ✅ Talent search interface
- ✅ Job listings page
- ✅ Role-specific dashboards
- ✅ Shared components (header, footer)

**Phase 2: Backend Integration (Next)**
- ⏳ FastAPI backend setup
- ⏳ Database models and migrations
- ⏳ Authentication & authorization
- ⏳ RESTful API endpoints
- ⏳ File upload functionality

**Phase 3: Advanced Features (Future)**
- ⏳ Real-time messaging
- ⏳ Interview scheduling
- ⏳ Advanced search filters
- ⏳ Analytics and reporting
- ⏳ Email notifications

## 👥 Team Members

1. Kelem Bampoe-Addo
2. Michael Abraham
3. George Asiedu
4. Jemima Asare
5. Prince Amankwah

## 🤝 Contributing

This is a team project. To contribute:
1. Create a new branch for your feature
2. Make your changes
3. Test thoroughly
4. Submit for review

## 📄 License

This project is part of an institutional training program.

## 📞 Support

For questions or issues, please contact the development team.

---

**Made with ❤️ in Africa**
