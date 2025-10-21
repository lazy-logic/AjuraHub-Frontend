"""
Immersion Experience Feedback - Dompell Africa
Experience feedback system with rating forms, detailed assessments, and feedback tracking using brand guidelines.
"""

from nicegui import ui

def immersion_experience_feedback_page():
    """Creates the immersion experience feedback page with brand guidelines and icon fixes."""
    
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
        .feedback-card {
            background: white;
            border-radius: 12px;
            border: 1px solid #E5E7EB;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .rating-container {
            display: flex;
            gap: 8px;
            align-items: center;
        }
        
        .star-rating {
            color: #FFA500;
            cursor: pointer;
            font-size: 24px;
        }
        
        .star-rating.inactive {
            color: #D1D5DB;
        }
        
        .progress-ring {
            transform: rotate(-90deg);
        }
        
        .feedback-section {
            border-left: 4px solid #0055B8;
            background: #F8FAFC;
        }
    </style>
    ''')
    
    # Outer page container with top spacing
    with ui.column().classes('min-h-screen w-full flex-col brand-light-mist pt-20'):
        with ui.column().classes('w-full max-w-7xl mx-auto p-6'):
            # Header section
            # Header
            with ui.row().classes('w-full max-w-6xl mx-auto px-6 mb-8'):
                with ui.row().classes('w-full items-center justify-between'):
                    with ui.column():
                        ui.html('<h1 class="heading-2 brand-charcoal mb-2">Immersion Experience Feedback</h1>')
                        ui.html('<p class="body-text brand-slate">Share your immersion experience and provide valuable feedback</p>')
                
                with ui.button('View Previous Feedback', icon='history').classes('bg-blue-600 text-white px-6 py-3'):
                    pass

        # Main content
        with ui.column().classes('w-full max-w-6xl mx-auto px-6'):
            # Experience overview card
            with ui.card().classes('w-full mb-6 feedback-card'):
                with ui.card_section().classes('p-6'):
                    with ui.row().classes('w-full items-center justify-between mb-4'):
                        ui.html('<h2 class="sub-heading brand-charcoal">Current Immersion Program</h2>')
                        ui.chip('In Progress', color='green').classes('text-white')
                    
                    with ui.grid(columns=3).classes('gap-6 mb-6'):
                        # Program info
                        with ui.column():
                            ui.html('<div class="caption brand-slate mb-1">Program</div>')
                            ui.html('<div class="body-text brand-charcoal font-medium">Software Development Bootcamp</div>')
                        
                        with ui.column():
                            ui.html('<div class="caption brand-slate mb-1">Company</div>')
                            ui.html('<div class="body-text brand-charcoal font-medium">TechCorp Solutions</div>')
                        
                        with ui.column():
                            ui.html('<div class="caption brand-slate mb-1">Duration</div>')
                            ui.html('<div class="body-text brand-charcoal font-medium">3 months (Week 8/12)</div>')
                    
                    # Progress indicator
                    with ui.row().classes('w-full items-center gap-4'):
                        ui.html('<div class="body-text brand-slate">Overall Progress:</div>')
                        ui.linear_progress(0.67).classes('flex-grow')
                        ui.html('<div class="body-text brand-primary font-medium">67%</div>')
        
        # Feedback sections
        with ui.row().classes('w-full gap-6'):
            # Main feedback form
            with ui.column().classes('flex-grow'):
                # Overall experience rating
                with ui.card().classes('w-full mb-6 feedback-card'):
                    with ui.card_section().classes('p-6 feedback-section'):
                        ui.html('<h3 class="sub-heading brand-charcoal mb-4">Overall Experience Rating</h3>')
                        
                        with ui.column().classes('space-y-4'):
                            # Star rating
                            with ui.row().classes('items-center gap-4 mb-4'):
                                ui.html('<div class="body-text brand-slate">Rate your experience:</div>')
                                with ui.row().classes('rating-container'):
                                    for i in range(5):
                                        star_class = 'star-rating' if i < 4 else 'star-rating inactive'
                                        ui.html(f'<i class="material-icons {star_class}">star</i>')
                                ui.html('<div class="body-text brand-primary font-medium">4.0/5.0</div>')
                            
                            # Quick feedback options
                            ui.html('<div class="body-text brand-slate mb-3">What stood out the most?</div>')
                            with ui.row().classes('flex-wrap gap-2'):
                                feedback_options = [
                                    'Excellent mentorship', 'Great team culture', 'Challenging projects',
                                    'Good work-life balance', 'Clear expectations', 'Supportive environment'
                                ]
                                for option in feedback_options:
                                    with ui.button(option, icon='check_circle').classes('bg-gray-100 text-gray-700 px-4 py-2 text-sm'):
                                        pass
                
                # Detailed feedback sections
                feedback_categories = [
                    {
                        'title': 'Learning & Development',
                        'icon': 'school',
                        'questions': [
                            'How well did the program meet your learning objectives?',
                            'Rate the quality of training materials and resources',
                            'How effective was the mentorship and guidance?'
                        ]
                    },
                    {
                        'title': 'Work Environment',
                        'icon': 'business',
                        'questions': [
                            'How would you rate the team collaboration?',
                            'Was the work environment inclusive and supportive?',
                            'How clear were project requirements and expectations?'
                        ]
                    },
                    {
                        'title': 'Skills & Growth',
                        'icon': 'trending_up',
                        'questions': [
                            'Which skills did you develop most during this immersion?',
                            'How challenging were the assigned projects?',
                            'What areas do you feel need more development?'
                        ]
                    }
                ]
                
                for category in feedback_categories:
                    with ui.card().classes('w-full mb-6 feedback-card'):
                        with ui.card_section().classes('p-6'):
                            with ui.row().classes('items-center gap-3 mb-4'):

                                ui.html(f'<h3 class="sub-heading brand-charcoal">{category["title"]}</h3>')
                            
                            for question in category['questions']:
                                with ui.column().classes('mb-4'):
                                    ui.html(f'<div class="body-text brand-slate mb-2">{question}</div>')
                                    with ui.row().classes('rating-container mb-2'):
                                        for i in range(5):
                                            star_class = 'star-rating' if i < 3 else 'star-rating inactive'
                                            ui.html(f'<i class="material-icons {star_class}" style="font-size: 20px;">star</i>')
                                    ui.textarea(placeholder='Add specific feedback or comments...').classes('w-full')
            
            # Sidebar with feedback summary
            with ui.column().classes('w-80'):
                # Feedback summary
                with ui.card().classes('w-full mb-6 feedback-card'):
                    with ui.card_section().classes('p-6'):
                        ui.html('<h3 class="sub-heading brand-charcoal mb-4">Feedback Summary</h3>')
                        
                        # Rating breakdown
                        rating_items = [
                            ('Overall Experience', 4.0, '#10B981'),
                            ('Learning Quality', 4.2, '#3B82F6'),
                            ('Mentorship', 3.8, '#8B5CF6'),
                            ('Work Environment', 4.5, '#F59E0B'),
                            ('Skill Development', 4.1, '#EF4444')
                        ]
                        
                        for item, rating, color in rating_items:
                            with ui.row().classes('w-full items-center justify-between mb-3'):
                                ui.html(f'<div class="caption brand-slate">{item}</div>')
                                ui.html(f'<div class="caption font-medium" style="color: {color};">{rating}/5.0</div>')
                
                # Previous feedback
                with ui.card().classes('w-full mb-6 feedback-card'):
                    with ui.card_section().classes('p-6'):
                        ui.html('<h3 class="sub-heading brand-charcoal mb-4">Previous Feedback</h3>')
                        
                        feedback_history = [
                            {'week': 'Week 6', 'rating': 3.8, 'date': 'Oct 1, 2025'},
                            {'week': 'Week 4', 'rating': 3.5, 'date': 'Sep 15, 2025'},
                            {'week': 'Week 2', 'rating': 3.2, 'date': 'Sep 1, 2025'}
                        ]
                        
                        for feedback in feedback_history:
                            with ui.row().classes('w-full items-center justify-between mb-3 p-3 bg-gray-50 rounded-lg'):
                                with ui.column():
                                    ui.html(f'<div class="body-text brand-charcoal font-medium">{feedback["week"]}</div>')
                                    ui.html(f'<div class="caption brand-slate">{feedback["date"]}</div>')
                                ui.html(f'<div class="caption brand-primary font-medium">{feedback["rating"]}/5</div>')
                
                # Action buttons
                with ui.column().classes('w-full space-y-3'):
                    ui.button('Submit Feedback', icon='send').classes('w-full bg-blue-600 text-white py-3')
                    ui.button('Save as Draft', icon='save').classes('w-full bg-gray-200 text-gray-700 py-3')
                    ui.button('Schedule Follow-up', icon='schedule').classes('w-full bg-green-600 text-white py-3')

# Export the page function
__all__ = ['immersion_experience_feedback_page']