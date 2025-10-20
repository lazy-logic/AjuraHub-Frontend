"""
Company Trainee Feedback System - TalentConnect Africa
Provide feedback and ratings for trainees using brand guidelines.
"""

from nicegui import ui

def company_trainee_feedback_page():
    """Creates the company trainee feedback system page with brand guidelines and icon fixes."""
    
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
        .feedback-card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .rating-star {
            color: #FCD34D;
            cursor: pointer;
            transition: all 0.2s;
        }

        .rating-star:hover {
            color: #F59E0B;
        }

        .rating-star.filled {
            color: #F59E0B;
        }

        .feedback-category {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 16px;
        }

        .performance-meter {
            height: 8px;
            background: #E5E7EB;
            border-radius: 4px;
            overflow: hidden;
        }

        .performance-bar {
            height: 100%;
            transition: width 0.3s ease;
        }

        .performance-excellent { background-color: #10B981; }
        .performance-good { background-color: #3B82F6; }
        .performance-average { background-color: #F59E0B; }
        .performance-poor { background-color: #EF4444; }
    </style>
    ''')

    with ui.column().classes('relative flex h-auto min-h-screen w-full flex-col brand-light-mist pt-20'):
        # Header section
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 mb-8'):
            with ui.row().classes('w-full justify-between items-center'):
                with ui.column():
                    ui.label('Trainee Feedback System').classes('heading-2 brand-charcoal')
                    ui.label('Provide comprehensive feedback and ratings for trainees').classes('body-text brand-slate')
                
                with ui.row().classes('gap-3'):
                    ui.button('View All Feedback').props('outlined').classes('px-4 py-2').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                    ui.button('New Feedback').classes('px-4 py-2').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')

        # Main content
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 gap-8'):
            # Left column - Feedback form
            with ui.column().classes('flex-1'):
                # Trainee selection
                with ui.card().classes('feedback-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Select Trainee').classes('sub-heading brand-charcoal ml-3')
                    
                    ui.select([
                        'Sarah Mwangi - Software Development',
                        'John Kiprotich - Data Science', 
                        'Mary Wanjiku - Digital Marketing',
                        'Peter Ochieng - Cybersecurity'
                    ], value='Sarah Mwangi - Software Development').classes('w-full mb-4')
                    
                    # Trainee preview
                    with ui.row().classes('items-center p-4 bg-gray-50 rounded-lg'):
                        ui.avatar(size='lg').classes('brand-primary-bg mr-4')
                        with ui.column():
                            ui.label('Sarah Mwangi').classes('body-text font-semibold brand-charcoal')
                            ui.label('Software Development • Moringa School').classes('caption brand-slate')
                            ui.label('Training Period: Jan 2024 - Jun 2024').classes('caption brand-slate')

                # Overall rating
                with ui.card().classes('feedback-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Overall Rating').classes('sub-heading brand-charcoal ml-3')
                    
                    with ui.row().classes('items-center gap-4 mb-4'):
                        ui.label('Rate this trainee:').classes('body-text brand-charcoal')
                        # Star rating
                        with ui.row().classes('gap-1'):
                            for i in range(5):

                        ui.label('(5.0)').classes('body-text brand-slate ml-2')
                    
                    ui.textarea('Overall feedback summary...').props('outlined').classes('w-full').props('rows=3')

                # Performance categories
                with ui.card().classes('feedback-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Performance Assessment').classes('sub-heading brand-charcoal ml-3')
                    
                    # Technical skills
                    with ui.element('div').classes('feedback-category'):
                        ui.label('Technical Skills').classes('body-text font-semibold brand-charcoal mb-3')
                        
                        for skill, rating in [
                            ('Programming Proficiency', 85),
                            ('Problem Solving', 90),
                            ('Code Quality', 80),
                            ('Learning Speed', 95)
                        ]:
                            with ui.row().classes('items-center justify-between mb-2'):
                                ui.label(skill).classes('body-text brand-slate')
                                ui.label(f'{rating}%').classes('caption brand-charcoal font-semibold')
                            with ui.element('div').classes('performance-meter mb-3'):
                                ui.element('div').classes(f'performance-bar performance-{"excellent" if rating >= 85 else "good" if rating >= 70 else "average" if rating >= 50 else "poor"}').style(f'width: {rating}%')
                    
                    # Soft skills
                    with ui.element('div').classes('feedback-category'):
                        ui.label('Soft Skills').classes('body-text font-semibold brand-charcoal mb-3')
                        
                        for skill, rating in [
                            ('Communication', 88),
                            ('Teamwork', 92),
                            ('Time Management', 75),
                            ('Adaptability', 85)
                        ]:
                            with ui.row().classes('items-center justify-between mb-2'):
                                ui.label(skill).classes('body-text brand-slate')
                                ui.label(f'{rating}%').classes('caption brand-charcoal font-semibold')
                            with ui.element('div').classes('performance-meter mb-3'):
                                ui.element('div').classes(f'performance-bar performance-{"excellent" if rating >= 85 else "good" if rating >= 70 else "average" if rating >= 50 else "poor"}').style(f'width: {rating}%')

                # Detailed feedback sections
                with ui.card().classes('feedback-card'):
                    with ui.row().classes('flex items-center mb-6'):

                        ui.label('Detailed Feedback').classes('sub-heading brand-charcoal ml-3')
                    
                    ui.label('Strengths').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.textarea('What did this trainee excel at?').props('outlined').classes('w-full mb-4').props('rows=3')
                    
                    ui.label('Areas for Improvement').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.textarea('What areas need development?').props('outlined').classes('w-full mb-4').props('rows=3')
                    
                    ui.label('Specific Examples').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.textarea('Provide specific examples of performance...').props('outlined').classes('w-full mb-4').props('rows=3')
                    
                    ui.label('Recommendations').classes('body-text font-semibold brand-charcoal mb-2')
                    ui.textarea('What would you recommend for this trainee?').props('outlined').classes('w-full').props('rows=3')

            # Right column - Previous feedback & templates
            with ui.column().classes('w-80'):
                # Previous feedback
                with ui.card().classes('feedback-card'):
                    ui.label('Previous Feedback').classes('sub-heading brand-charcoal mb-4')
                    
                    for i in range(3):
                        with ui.card().classes('p-4 mb-3 border'):
                            with ui.row().classes('items-start justify-between mb-2'):
                                ui.label(f'Feedback #{i+1}').classes('body-text font-semibold brand-charcoal')
                                ui.label('Jan 2024').classes('caption brand-slate')
                            
                            with ui.row().classes('items-center mb-2'):
                                # Star rating display
                                with ui.row().classes('gap-1'):
                                    for j in range(5):
                                        if j < 4:

                                        else:

                                ui.label('4.2').classes('caption brand-slate ml-2')
                            
                            ui.label('Excellent technical skills and great team player...').classes('caption brand-slate')
                            
                            ui.button('View Full').props('flat size=sm').style('color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')

                # Feedback templates
                with ui.card().classes('feedback-card'):
                    ui.label('Quick Templates').classes('sub-heading brand-charcoal mb-4')
                    
                    for template in [
                        'Excellent Performance',
                        'Good with Improvements',
                        'Average Performance',
                        'Needs Significant Work'
                    ]:
                        with ui.row().classes('w-full justify-between items-center p-3 border rounded-lg mb-2 cursor-pointer hover:bg-gray-50'):
                            ui.label(template).classes('body-text brand-slate')


                # Feedback statistics
                with ui.card().classes('feedback-card'):
                    ui.label('Feedback Statistics').classes('sub-heading brand-charcoal mb-4')
                    
                    for stat, value in [
                        ('Total Feedback Given', '47'),
                        ('Average Rating', '4.3'),
                        ('This Month', '8'),
                        ('Response Rate', '94%')
                    ]:
                        with ui.row().classes('w-full justify-between items-center mb-3'):
                            ui.label(stat).classes('body-text brand-slate')
                            ui.label(value).classes('body-text font-semibold brand-charcoal')

        # Action buttons
        with ui.row().classes('w-full max-w-6xl mx-auto px-6 mt-8 mb-12'):
            with ui.row().classes('w-full justify-end gap-3'):
                ui.button('Save as Draft').props('outlined').classes('px-6 py-3').style('border-color: #0055B8; color: #0055B8; font-family: "Raleway", sans-serif; font-weight: 600;')
                ui.button('Submit Feedback').classes('px-6 py-3').style('background-color: #0055B8; color: white; font-family: "Raleway", sans-serif; font-weight: 600;')
