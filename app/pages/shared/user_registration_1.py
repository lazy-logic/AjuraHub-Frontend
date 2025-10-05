"""
User Registration Page 1 - TalentConnect Africa
Multi-step registration workflow (Page 1) with role selection, basic information, and brand guidelines.
"""

from nicegui import ui

def user_registration_1_page():
    """Creates the user registration page 1 with brand guidelines and icon fixes."""
    
    # Add brand fonts and icon protection
    ui.add_head_html('''
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
        /* Brand typography - excludes icons to prevent font override */
        *:not(.material-icons):not(.q-icon):not([class*="material-icons"]):not(i) {
            font-family: 'Raleway', sans-serif !important;
        }

        /* Material Icons properties */
        .material-icons {
            font-family: 'Material Icons' !important;
            font-weight: normal;
            font-style: normal;
            font-size: 24px;
            line-height: 1;
            letter-spacing: normal;
            text-transform: none;
            display: inline-block;
            white-space: nowrap;
            word-wrap: normal;
            direction: ltr;
            font-feature-settings: 'liga';
            -webkit-font-smoothing: antialiased;
            -webkit-font-feature-settings: 'liga';
        }

        /* Typography classes */
        .heading-1 { font-size: 3rem; font-weight: 700; line-height: 1.1; }
        .heading-2 { font-size: 2.25rem; font-weight: 600; line-height: 1.2; }
        .sub-heading { font-size: 1.5rem; font-weight: 500; line-height: 1.4; }
        .body-text { font-size: 1rem; font-weight: 400; line-height: 1.6; }
        .caption { font-size: 0.75rem; font-weight: 400; }

        /* Brand colors */
        .brand-primary { color: #0055B8; }
        .brand-charcoal { color: #1A1A1A; }
        .brand-slate { color: #4D4D4D; }
        .brand-light-mist { background-color: #F2F7FB; }

        /* Custom styling */
        .registration-container {
            min-height: 100vh;
            background: linear-gradient(135deg, #F2F7FB 0%, #E3F2FD 100%);
        }
        
        .registration-card {
            background: white;
            border-radius: 16px;
            border: 1px solid #E5E7EB;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            max-width: 500px;
            width: 100%;
        }
        
        .progress-indicator {
            height: 4px;
            background: #E5E7EB;
            border-radius: 2px;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: #0055B8;
            width: 33.33%;
            transition: width 0.3s ease;
        }
        
        .role-option {
            border: 2px solid #E5E7EB;
            border-radius: 12px;
            padding: 24px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
        }
        
        .role-option:hover {
            border-color: #0055B8;
            background: #F0F7FF;
        }
        
        .role-option.selected {
            border-color: #0055B8;
            background: #F0F7FF;
        }
        
        .role-icon {
            width: 64px;
            height: 64px;
            background: #F3F4F6;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 16px;
            font-size: 32px;
            color: #6B7280;
        }
        
        .role-option.selected .role-icon {
            background: #0055B8;
            color: white;
        }
        
        .form-input {
            border: 1px solid #D1D5DB;
            border-radius: 8px;
            padding: 12px 16px;
            width: 100%;
            transition: border-color 0.2s;
        }
        
        .form-input:focus {
            border-color: #0055B8;
            outline: none;
            box-shadow: 0 0 0 3px rgba(0,85,184,0.1);
        }
        
        .step-indicator {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            font-size: 14px;
        }
        
        .step-active {
            background: #0055B8;
            color: white;
        }
        
        .step-inactive {
            background: #E5E7EB;
            color: #6B7280;
        }
        
        .step-connector {
            width: 60px;
            height: 2px;
            background: #E5E7EB;
        }
    </style>
    ''')
    
    with ui.column().classes('registration-container w-full min-h-screen flex items-center justify-center p-6'):
        # Registration card
        with ui.card().classes('registration-card'):
            with ui.card_section().classes('p-8'):
                # Header with logo and progress
                with ui.column().classes('w-full mb-8'):
                    # Logo and brand
                    with ui.row().classes('w-full items-center justify-center mb-6'):
                        ui.icon('account_balance').classes('text-blue-600 text-4xl mr-3')
                        ui.html('<div class="heading-2 brand-primary">TalentConnect Africa</div>')
                    
                    # Progress indicator
                    with ui.column().classes('w-full mb-4'):
                        ui.html('<div class="progress-indicator"><div class="progress-fill"></div></div>')
                        
                        # Step indicators
                        with ui.row().classes('w-full items-center justify-between mt-4'):
                            # Step 1 - Active
                            with ui.column().classes('items-center'):
                                ui.html('<div class="step-indicator step-active">1</div>')
                                ui.html('<div class="caption brand-slate mt-1">Account Type</div>')
                            
                            ui.html('<div class="step-connector"></div>')
                            
                            # Step 2 - Inactive
                            with ui.column().classes('items-center'):
                                ui.html('<div class="step-indicator step-inactive">2</div>')
                                ui.html('<div class="caption brand-slate mt-1">Profile Details</div>')
                            
                            ui.html('<div class="step-connector"></div>')
                            
                            # Step 3 - Inactive
                            with ui.column().classes('items-center'):
                                ui.html('<div class="step-indicator step-inactive">3</div>')
                                ui.html('<div class="caption brand-slate mt-1">Verification</div>')
                
                # Welcome text
                with ui.column().classes('w-full text-center mb-8'):
                    ui.html('<h1 class="heading-2 brand-charcoal mb-3">Join TalentConnect Africa</h1>')
                    ui.html('<p class="body-text brand-slate">Start your journey by selecting your account type</p>')
                
                # Role selection
                with ui.column().classes('w-full mb-8'):
                    ui.html('<div class="sub-heading brand-charcoal mb-6">I am a...</div>')
                    
                    # Role options
                    role_options = [
                        {
                            'role': 'trainee',
                            'title': 'Trainee/Job Seeker',
                            'description': 'Looking for internships, training programs, and job opportunities',
                            'icon': 'person'
                        },
                        {
                            'role': 'company',
                            'title': 'Company/Employer',
                            'description': 'Hiring talent and offering training programs',
                            'icon': 'business'
                        },
                        {
                            'role': 'institution',
                            'title': 'Training Institution',
                            'description': 'Providing educational programs and courses',
                            'icon': 'school'
                        }
                    ]
                    
                    for option in role_options:
                        with ui.column().classes('role-option mb-4'):
                            ui.html(f'<div class="role-icon"><i class="material-icons">{option["icon"]}</i></div>')
                            ui.html(f'<div class="body-text brand-charcoal font-medium mb-2">{option["title"]}</div>')
                            ui.html(f'<div class="caption brand-slate">{option["description"]}</div>')
                
                # Basic information form
                with ui.column().classes('w-full mb-8'):
                    ui.html('<div class="sub-heading brand-charcoal mb-6">Basic Information</div>')
                    
                    with ui.row().classes('w-full gap-4 mb-4'):
                        ui.input(label='First Name', placeholder='Enter your first name').classes('flex-1')
                        ui.input(label='Last Name', placeholder='Enter your last name').classes('flex-1')
                    
                    ui.input(label='Email Address', placeholder='your.email@example.com').classes('w-full mb-4')
                    ui.input(label='Phone Number', placeholder='+1 (555) 123-4567').classes('w-full mb-4')
                    
                    # Password fields
                    ui.input(label='Password', placeholder='Create a strong password', password=True).classes('w-full mb-4')
                    ui.input(label='Confirm Password', placeholder='Confirm your password', password=True).classes('w-full mb-4')
                    
                    # Password strength indicator
                    with ui.row().classes('w-full items-center gap-2 mb-4'):
                        ui.html('<div class="caption brand-slate">Password strength:</div>')
                        ui.linear_progress(0.6).classes('flex-grow')
                        ui.html('<div class="caption brand-primary">Strong</div>')
                
                # Terms and privacy
                with ui.column().classes('w-full mb-8'):
                    with ui.row().classes('w-full items-start gap-3'):
                        ui.checkbox().classes('mt-1')
                        ui.html('''
                        <div class="caption brand-slate">
                            I agree to the <a href="#" class="brand-primary">Terms of Service</a> 
                            and <a href="#" class="brand-primary">Privacy Policy</a>
                        </div>
                        ''')
                    
                    with ui.row().classes('w-full items-start gap-3 mt-3'):
                        ui.checkbox().classes('mt-1')
                        ui.html('<div class="caption brand-slate">I would like to receive updates and marketing communications</div>')
                
                # Action buttons
                with ui.row().classes('w-full gap-4'):
                    ui.button('Back to Login', icon='arrow_back').classes('flex-1 bg-gray-200 text-gray-700 py-3')
                    ui.button('Continue →', icon='arrow_forward').classes('flex-1 bg-blue-600 text-white py-3')
        
        # Additional help section
        with ui.column().classes('w-full max-w-md mt-6 text-center'):
            ui.html('<div class="caption brand-slate mb-3">Need help getting started?</div>')
            with ui.row().classes('w-full justify-center gap-6'):
                ui.button('Contact Support', icon='support_agent').classes('text-blue-600 p-2')
                ui.button('View Help Guide', icon='help').classes('text-blue-600 p-2')

# Export the page function
__all__ = ['user_registration_1_page']