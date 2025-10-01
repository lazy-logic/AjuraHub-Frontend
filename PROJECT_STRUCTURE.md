# TalentConnect Africa - Project Structure

## 📂 Modular Architecture

This project follows a clean, modular architecture for easy maintenance and scalability.

### Directory Structure

```
TalentKonnect Project Designs and Code/
│
├── main.py                      # Application entry point & route registration
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── .gitignore                   # Git ignore rules
├── run.bat                      # Quick start script (Windows)
│
└── app/                         # Main application package
    │
    ├── __init__.py              # Package initialization
    ├── state.py                 # Global state management
    ├── data.py                  # Sample data (temporary, will be replaced with DB)
    │
    ├── shared/                  # Shared/reusable components
    │   ├── __init__.py
    │   ├── header.py            # Navigation header component
    │   └── footer.py            # Footer component
    │
    └── pages/                   # Page modules organized by user roles
        ├── __init__.py
        │
        ├── shared/              # Pages used by multiple user types
        │   ├── __init__.py
        │   ├── home.py          # Landing page
        │   ├── auth.py          # Authentication (login/signup)
        │   ├── about.py         # About platform
        │   ├── how_it_works.py  # Platform workflow guide
        │   ├── help_and_support.py  # Support and FAQ
        │   ├── search.py        # Job/talent search interface
        │   ├── jobs.py          # Job listings
        │   └── messaging.py     # Communication system
        │
        ├── candidates/          # Candidate/Trainee specific pages
        │   ├── __init__.py
        │   ├── dashboard.py     # Trainee dashboard
        │   ├── trainee_profile.py   # Profile management
        │   └── application_tracking.py  # Track applications
        │
        ├── employers/           # Employer specific pages
        │   ├── __init__.py
        │   ├── employer_dashboard.py    # Employer overview
        │   └── job_posting.py   # Create job postings
        │
        ├── institutions/        # Institution specific pages
        │   ├── __init__.py
        │   ├── institution_dashboard.py        # Institution overview
        │   └── institution_program_listing.py  # Manage programs
        │
        └── admin/              # Admin & Management pages
            ├── __init__.py
            ├── admin_management.py     # System administration
            └── notification_management.py  # Notification settings
```

## 🔧 Module Descriptions

### Core Files

#### `main.py`
- Application entry point
- Route registration for all pages
- NiceGUI configuration
- Runs on port 8080 by default

#### `app/state.py`
- Global application state management
- User authentication state
- Session management
- Shared across all pages

#### `app/data.py`
- Sample data for development
- Mock trainees, jobs, institutions
- Will be replaced with database queries in Phase 2

### Shared Components (`app/shared/`)

#### `header.py`
- Responsive navigation header
- Role-based menu items
- User authentication controls
- Mobile-friendly hamburger menu

#### `footer.py`
- Site-wide footer
- Quick links
- Social media links
- Newsletter subscription
- Contact information

### Pages (`app/pages/`) - Organized by User Role

#### **🔗 Shared Pages (`app/pages/shared/`)**
*Pages used by multiple user types with role-specific views*

##### `home.py`
- Landing page with hero section
- Platform statistics and success stories
- Feature highlights and call-to-action sections
- Entry point for all user types

##### `auth.py`
- Universal authentication (login/signup)
- Role-specific signup forms (candidate, employer, institution)
- Password reset and social login placeholders
- Session management and role routing

##### `about.py`
- About TalentKonnect platform
- Mission, vision, and company story
- Team information and partnerships

##### `how_it_works.py`
- Platform workflow explanation
- Step-by-step guides for each user type
- User journey illustrations and getting started

##### `help_and_support.py`
- FAQ section and contact information
- Support tickets and user guides
- Documentation for all user roles

##### `search.py`
- **Candidate View**: Job search with filtering and recommendations
- **Employer View**: Talent discovery with candidate matching
- **Institution View**: Job market analysis for students
- Advanced filtering and saved searches

##### `jobs.py`
- **Candidate View**: Browse jobs, apply, bookmark positions
- **Employer View**: Manage posted jobs and view applications
- **Institution View**: Job market insights for curriculum planning
- Job details, requirements, and application tracking

##### `messaging.py`
- **Candidate ↔ Employer**: Direct communication and interview coordination
- **Institution ↔ Employer**: Partnership discussions and student placements
- Message threads, file sharing, and real-time notifications

#### **👥 Candidate Pages (`app/pages/candidates/`)**
*Focused on job seekers and trainees*

##### `dashboard.py`
- Personal dashboard overview
- Profile completion status and recommendations
- Application tracking summary
- Recommended jobs and skill assessments

##### `trainee_profile.py`
- Complete profile management
- Skills, competencies, and experience tracking
- Education history and certifications
- Portfolio showcase and achievement records

##### `application_tracking.py`
- View all submitted applications
- Application status tracking and updates
- Interview scheduling and preparation
- Communication history with employers

#### **🏢 Employer Pages (`app/pages/employers/`)**
*Focused on companies and hiring managers*

##### `employer_dashboard.py`
- Company overview and analytics dashboard
- Posted jobs performance and statistics
- Application management summary
- Recruitment metrics and insights

##### `job_posting.py`
- Create and manage job postings
- Job requirements specification and settings
- Application management and publishing controls
- Job performance analytics and optimization

#### **🎓 Institution Pages (`app/pages/institutions/`)**
*Focused on training institutions and schools*

##### `institution_dashboard.py`
- Institution overview and analytics
- Student placement statistics and success rates
- Program performance metrics
- Partnership management and employer relationships

##### `institution_program_listing.py`
- Manage training programs and curricula
- Program details, duration, and certification tracking
- Student enrollment and progress monitoring
- Industry alignment and skill mapping

#### **⚙️ Admin Pages (`app/pages/admin/`)**
*System administration and management*

##### `admin_management.py`
- System administration and user management
- Platform analytics and performance monitoring
- Content moderation and quality control
- System configuration and maintenance

##### `notification_management.py`
- Global notification settings and templates
- Email campaign management and preferences
- Push notification controls and scheduling
- Communication analytics and optimization

## �️ Organized Folder Structure Benefits

The new folder-based organization provides several key advantages:

### **📁 Clear Separation of Concerns**
- **`shared/`** - Pages with multi-role functionality
- **`candidates/`** - Job seeker and trainee focused features
- **`employers/`** - Company and hiring manager tools  
- **`institutions/`** - Training provider and school management
- **`admin/`** - System administration and oversight

### **🔍 Easy Navigation & Maintenance**
- **Logical Grouping**: Related pages are grouped together
- **Reduced Complexity**: Smaller, focused directories  
- **Clear Ownership**: Each team can focus on their user type
- **Scalable Structure**: Easy to add new features per role

### **👥 Role-Based Development**
Each folder serves specific user types with distinct goals:

#### **🎯 Candidates/Trainees** (`candidates/`)
**Primary Goal:** Find jobs and manage career journey
- Personal dashboard and profile management
- Application tracking and status updates
- Career development and skill building

#### **🏢 Employers** (`employers/`)  
**Primary Goal:** Find talent and manage hiring process
- Company dashboard and job posting tools
- Application management and candidate review
- Recruitment analytics and hiring insights

#### **🎓 Institutions** (`institutions/`)
**Primary Goal:** Manage training programs and student success
- Program management and curriculum tracking
- Student placement and employer partnerships
- Success metrics and industry alignment

#### **� Shared Functionality** (`shared/`)
**Cross-Role Features:** Pages serving multiple user types
- Authentication and general information pages
- Search functionality (jobs vs talent vs market analysis)
- Messaging system (candidate-employer communication)
- Universal help and support resources

#### **⚙️ Administrative** (`admin/`)
**System Management:** Platform oversight and administration
- User management and system analytics
- Content moderation and quality control
- Notification management and communication tools

## 🎯 Design Patterns

### 1. **Role-Based Architecture**
- Pages adapt content based on user role
- Shared components with role-specific variations
- Centralized authentication and authorization
- Dynamic navigation based on user permissions

### 2. **Separation of Concerns**
- Pages handle UI and user interaction
- State management is centralized
- Shared components are reusable
- Data layer is separate

### 3. **Component-Based Architecture**
- Reusable header and footer
- Modular page components
- Easy to maintain and extend

### 4. **Scalability Ready**
- Easy to add new pages for any role
- Simple to extend functionality
- Ready for database integration
- FastAPI integration prepared

## 🚀 Adding New Features

### To add a new page:

1. **Create page module** in `app/pages/`:
```python
# app/pages/new_page.py
from nicegui import ui
from app.shared.header import create_header
from app.shared.footer import create_footer

def new_page():
    create_header()
    # Your page content here
    create_footer()
```

2. **Register route** in `main.py`:
```python
from app.pages.new_page import new_page

@ui.page('/new-page')
def new():
    new_page()
```

### To add a new component:

1. **Create component** in `app/shared/`:
```python
# app/shared/new_component.py
from nicegui import ui

def create_new_component():
    # Component code here
    pass
```

2. **Import and use** in any page:
```python
from app.shared.new_component import create_new_component
```

## 🔄 State Management

The `app_state` object is globally accessible:

```python
from app.state import app_state

# Check authentication
if app_state.is_authenticated():
    # User is logged in
    user_email = app_state.current_user
    user_role = app_state.user_role

# Login user
app_state.login('user@example.com', 'trainee')

# Logout user
app_state.logout()
```

## 📦 Dependencies

- **nicegui** - Python UI framework
- **fastapi** - Backend framework (ready for integration)
- **uvicorn** - ASGI server
- **python-multipart** - File upload support

## 🎨 Styling

- **Tailwind CSS** - Utility-first CSS framework
- Responsive design (mobile, tablet, desktop)
- Consistent color scheme
- Modern UI components

## 🔜 Next Steps

1. **Backend Integration**
   - Set up FastAPI routes
   - Create database models
   - Implement authentication

2. **Database**
   - PostgreSQL or MongoDB
   - User management
   - Job postings
   - Applications tracking

3. **Advanced Features**
   - File uploads
   - Real-time messaging
   - Email notifications
   - Analytics dashboard

## 💡 Best Practices

1. **Keep components small and focused**
2. **Use shared components for consistency**
3. **Maintain separation between UI and logic**
4. **Follow the existing code style**
5. **Test each component independently**
6. **Document new features**

---

**Last Updated:** 2025-09-30
