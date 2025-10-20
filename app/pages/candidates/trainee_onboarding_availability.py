"""
Trainee Onboarding - Availability & Review - TalentConnect Africa
Availability setup with calendar integration and schedule management using brand guidelines.
"""

from nicegui import ui

def trainee_onboarding_availability_page():
    """Creates the trainee onboarding availability setup page with brand guidelines and icon fixes."""
    
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
        .button-label { font-size: 0.875rem; font-weight: 600; }
        .caption { font-size: 0.75rem; font-weight: 400; }

        /* Brand colors */
        .brand-primary { color: #0055B8; }
        .brand-charcoal { color: #1A1A1A; }
        .brand-slate { color: #4D4D4D; }
        .brand-light-mist { background-color: #F2F7FB; }
        .brand-primary-bg { background-color: #0055B8; }

        /* Custom styling */
        .availability-card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .time-slot {
            background: #F8FAFC;
            border: 2px solid #E2E8F0;
            border-radius: 8px;
            padding: 12px 16px;
            margin: 4px;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }

        .time-slot:hover {
            border-color: #0055B8;
            background: #F2F7FB;
        }

        .time-slot.selected {
            border-color: #0055B8;
            background: #0055B8;
            color: white;
        }

        .day-selector {
            background: #F8FAFC;
            border: 2px solid #E2E8F0;
            border-radius: 8px;
            padding: 16px;
            margin: 8px 4px;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
            min-width: 120px;
        }

        .day-selector:hover {
            border-color: #0055B8;
            background: #F2F7FB;
        }

        .day-selector.selected {
            border-color: #0055B8;
            background: #0055B8;
            color: white;
        }

        .progress-bar {
            background: #E5E7EB;
            height: 8px;
            border-radius: 4px;
            overflow: hidden;
        }

        .progress-fill {
            background: #0055B8;
            height: 100%;
            transition: width 0.3s ease;
        }

        .availability-summary {
            background: #F0F9FF;
            border: 1px solid #0EA5E9;
            border-radius: 8px;
            padding: 16px;
        }

        .location-option {
            background: white;
            border: 2px solid #E2E8F0;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 12px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .location-option:hover {
            border-color: #0055B8;
            box-shadow: 0 2px 8px rgba(0, 85, 184, 0.1);
        }

        .location-option.selected {
            border-color: #0055B8;
            background: #F2F7FB;
        }
    </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Progress indicator
        with ui.row().classes('w-full max-w-4xl mx-auto px-6 mb-8'):
            with ui.column().classes('w-full'):
                with ui.row().classes('w-full items-center justify-between mb-4'):
                    ui.label('Step 3 of 4: Availability & Preferences').classes('body-text brand-slate')
                    ui.label('75% Complete').classes('caption brand-slate')
                
                with ui.element('div').classes('progress-bar w-full'):
                    ui.element('div').classes('progress-fill').style('width: 75%')

        # Header section
        with ui.row().classes('w-full max-w-4xl mx-auto px-6 mb-8 text-center'):
            with ui.column().classes('w-full'):
                ui.label('Set Your Availability').classes('heading-2 brand-charcoal mb-4')
                ui.label('Help us match you with opportunities that fit your schedule and preferences').classes('body-text brand-slate')

        # Main content
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 gap-8'):
            # Left column - Availability settings
            with ui.column().classes('flex-1'):
                # Working days
                with ui.card().classes('availability-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Preferred Working Days').classes('sub-heading brand-charcoal ml-3')
                    
                    ui.label('Select the days you\'re available to work or attend training').classes('body-text brand-slate mb-4')
                    
                    with ui.row().classes('flex-wrap'):
                        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                        for day in days:
                            with ui.element('div').classes('day-selector'):
                                ui.label(day[:3]).classes('body-text font-semibold')
                                ui.label(day).classes('caption')

                # Working hours
                with ui.card().classes('availability-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Preferred Working Hours').classes('sub-heading brand-charcoal ml-3')
                    
                    ui.label('What time of day works best for you?').classes('body-text brand-slate mb-4')
                    
                    # Morning slots
                    with ui.column().classes('mb-6'):
                        ui.label('Morning (6:00 AM - 12:00 PM)').classes('body-text font-semibold brand-charcoal mb-3')
                        with ui.row().classes('flex-wrap'):
                            morning_slots = ['6:00 AM', '7:00 AM', '8:00 AM', '9:00 AM', '10:00 AM', '11:00 AM']
                            for slot in morning_slots:
                                with ui.element('div').classes('time-slot'):
                                    ui.label(slot).classes('caption font-semibold')
                    
                    # Afternoon slots
                    with ui.column().classes('mb-6'):
                        ui.label('Afternoon (12:00 PM - 6:00 PM)').classes('body-text font-semibold brand-charcoal mb-3')
                        with ui.row().classes('flex-wrap'):
                            afternoon_slots = ['12:00 PM', '1:00 PM', '2:00 PM', '3:00 PM', '4:00 PM', '5:00 PM']
                            for slot in afternoon_slots:
                                with ui.element('div').classes('time-slot'):
                                    ui.label(slot).classes('caption font-semibold')
                    
                    # Evening slots
                    with ui.column():
                        ui.label('Evening (6:00 PM - 10:00 PM)').classes('body-text font-semibold brand-charcoal mb-3')
                        with ui.row().classes('flex-wrap'):
                            evening_slots = ['6:00 PM', '7:00 PM', '8:00 PM', '9:00 PM']
                            for slot in evening_slots:
                                with ui.element('div').classes('time-slot'):
                                    ui.label(slot).classes('caption font-semibold')

                # Location preferences
                with ui.card().classes('availability-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Location Preferences').classes('sub-heading brand-charcoal ml-3')
                    
                    ui.label('Where are you comfortable working or attending training?').classes('body-text brand-slate mb-4')
                    
                    # Remote work
                    with ui.element('div').classes('location-option selected'):
                        with ui.row().classes('items-center justify-between'):
                            with ui.row().classes('items-center'):

                                with ui.column():
                                    ui.label('Remote Work').classes('body-text font-semibold brand-charcoal')
                                    ui.label('Work from home or any location with internet').classes('caption brand-slate')

                    
                    # On-site work
                    with ui.element('div').classes('location-option'):
                        with ui.row().classes('items-center justify-between'):
                            with ui.row().classes('items-center'):

                                with ui.column():
                                    ui.label('On-site Work').classes('body-text font-semibold brand-charcoal')
                                    ui.label('Work at company offices or training centers').classes('caption brand-slate')

                    
                    # Hybrid work
                    with ui.element('div').classes('location-option'):
                        with ui.row().classes('items-center justify-between'):
                            with ui.row().classes('items-center'):

                                with ui.column():
                                    ui.label('Hybrid Work').classes('body-text font-semibold brand-charcoal')
                                    ui.label('Combination of remote and on-site work').classes('caption brand-slate')


                # Travel preferences
                with ui.card().classes('availability-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Travel & Relocation').classes('sub-heading brand-charcoal ml-3')
                    
                    ui.label('Are you open to travel or relocation for opportunities?').classes('body-text brand-slate mb-4')
                    
                    with ui.column().classes('gap-4'):
                        # Travel willingness
                        with ui.row().classes('items-center'):
                            ui.checkbox('I am willing to travel for work opportunities').classes('mr-3')
                            ui.label('Travel for Work').classes('body-text brand-charcoal')
                        
                        # Relocation willingness
                        with ui.row().classes('items-center'):
                            ui.checkbox('I am open to relocating for the right opportunity').classes('mr-3')
                            ui.label('Open to Relocation').classes('body-text brand-charcoal')
                        
                        # Maximum travel distance
                        ui.label('Maximum Travel Distance').classes('body-text font-semibold brand-charcoal mt-4 mb-2')
                        ui.select([
                            'Within my city/town',
                            'Within 50km radius',
                            'Within 100km radius',
                            'Anywhere in my country',
                            'International travel OK'
                        ], value='Within 100km radius').classes('w-full')

            # Right column - Summary & preferences
            with ui.column().classes('w-80'):
                # Availability summary
                with ui.card().classes('availability-card'):
                    ui.label('Availability Summary').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.element('div').classes('availability-summary'):
                        with ui.row().classes('items-center mb-3'):

                            ui.label('40 hours/week').classes('body-text font-semibold brand-charcoal')
                        
                        with ui.row().classes('items-center mb-3'):

                            ui.label('Mon - Fri').classes('body-text font-semibold brand-charcoal')
                        
                        with ui.row().classes('items-center mb-3'):

                            ui.label('9:00 AM - 5:00 PM').classes('body-text font-semibold brand-charcoal')
                        
                        with ui.row().classes('items-center'):

                            ui.label('Remote Preferred').classes('body-text font-semibold brand-charcoal')

                # Additional preferences
                with ui.card().classes('availability-card'):
                    ui.label('Additional Preferences').classes('sub-heading brand-charcoal mb-4')
                    
                    ui.label('Start Date').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.select([
                        'Immediately',
                        'Within 1 week',
                        'Within 2 weeks',
                        'Within 1 month',
                        'Specific date'
                    ], value='Within 2 weeks').classes('w-full mb-4')
                    
                    ui.label('Commitment Level').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.select([
                        'Full-time (40+ hours/week)',
                        'Part-time (20-39 hours/week)',
                        'Contract (Project-based)',
                        'Internship',
                        'Flexible'
                    ], value='Full-time (40+ hours/week)').classes('w-full mb-4')
                    
                    ui.label('Notice Period').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.select([
                        'No notice required',
                        '1 week notice',
                        '2 weeks notice',
                        '1 month notice',
                        'Other'
                    ], value='2 weeks notice').classes('w-full')

                # Calendar integration
                with ui.card().classes('availability-card'):
                    ui.label('Calendar Integration').classes('sub-heading brand-charcoal mb-4')
                    
                    ui.label('Connect your calendar to automatically sync availability').classes('body-text brand-slate mb-4')
                    
                    with ui.column().classes('gap-3'):
                        with ui.row().classes('items-center p-3 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-50'):

                            with ui.column().classes('flex-1'):
                                ui.label('Google Calendar').classes('body-text font-semibold brand-charcoal')
                                ui.label('Sync with Google Calendar').classes('caption brand-slate')
                            ui.button('Connect').props('flat').style('color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                        
                        with ui.row().classes('items-center p-3 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-50'):

                            with ui.column().classes('flex-1'):
                                ui.label('Outlook Calendar').classes('body-text font-semibold brand-charcoal')
                                ui.label('Sync with Outlook Calendar').classes('caption brand-slate')
                            ui.button('Connect').props('flat').style('color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')

        # Navigation buttons
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 mt-8 mb-12'):
            with ui.row().classes('w-full justify-between items-center'):
                ui.button('← Back: Skills & Experience').props('outlined').classes('px-6 py-3').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                
                with ui.row().classes('gap-3'):
                    ui.button('Save as Draft').props('outlined').classes('px-6 py-3').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                    ui.button('Continue to Review →').classes('px-6 py-3').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')
