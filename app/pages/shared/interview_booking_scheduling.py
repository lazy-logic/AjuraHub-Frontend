"""
Interview Booking & Scheduling - TalentConnect Africa
Interview scheduling system with calendar integration and video call setup using brand guidelines.
"""

from nicegui import ui

def interview_booking_scheduling_page():
    """Creates the interview booking and scheduling page with brand guidelines and icon fixes."""
    
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
        .interview-card {
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

        .time-slot.unavailable {
            background: #F3F4F6;
            border-color: #D1D5DB;
            color: #9CA3AF;
            cursor: not-allowed;
        }

        .calendar-day {
            min-height: 100px;
            border: 1px solid #E5E7EB;
            padding: 8px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .calendar-day:hover {
            background: #F9FAFB;
        }

        .calendar-day.selected {
            background: #EBF4FF;
            border-color: #0055B8;
        }

        .calendar-day.has-slots {
            border-color: #10B981;
        }

        .interview-type-card {
            background: white;
            border: 2px solid #E2E8F0;
            border-radius: 8px;
            padding: 16px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .interview-type-card:hover {
            border-color: #0055B8;
        }

        .interview-type-card.selected {
            border-color: #0055B8;
            background: #F2F7FB;
        }
    </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Header
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 mb-8 text-center'):
            with ui.column().classes('w-full'):
                ui.label('Schedule Interview').classes('heading-2 brand-charcoal mb-4')
                ui.label('Select your preferred interview time and format').classes('body-text brand-slate')

        # Main content
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 gap-8'):
            # Left column - Interview details
            with ui.column().classes('flex-1'):
                # Interview information
                with ui.card().classes('interview-card'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.icon('work', size='2rem').classes('brand-primary')
                        ui.label('Interview Details').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.row().classes('items-center mb-4'):
                        ui.avatar(size='lg').classes('brand-primary-bg mr-4')
                        with ui.column():
                            ui.label('Senior Full Stack Developer').classes('body-text font-semibold brand-charcoal')
                            ui.label('TechStart Solutions').classes('caption brand-slate')
                            ui.label('Application ID: TCA-2024-0847').classes('caption brand-slate')
                    
                    with ui.row().classes('items-center gap-6 mb-4'):
                        with ui.row().classes('items-center'):
                            ui.icon('schedule', size='1rem').classes('brand-slate mr-2')
                            ui.label('Duration: 60 minutes').classes('caption brand-slate')
                        
                        with ui.row().classes('items-center'):
                            ui.icon('person', size='1rem').classes('brand-slate mr-2')
                            ui.label('Interviewer: Jane Doe').classes('caption brand-slate')

                # Interview type selection
                with ui.card().classes('interview-card'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.icon('videocam', size='2rem').classes('brand-primary')
                        ui.label('Interview Format').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.row().classes('gap-4'):
                        # Video interview
                        with ui.element('div').classes('interview-type-card selected flex-1'):
                            with ui.column().classes('text-center'):
                                ui.icon('videocam', size='3rem').classes('brand-primary mb-3')
                                ui.label('Video Interview').classes('body-text font-semibold brand-charcoal mb-2')
                                ui.label('Online video call via platform').classes('caption brand-slate')
                        
                        # Phone interview
                        with ui.element('div').classes('interview-type-card flex-1'):
                            with ui.column().classes('text-center'):
                                ui.icon('phone', size='3rem').classes('brand-slate mb-3')
                                ui.label('Phone Interview').classes('body-text font-semibold brand-charcoal mb-2')
                                ui.label('Traditional phone conversation').classes('caption brand-slate')
                        
                        # In-person interview
                        with ui.element('div').classes('interview-type-card flex-1'):
                            with ui.column().classes('text-center'):
                                ui.icon('business', size='3rem').classes('brand-slate mb-3')
                                ui.label('In-Person').classes('body-text font-semibold brand-charcoal mb-2')
                                ui.label('Meet at company office').classes('caption brand-slate')

                # Calendar selection
                with ui.card().classes('interview-card'):
                    with ui.row().classes('flex items-center justify-between mb-6'):
                        with ui.row().classes('items-center'):
                            ui.icon('calendar_today', size='2rem').classes('brand-primary')
                            ui.label('Select Date').classes('sub-heading brand-charcoal ml-3')
                        
                        with ui.row().classes('gap-2'):
                            ui.button('← Prev').props('flat').classes('brand-primary')
                            ui.label('October 2024').classes('body-text font-semibold brand-charcoal')
                            ui.button('Next →').props('flat').classes('brand-primary')
                    
                    # Mini calendar grid (simplified)
                    with ui.grid(columns=7).classes('gap-1 mb-6'):
                        # Days of week
                        for day in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']:
                            ui.label(day).classes('caption brand-slate text-center font-semibold p-2')
                        
                        # Calendar days (sample)
                        for day in range(1, 32):
                            if day in [15, 16, 17, 22, 23]:  # Available days
                                with ui.element('div').classes('calendar-day has-slots'):
                                    ui.label(str(day)).classes('caption brand-charcoal')
                                    ui.label('●').classes('caption text-green-600 text-center')
                            elif day in [12, 13, 14]:  # Selected day
                                with ui.element('div').classes('calendar-day selected'):
                                    ui.label(str(day)).classes('caption brand-primary font-semibold')
                            else:
                                with ui.element('div').classes('calendar-day'):
                                    ui.label(str(day)).classes('caption brand-slate')

                # Time slot selection
                with ui.card().classes('interview-card'):
                    with ui.row().classes('flex items-center mb-6'):
                        ui.icon('access_time', size='2rem').classes('brand-primary')
                        ui.label('Available Time Slots').classes('sub-heading brand-charcoal ml-3')
                    
                    ui.label('Tuesday, October 15, 2024').classes('body-text font-semibold brand-charcoal mb-4')
                    
                    # Morning slots
                    ui.label('Morning').classes('body-text font-semibold brand-charcoal mb-3')
                    with ui.row().classes('flex-wrap gap-2 mb-6'):
                        morning_slots = ['9:00 AM', '9:30 AM', '10:00 AM', '10:30 AM', '11:00 AM', '11:30 AM']
                        for i, slot in enumerate(morning_slots):
                            if i == 2:  # Selected slot
                                with ui.element('div').classes('time-slot selected'):
                                    ui.label(slot)
                            elif i == 5:  # Unavailable slot
                                with ui.element('div').classes('time-slot unavailable'):
                                    ui.label(slot)
                            else:
                                with ui.element('div').classes('time-slot'):
                                    ui.label(slot)
                    
                    # Afternoon slots
                    ui.label('Afternoon').classes('body-text font-semibold brand-charcoal mb-3')
                    with ui.row().classes('flex-wrap gap-2 mb-6'):
                        afternoon_slots = ['2:00 PM', '2:30 PM', '3:00 PM', '3:30 PM', '4:00 PM', '4:30 PM']
                        for i, slot in enumerate(afternoon_slots):
                            if i in [1, 4]:  # Unavailable slots
                                with ui.element('div').classes('time-slot unavailable'):
                                    ui.label(slot)
                            else:
                                with ui.element('div').classes('time-slot'):
                                    ui.label(slot)

            # Right column - Confirmation details
            with ui.column().classes('w-80'):
                # Selected interview summary
                with ui.card().classes('interview-card'):
                    ui.label('Interview Summary').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.column().classes('gap-3'):
                        with ui.row().classes('items-center'):
                            ui.icon('event', size='1.5rem').classes('brand-slate mr-3')
                            with ui.column():
                                ui.label('Date & Time').classes('caption brand-slate')
                                ui.label('Oct 15, 2024 at 10:00 AM').classes('body-text brand-charcoal')
                        
                        with ui.row().classes('items-center'):
                            ui.icon('videocam', size='1.5rem').classes('brand-slate mr-3')
                            with ui.column():
                                ui.label('Format').classes('caption brand-slate')
                                ui.label('Video Interview').classes('body-text brand-charcoal')
                        
                        with ui.row().classes('items-center'):
                            ui.icon('schedule', size='1.5rem').classes('brand-slate mr-3')
                            with ui.column():
                                ui.label('Duration').classes('caption brand-slate')
                                ui.label('60 minutes').classes('body-text brand-charcoal')
                        
                        with ui.row().classes('items-center'):
                            ui.icon('location_on', size='1.5rem').classes('brand-slate mr-3')
                            with ui.column():
                                ui.label('Platform').classes('caption brand-slate')
                                ui.label('Google Meet').classes('body-text brand-charcoal')

                # Contact information
                with ui.card().classes('interview-card'):
                    ui.label('Interviewer Contact').classes('sub-heading brand-charcoal mb-4')
                    
                    with ui.row().classes('items-center mb-4'):
                        ui.avatar(size='lg').classes('brand-primary-bg mr-4')
                        with ui.column():
                            ui.label('Jane Doe').classes('body-text font-semibold brand-charcoal')
                            ui.label('Senior HR Manager').classes('caption brand-slate')
                    
                    with ui.column().classes('gap-2'):
                        with ui.row().classes('items-center'):
                            ui.icon('email', size='1rem').classes('brand-slate mr-2')
                            ui.label('jane.doe@techstart.co.ke').classes('caption brand-slate')
                        
                        with ui.row().classes('items-center'):
                            ui.icon('phone', size='1rem').classes('brand-slate mr-2')
                            ui.label('+254 712 345 678').classes('caption brand-slate')

                # Preparation tips
                with ui.card().classes('interview-card'):
                    ui.label('Interview Preparation').classes('sub-heading brand-charcoal mb-4')
                    
                    tips = [
                        'Test your internet connection',
                        'Prepare your portfolio and examples',
                        'Review the job description',
                        'Prepare questions about the role',
                        'Have a quiet, well-lit space ready'
                    ]
                    
                    with ui.column().classes('gap-2'):
                        for tip in tips:
                            with ui.row().classes('items-start'):
                                ui.icon('check_circle', size='1rem').classes('text-green-600 mr-2 mt-1')
                                ui.label(tip).classes('caption brand-slate')

                # Reschedule options
                with ui.card().classes('interview-card bg-amber-50 border border-amber-200'):
                    with ui.row().classes('items-center mb-3'):
                        ui.icon('info', size='2rem').classes('text-amber-600')
                        ui.label('Need to Reschedule?').classes('body-text font-semibold text-amber-800 ml-3')
                    
                    ui.label('You can reschedule up to 24 hours before your interview time.').classes('caption text-amber-700 mb-4')
                    
                    ui.button('Reschedule Interview').props('outlined').classes('w-full').style('border-color: #F59E0B; color: #F59E0B; font-family: "Raleway", sans-serif; font-weight: 600;')

        # Confirmation section
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 mt-8'):
            with ui.card().classes('interview-card w-full'):
                ui.label('Additional Information').classes('sub-heading brand-charcoal mb-4')
                
                ui.label('Special Requirements or Notes (Optional)').classes('body-text font-semibold brand-charcoal mb-2')
                ui.textarea('Any specific requirements, accessibility needs, or additional information...').props('outlined rows=3').classes('w-full mb-4')
                
                with ui.row().classes('items-center mb-4'):
                    ui.checkbox('I confirm that I will attend this interview at the scheduled time').classes('mr-3')
                    ui.label('Attendance Confirmation *').classes('body-text brand-charcoal')
                
                with ui.row().classes('items-center'):
                    ui.checkbox('Send me email and SMS reminders before the interview').classes('mr-3')
                    ui.label('Interview Reminders').classes('body-text brand-slate')

        # Action buttons
        with ui.row().classes('w-full max-w-7xl mx-auto px-6 mt-8 mb-12'):
            with ui.row().classes('w-full justify-between items-center'):
                ui.button('← Cancel').props('outlined').classes('px-6 py-3').style('border-color: #EF4444; color: #EF4444; font-family: "Raleway", sans-serif; font-weight: 600;')
                
                with ui.row().classes('gap-3'):
                    ui.button('Save as Draft').props('outlined').classes('px-6 py-3').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                    ui.button('Confirm Interview').classes('px-6 py-3').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')