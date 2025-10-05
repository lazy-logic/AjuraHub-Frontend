"""
User Registration Page 2 - TalentConnect Africa
Multi-step registration workflow (Page 2) with profile details, preferences, and completion.
"""

from nicegui import ui

def user_registration_2_page():
    """Creates the user registration page 2 with brand guidelines and icon fixes."""
    
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
            max-width: 600px;
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
            width: 66.66%;
            transition: width 0.3s ease;
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
        
        .step-completed {
            background: #10B981;
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
        
        .step-connector.completed {
            background: #10B981;
        }
        
        .profile-section {
            border: 1px solid #E5E7EB;
            border-radius: 12px;
            padding: 20px;
            background: #FAFBFC;
        }
        
        .skill-tag {
            display: inline-block;
            padding: 6px 12px;
            background: #E0F2FE;
            border: 1px solid #0369A1;
            border-radius: 20px;
            font-size: 14px;
            color: #0369A1;
            margin: 4px;
        }
        
        .avatar-placeholder {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            border: 3px dashed #D1D5DB;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #F9FAFB;
            cursor: pointer;
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
                            # Step 1 - Completed
                            with ui.column().classes('items-center'):
                                ui.html('<div class="step-indicator step-completed">✓</div>')
                                ui.html('<div class="caption brand-slate mt-1">Account Type</div>')
                            
                            ui.html('<div class="step-connector completed"></div>')
                            
                            # Step 2 - Active
                            with ui.column().classes('items-center'):
                                ui.html('<div class="step-indicator step-active">2</div>')
                                ui.html('<div class="caption brand-slate mt-1">Profile Details</div>')
                            
                            ui.html('<div class="step-connector"></div>')
                            
                            # Step 3 - Inactive
                            with ui.column().classes('items-center'):
                                ui.html('<div class="step-indicator step-inactive">3</div>')
                                ui.html('<div class="caption brand-slate mt-1">Verification</div>')
                
                # Welcome text
                with ui.column().classes('w-full text-center mb-8'):
                    ui.html('<h1 class="heading-2 brand-charcoal mb-3">Complete Your Profile</h1>')
                    ui.html('<p class="body-text brand-slate">Help us personalize your experience</p>')
                
                with ui.row().classes('w-full gap-8'):
                    # Left column - Profile photo and basic info
                    with ui.column().classes('flex-1'):
                        # Profile photo section
                        with ui.column().classes('profile-section mb-6'):
                            ui.html('<div class="sub-heading brand-charcoal mb-4">Profile Photo</div>')
                            
                            with ui.column().classes('items-center'):
                                ui.html('<div class="avatar-placeholder"><i class="material-icons text-gray-400 text-3xl">person</i></div>')
                                ui.button('Upload Photo', icon='camera_alt').classes('mt-3 bg-blue-600 text-white px-4 py-2')
                                ui.html('<div class="caption brand-slate mt-2">JPG, PNG up to 5MB</div>')
                        
                        # Location information
                        with ui.column().classes('profile-section'):
                            ui.html('<div class="sub-heading brand-charcoal mb-4">Location</div>')
                            
                            ui.select(['South Africa', 'Nigeria', 'Kenya', 'Ghana', 'Other'], 
                                     label='Country').classes('w-full mb-4')
                            ui.input(label='City', placeholder='Enter your city').classes('w-full mb-4')
                            ui.select(['GMT+2 (SAST)', 'GMT+1 (WAT)', 'GMT+3 (EAT)', 'Other'], 
                                     label='Time Zone').classes('w-full')
                    
                    # Right column - Professional details
                    with ui.column().classes('flex-1'):
                        # Professional information (Trainee-specific)
                        with ui.column().classes('profile-section mb-6'):
                            ui.html('<div class="sub-heading brand-charcoal mb-4">Professional Information</div>')
                            
                            ui.input(label='Current/Desired Job Title', 
                                    placeholder='e.g., Software Developer').classes('w-full mb-4')
                            
                            ui.select(['Technology', 'Healthcare', 'Finance', 'Education', 'Marketing', 'Other'], 
                                     label='Industry Interest').classes('w-full mb-4')
                            
                            ui.select(['Entry Level', '1-2 years', '3-5 years', '5+ years'], 
                                     label='Experience Level').classes('w-full mb-4')
                            
                            ui.textarea(label='Brief Bio', 
                                       placeholder='Tell us about yourself and your career goals...').classes('w-full')
                        
                        # Skills section
                        with ui.column().classes('profile-section'):
                            ui.html('<div class="sub-heading brand-charcoal mb-4">Skills & Interests</div>')
                            
                            ui.html('<div class="body-text brand-slate mb-3">Select your top skills:</div>')
                            with ui.row().classes('flex-wrap gap-2 mb-4'):
                                skills = [
                                    'Python', 'JavaScript', 'React', 'Node.js', 'Data Analysis',
                                    'Digital Marketing', 'Graphic Design', 'Project Management',
                                    'Sales', 'Customer Service', 'Writing', 'Social Media'
                                ]
                                for skill in skills:
                                    ui.chip(skill, removable=False).classes('bg-blue-100 text-blue-800 cursor-pointer')
                            
                            ui.input(placeholder='Add custom skill...').classes('w-full')
                
                # Preferences section
                with ui.column().classes('profile-section w-full mt-6 mb-8'):
                    ui.html('<div class="sub-heading brand-charcoal mb-4">Preferences</div>')
                    
                    with ui.row().classes('w-full gap-8'):
                        # Work preferences
                        with ui.column().classes('flex-1'):
                            ui.html('<div class="body-text brand-slate mb-3">Work Preferences:</div>')
                            
                            with ui.column().classes('space-y-2'):
                                with ui.row().classes('items-center gap-3'):
                                    ui.checkbox()
                                    ui.html('<div class="body-text brand-charcoal">Remote work</div>')
                                
                                with ui.row().classes('items-center gap-3'):
                                    ui.checkbox()
                                    ui.html('<div class="body-text brand-charcoal">On-site work</div>')
                                
                                with ui.row().classes('items-center gap-3'):
                                    ui.checkbox()
                                    ui.html('<div class="body-text brand-charcoal">Hybrid work</div>')
                                
                                with ui.row().classes('items-center gap-3'):
                                    ui.checkbox()
                                    ui.html('<div class="body-text brand-charcoal">Willing to relocate</div>')
                        
                        # Opportunity types
                        with ui.column().classes('flex-1'):
                            ui.html('<div class="body-text brand-slate mb-3">Opportunity Types:</div>')
                            
                            with ui.column().classes('space-y-2'):
                                with ui.row().classes('items-center gap-3'):
                                    ui.checkbox()
                                    ui.html('<div class="body-text brand-charcoal">Internships</div>')
                                
                                with ui.row().classes('items-center gap-3'):
                                    ui.checkbox()
                                    ui.html('<div class="body-text brand-charcoal">Training Programs</div>')
                                
                                with ui.row().classes('items-center gap-3'):
                                    ui.checkbox()
                                    ui.html('<div class="body-text brand-charcoal">Full-time Jobs</div>')
                                
                                with ui.row().classes('items-center gap-3'):
                                    ui.checkbox()
                                    ui.html('<div class="body-text brand-charcoal">Freelance Work</div>')
                
                # Notification preferences
                with ui.column().classes('w-full mb-8'):
                    ui.html('<div class="sub-heading brand-charcoal mb-4">Notification Preferences</div>')
                    
                    with ui.row().classes('w-full items-center justify-between p-4 bg-gray-50 rounded-lg mb-3'):
                        ui.html('<div class="body-text brand-charcoal">Email notifications for new opportunities</div>')
                        ui.switch().classes('').props('value=true')
                    
                    with ui.row().classes('w-full items-center justify-between p-4 bg-gray-50 rounded-lg mb-3'):
                        ui.html('<div class="body-text brand-charcoal">SMS notifications for urgent updates</div>')
                        ui.switch().classes('')
                    
                    with ui.row().classes('w-full items-center justify-between p-4 bg-gray-50 rounded-lg'):
                        ui.html('<div class="body-text brand-charcoal">Weekly digest of recommended opportunities</div>')
                        ui.switch().classes('').props('value=true')
                
                # Action buttons
                with ui.row().classes('w-full gap-4'):
                    ui.button('← Back', icon='arrow_back').classes('flex-1 bg-gray-200 text-gray-700 py-3')
                    ui.button('Complete Registration', icon='check_circle').classes('flex-1 bg-blue-600 text-white py-3')
        
        # Progress summary
        with ui.column().classes('w-full max-w-md mt-6 text-center'):
            ui.html('<div class="caption brand-slate mb-2">Almost done! One more step to verify your account.</div>')
            ui.html('<div class="caption brand-slate">You\'ll receive a verification email after completing this step.</div>')

# Export the page function
__all__ = ['user_registration_2_page']