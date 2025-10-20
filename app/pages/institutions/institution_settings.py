"""
Institution Settings Page for Dompell Africa
"""

from nicegui import ui

def institution_settings_page():
    """Creates the institution settings page with brand guidelines."""
    
    # Add brand styling
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <style>
            * { font-family: 'Raleway', sans-serif !important; }
            
            .heading-1 { font-size: 48px; font-weight: 700; color: #1A1A1A; line-height: 110%; }
            .heading-2 { font-size: 32px; font-weight: 600; color: #1A1A1A; line-height: 115%; }
            .sub-heading { font-size: 24px; font-weight: 600; color: #1A1A1A; }
            .body-text { font-size: 16px; font-weight: 400; color: #1A1A1A; }
            .caption { font-size: 12px; font-weight: 400; color: #4D4D4D; }
            
            .brand-primary { color: #0055B8 !important; }
            .brand-primary-bg { background-color: #0055B8 !important; }
            
            .settings-card {
                background: white;
                border-radius: 12px;
                border: 1px solid rgba(0, 85, 184, 0.1);
                box-shadow: 0 2px 8px rgba(0, 85, 184, 0.05);
                padding: 24px;
                margin-bottom: 24px;
            }
            
            .settings-section {
                border-bottom: 1px solid #E5E7EB;
                padding: 20px 0;
            }
            
            .settings-section:last-child {
                border-bottom: none;
            }
        </style>
    ''')
    
    with ui.column().classes('w-full min-h-screen').style('background: #F2F7FB; padding-top: 5rem;'):
        with ui.column().classes('w-full max-w-5xl mx-auto px-6 py-8'):
            # Page Header
            ui.label('Institution Settings').classes('heading-1 mb-2')
            ui.label('Manage your institution account and preferences').classes('body-text mb-8').style('color: #4D4D4D;')
            
            # Profile Settings
            with ui.element('div').classes('settings-card'):
                ui.label('Profile Information').classes('sub-heading mb-4')
                
                with ui.element('div').classes('settings-section'):
                    ui.label('Institution Name').classes('body-text font-semibold mb-2')
                    ui.input(placeholder='Enter institution name', value='University of Lagos').classes('w-full').props('outlined')
                
                with ui.element('div').classes('settings-section'):
                    ui.label('Email Address').classes('body-text font-semibold mb-2')
                    ui.input(placeholder='contact@institution.edu', value='contact@unilag.edu.ng').classes('w-full').props('outlined')
                
                with ui.element('div').classes('settings-section'):
                    ui.label('Phone Number').classes('body-text font-semibold mb-2')
                    ui.input(placeholder='+234 XXX XXX XXXX', value='+234 801 234 5678').classes('w-full').props('outlined')
                
                with ui.element('div').classes('settings-section'):
                    ui.label('Website').classes('body-text font-semibold mb-2')
                    ui.input(placeholder='https://www.institution.edu', value='https://www.unilag.edu.ng').classes('w-full').props('outlined')
                
                with ui.element('div').classes('settings-section'):
                    ui.label('Address').classes('body-text font-semibold mb-2')
                    ui.textarea(placeholder='Enter full address', value='University of Lagos, Akoka, Yaba, Lagos State, Nigeria').classes('w-full').props('outlined rows=3')
                
                ui.button('Save Profile Changes', icon='save').classes('brand-primary-bg text-white px-6 py-3 rounded mt-4')
            
            # Notification Settings
            with ui.element('div').classes('settings-card'):
                ui.label('Notification Preferences').classes('sub-heading mb-4')
                
                with ui.element('div').classes('settings-section'):
                    with ui.row().classes('items-center justify-between'):
                        with ui.column().classes('gap-1'):
                            ui.label('Email Notifications').classes('body-text font-semibold')
                            ui.label('Receive email updates about applications and programs').classes('caption')
                        ui.switch(value=True)
                
                with ui.element('div').classes('settings-section'):
                    with ui.row().classes('items-center justify-between'):
                        with ui.column().classes('gap-1'):
                            ui.label('Application Alerts').classes('body-text font-semibold')
                            ui.label('Get notified when students apply to your programs').classes('caption')
                        ui.switch(value=True)
                
                with ui.element('div').classes('settings-section'):
                    with ui.row().classes('items-center justify-between'):
                        with ui.column().classes('gap-1'):
                            ui.label('Weekly Reports').classes('body-text font-semibold')
                            ui.label('Receive weekly summary of program performance').classes('caption')
                        ui.switch(value=False)
                
                with ui.element('div').classes('settings-section'):
                    with ui.row().classes('items-center justify-between'):
                        with ui.column().classes('gap-1'):
                            ui.label('Marketing Communications').classes('body-text font-semibold')
                            ui.label('Receive updates about new features and promotions').classes('caption')
                        ui.switch(value=True)
            
            # Security Settings
            with ui.element('div').classes('settings-card'):
                ui.label('Security & Privacy').classes('sub-heading mb-4')
                
                with ui.element('div').classes('settings-section'):
                    ui.label('Change Password').classes('body-text font-semibold mb-2')
                    ui.input(placeholder='Current password', password=True, password_toggle_button=True).classes('w-full mb-2').props('outlined')
                    ui.input(placeholder='New password', password=True, password_toggle_button=True).classes('w-full mb-2').props('outlined')
                    ui.input(placeholder='Confirm new password', password=True, password_toggle_button=True).classes('w-full').props('outlined')
                    ui.button('Update Password', icon='lock').classes('brand-primary-bg text-white px-6 py-3 rounded mt-4')
                
                with ui.element('div').classes('settings-section'):
                    ui.label('Two-Factor Authentication').classes('body-text font-semibold mb-2')
                    ui.label('Add an extra layer of security to your account').classes('caption mb-3')
                    with ui.row().classes('items-center gap-3'):
                        ui.switch(value=False)
                        ui.label('Enable 2FA').classes('body-text')
            
            # Billing Settings
            with ui.element('div').classes('settings-card'):
                ui.label('Billing & Subscription').classes('sub-heading mb-4')
                
                with ui.element('div').classes('settings-section'):
                    with ui.row().classes('items-center justify-between'):
                        with ui.column().classes('gap-1'):
                            ui.label('Current Plan').classes('body-text font-semibold')
                            ui.label('Professional Plan - $79/month').classes('caption')
                        ui.button('Upgrade Plan', icon='arrow_upward').props('flat').classes('brand-primary')
                
                with ui.element('div').classes('settings-section'):
                    ui.label('Payment Method').classes('body-text font-semibold mb-2')
                    ui.label('•••• •••• •••• 4242 (Visa)').classes('body-text mb-2')
                    ui.button('Update Payment Method', icon='credit_card').props('flat').classes('brand-primary')
                
                with ui.element('div').classes('settings-section'):
                    ui.label('Billing History').classes('body-text font-semibold mb-2')
                    ui.button('View Invoices', icon='receipt').props('flat').classes('brand-primary')
            
            # Danger Zone
            with ui.element('div').classes('settings-card').style('border-color: #EF4444;'):
                ui.label('Danger Zone').classes('sub-heading mb-4').style('color: #EF4444;')
                
                with ui.element('div').classes('settings-section'):
                    ui.label('Deactivate Account').classes('body-text font-semibold mb-2')
                    ui.label('Temporarily disable your institution account').classes('caption mb-3')
                    ui.button('Deactivate Account', icon='block').props('outline').style('color: #EF4444; border-color: #EF4444;')
                
                with ui.element('div').classes('settings-section'):
                    ui.label('Delete Account').classes('body-text font-semibold mb-2')
                    ui.label('Permanently delete your account and all data').classes('caption mb-3')
                    ui.button('Delete Account', icon='delete_forever').props('outline').style('color: #DC2626; border-color: #DC2626;')
