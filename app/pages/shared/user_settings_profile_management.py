"""
User Settings & Profile Management - Dompell Africa
Comprehensive user settings with profile management, privacy controls, and preferences using brand guidelines.
"""

from nicegui import ui

def user_settings_profile_management_page():
    """Creates the user settings and profile management page with brand guidelines and icon fixes."""
    
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
        .settings-card {
            background: white;
            border-radius: 12px;
            border: 1px solid #E5E7EB;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .settings-nav {
            border-right: 1px solid #E5E7EB;
            background: #F9FAFB;
        }
        
        .nav-item {
            padding: 12px 16px;
            cursor: pointer;
            border-radius: 8px;
            margin: 4px;
            transition: all 0.2s;
        }
        
        .nav-item:hover {
            background: #E5E7EB;
        }
        
        .nav-item.active {
            background: #0055B8;
            color: white;
        }
        
        .profile-avatar {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            border: 3px solid #E5E7EB;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #F3F4F6;
        }
        
        .privacy-option {
            padding: 16px;
            border: 1px solid #E5E7EB;
            border-radius: 8px;
            background: #FAFAFA;
        }
        
        .notification-item {
            padding: 12px;
            border-bottom: 1px solid #E5E7EB;
            display: flex;
            align-items: center;
            justify-content: between;
        }
    </style>
    ''')
    
    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Header
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 mb-8'):
            with ui.row().classes('w-full items-center justify-between'):
                ui.html('<h1 class="heading-2 brand-charcoal">User Settings & Profile</h1>')
                ui.button('Save All Changes', icon='save').classes('bg-blue-600 text-white px-6 py-3')
        
        # Main content
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 gap-0'):
            # Navigation sidebar
            with ui.column().classes('w-64 settings-nav min-h-screen'):
                    with ui.column().classes('p-4'):
                        nav_items = [
                        {'icon': 'person', 'label': 'Profile Information', 'active': True},
                        {'icon': 'security', 'label': 'Security & Privacy', 'active': False},
                        {'icon': 'notifications', 'label': 'Notifications', 'active': False},
                        {'icon': 'palette', 'label': 'Appearance', 'active': False},
                        {'icon': 'language', 'label': 'Language & Region', 'active': False},
                        {'icon': 'link', 'label': 'Connected Accounts', 'active': False},
                        {'icon': 'storage', 'label': 'Data & Privacy', 'active': False},
                        {'icon': 'payment', 'label': 'Billing & Plans', 'active': False}
                    ]
                    
                    for item in nav_items:
                        item_class = 'nav-item active' if item['active'] else 'nav-item'
                        with ui.row().classes(f'{item_class} w-full items-center gap-3'):

                            ui.html(f'<div class="body-text">{item["label"]}</div>')
            
            # Main content area
            with ui.column().classes('flex-grow p-8'):
                # Profile Information Section (active)
                with ui.card().classes('w-full mb-6 settings-card'):
                    with ui.card_section().classes('p-6'):
                        ui.html('<h2 class="sub-heading brand-charcoal mb-6">Profile Information</h2>')
                        
                        with ui.row().classes('w-full gap-8 mb-8'):
                            # Profile avatar
                            with ui.column().classes('items-center'):
                                ui.html('<div class="profile-avatar"><i class="material-icons text-gray-400 text-4xl">person</i></div>')
                                ui.button('Change Photo', icon='camera_alt').classes('mt-3 bg-blue-600 text-white px-4 py-2')
                                ui.button('Remove', icon='delete').classes('mt-2 text-red-600 px-4 py-2')
                            
                            # Profile form
                            with ui.column().classes('flex-grow space-y-4'):
                                with ui.row().classes('w-full gap-4'):
                                    ui.input(label='First Name', value='Sarah').classes('flex-1')
                                    ui.input(label='Last Name', value='Johnson').classes('flex-1')
                                
                                ui.input(label='Professional Title', value='Software Engineer').classes('w-full')
                                ui.input(label='Email Address', value='sarah.johnson@email.com').classes('w-full')
                                ui.input(label='Phone Number', value='+1 (555) 123-4567').classes('w-full')
                                
                                ui.textarea(label='Bio',
                                           value='Passionate software engineer with 5+ years of experience...').classes('w-full')
                        
                        # Additional profile sections
                        with ui.row().classes('w-full gap-8'):
                            # Location
                            with ui.column().classes('flex-1'):
                                ui.html('<h3 class="sub-heading brand-charcoal mb-4">Location</h3>')
                                ui.select(['United States', 'Canada', 'United Kingdom', 'South Africa'], 
                                         label='Country', value='United States').classes('w-full mb-3')
                                ui.input(label='City', value='San Francisco').classes('w-full mb-3')
                                ui.select(['Pacific Time', 'Eastern Time', 'Central Time', 'Mountain Time'], 
                                         label='Time Zone', value='Pacific Time').classes('w-full')
                            
                            # Professional Links
                            with ui.column().classes('flex-1'):
                                ui.html('<h3 class="sub-heading brand-charcoal mb-4">Professional Links</h3>')
                                ui.input(label='LinkedIn Profile', placeholder='https://linkedin.com/in/username').classes('w-full mb-3')
                                ui.input(label='GitHub Profile', placeholder='https://github.com/username').classes('w-full mb-3')
                                ui.input(label='Portfolio Website', placeholder='https://yoursite.com').classes('w-full')
                
                # Security & Privacy Section
                with ui.card().classes('w-full mb-6 settings-card'):
                    with ui.card_section().classes('p-6'):
                        ui.html('<h2 class="sub-heading brand-charcoal mb-6">Security & Privacy</h2>')
                        
                        # Password settings
                        with ui.column().classes('mb-6'):
                            ui.html('<h3 class="sub-heading brand-charcoal mb-4">Password & Authentication</h3>')
                            
                            with ui.row().classes('w-full items-center justify-between p-4 bg-gray-50 rounded-lg mb-3'):
                                with ui.column():
                                    ui.html('<div class="body-text brand-charcoal font-medium">Password</div>')
                                    ui.html('<div class="caption brand-slate">Last changed 2 months ago</div>')
                                ui.button('Change Password', icon='lock').classes('bg-blue-600 text-white px-4 py-2')
                            
                            with ui.row().classes('w-full items-center justify-between p-4 bg-gray-50 rounded-lg mb-3'):
                                with ui.column():
                                    ui.html('<div class="body-text brand-charcoal font-medium">Two-Factor Authentication</div>')
                                    ui.html('<div class="caption brand-slate">Add extra security to your account</div>')
                                ui.switch().classes('')
                            
                            with ui.row().classes('w-full items-center justify-between p-4 bg-gray-50 rounded-lg'):
                                with ui.column():
                                    ui.html('<div class="body-text brand-charcoal font-medium">Login Alerts</div>')
                                    ui.html('<div class="caption brand-slate">Get notified of suspicious activity</div>')
                                ui.switch().classes('').props('value=true')
                        
                        # Privacy settings
                        privacy_options = [
                            {
                                'title': 'Profile Visibility',
                                'description': 'Who can see your full profile',
                                'options': ['Public', 'Connections Only', 'Private']
                            },
                            {
                                'title': 'Contact Information',
                                'description': 'Who can see your email and phone',
                                'options': ['Everyone', 'Connections', 'Nobody']
                            },
                            {
                                'title': 'Activity Status',
                                'description': 'Show when you\'re online',
                                'options': ['Always', 'Connections Only', 'Never']
                            }
                        ]
                        
                        ui.html('<h3 class="sub-heading brand-charcoal mb-4">Privacy Controls</h3>')
                        for option in privacy_options:
                            with ui.column().classes('privacy-option mb-4'):
                                ui.html(f'<div class="body-text brand-charcoal font-medium mb-1">{option["title"]}</div>')
                                ui.html(f'<div class="caption brand-slate mb-3">{option["description"]}</div>')
                                ui.select(option['options'], value=option['options'][1]).classes('w-48')
                
                # Notification Preferences
                with ui.card().classes('w-full mb-6 settings-card'):
                    with ui.card_section().classes('p-6'):
                        ui.html('<h2 class="sub-heading brand-charcoal mb-6">Notification Preferences</h2>')
                        
                        notification_categories = [
                            {
                                'title': 'Application Updates',
                                'items': [
                                    ('New application received', True, True),
                                    ('Application status changed', True, False),
                                    ('Interview scheduled', True, True)
                                ]
                            },
                            {
                                'title': 'Messages & Communication',
                                'items': [
                                    ('New messages', True, True),
                                    ('Mention in comments', True, False),
                                    ('Weekly digest', False, True)
                                ]
                            },
                            {
                                'title': 'System & Account',
                                'items': [
                                    ('Security alerts', True, True),
                                    ('Product updates', False, True),
                                    ('Marketing communications', False, False)
                                ]
                            }
                        ]
                        
                        for category in notification_categories:
                            with ui.column().classes('mb-6'):
                                ui.html(f'<h3 class="sub-heading brand-charcoal mb-4">{category["title"]}</h3>')
                                
                                # Header row
                                with ui.row().classes('w-full items-center mb-3'):
                                    ui.html('<div class="body-text brand-slate font-medium" style="width: 60%;">Notification Type</div>')
                                    ui.html('<div class="body-text brand-slate font-medium" style="width: 20%;">Email</div>')
                                    ui.html('<div class="body-text brand-slate font-medium" style="width: 20%;">Push</div>')
                                
                                for item_name, email_enabled, push_enabled in category['items']:
                                    with ui.row().classes('notification-item w-full items-center'):
                                        ui.html(f'<div class="body-text brand-charcoal" style="width: 60%;">{item_name}</div>')
                                        ui.switch().classes('').props(f'value={str(email_enabled).lower()}').style('width: 20%;')
                                        ui.switch().classes('').props(f'value={str(push_enabled).lower()}').style('width: 20%;')
                
                # Account actions
                with ui.card().classes('w-full settings-card'):
                    with ui.card_section().classes('p-6'):
                        ui.html('<h2 class="sub-heading brand-charcoal mb-6">Account Actions</h2>')
                        
                        with ui.row().classes('w-full gap-4'):
                            ui.button('Export Data', icon='download').classes('bg-green-600 text-white px-6 py-3')
                            ui.button('Deactivate Account', icon='pause_circle').classes('bg-yellow-600 text-white px-6 py-3')
                            ui.button('Delete Account', icon='delete_forever').classes('bg-red-600 text-white px-6 py-3')

# Export the page function
__all__ = ['user_settings_profile_management_page']