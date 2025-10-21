"""
Candidates Success Stories
Showcase of successful candidates and their career journeys through Dompell Africa.
"""

from nicegui import ui

def create_story_card(story: dict, index: int):
    """Create a large testimonial-style story card"""
    # Alternate background colors
    bg_color = "#FFFFFF" if index % 2 == 0 else "#F8FAFC"
    
    with ui.card().classes("p-8 mb-6 border-l-4").style(
        f"background-color: {bg_color} !important; border-left-color: #0055B8 !important; box-shadow: 0 1px 3px rgba(0,0,0,0.1);"
    ):
        # Quote section - large and prominent
        with ui.column().classes("mb-6"):
            ui.label('"').classes("text-6xl font-bold").style("color: #0055B8 !important; line-height: 0.5; margin-bottom: 8px;")
            if "quote" in story:
                ui.label(story["quote"]).classes("text-xl italic leading-relaxed").style("color: #1A1A1A !important; font-weight: 400;")
        
        # Divider line
        ui.element('div').classes('w-full h-px bg-gray-200 my-6')
        
        # Person info and metrics in two columns
        with ui.row().classes("justify-between items-start gap-8"):
            # Left: Person details
            with ui.column().classes("flex-1"):
                ui.label(story["name"]).classes("text-2xl font-bold mb-2").style("color: #1A1A1A !important;")
                ui.label(story['position']).classes("text-lg mb-1").style("color: #4D4D4D !important;")
                ui.label(story['company']).classes("text-lg font-semibold").style("color: #0055B8 !important;")
            
            # Right: Metrics
            with ui.row().classes("gap-8"):
                if 'duration' in story:
                    with ui.column().classes("text-center"):
                        ui.label(story['duration']).classes("text-3xl font-bold").style("color: #0055B8 !important;")
                        ui.label('Duration').classes("text-sm").style("color: #6B7280 !important;")
                
                if 'salary_increase' in story:
                    with ui.column().classes("text-center"):
                        ui.label(story['salary_increase']).classes("text-3xl font-bold").style("color: #10B981 !important;")
                        ui.label('Salary Increase').classes("text-sm").style("color: #6B7280 !important;")
        
        # Program tag at bottom
        with ui.row().classes("mt-6"):
            ui.label(f"Program: {story['program']}").classes("px-4 py-2").style(
                "background-color: #EBF4FF; color: #0055B8; font-weight: 600; border-radius: 4px;"
            )

def view_story(name: str):
    """View full success story"""
    ui.notify(f"Opening full story for {name}", type="info")

def candidates_success_stories_page():
    """Creates the candidates success stories page."""
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <style>
            body { font-family: 'Raleway', sans-serif !important; background: #F2F7FB !important; color: #1A1A1A !important; }
            .stories-hero {
                background: linear-gradient(135deg, #1A1A1A 0%, #0055B8 100%);
                color: white;
                padding: 64px 20px 48px 20px;
                text-align: center;
                border-radius: 0 0 32px 32px;
                position: relative;
                overflow: hidden;
            }
            .stories-hero::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background-image: 
                    radial-gradient(circle at 20% 50%, rgba(255, 255, 255, 0.1) 1px, transparent 1px),
                    radial-gradient(circle at 80% 80%, rgba(255, 255, 255, 0.1) 1px, transparent 1px),
                    radial-gradient(circle at 40% 20%, rgba(255, 255, 255, 0.08) 2px, transparent 2px);
                background-size: 50px 50px, 80px 80px, 100px 100px;
                background-position: 0 0, 40px 60px, 20px 30px;
                opacity: 0.4;
                z-index: 1;
            }
            .stories-hero::after {
                content: '';
                position: absolute;
                top: -50%;
                right: -10%;
                width: 500px;
                height: 500px;
                background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, transparent 70%);
                border-radius: 50%;
                z-index: 1;
            }
            .stories-hero h1,
            .stories-hero p {
                position: relative;
                z-index: 2;
            }
            .stories-hero h1 { font-size: 56px; font-weight: 900; margin-bottom: 24px; letter-spacing: -0.03em; }
            .stories-hero p { font-size: 22px; font-weight: 400; opacity: 0.95; max-width: 800px; margin: 0 auto; line-height: 1.6; }
            .stories-main { max-width: 1000px; margin: 48px auto 0 auto; padding: 0 20px; }
            @media (max-width: 900px) {
                .stories-main { padding: 0 8px; }
            }
        </style>
    ''')

    # Hero Section
    ui.html('''
    <section class="stories-hero">
        <h1>Real Stories, Real Impact</h1>
        <p>Meet the professionals who transformed their careers through Dompell Africa. Their journeys prove that with the right training and determination, anything is possible.</p>
    </section>
    ''')

    with ui.column().classes("stories-main"):
        # Impact numbers - simple text layout
        with ui.row().classes("justify-between mb-12 py-8 border-y-2").style("border-color: #E5E7EB;"):
            with ui.column().classes("text-center flex-1"):
                ui.label("8,247").classes("text-5xl font-black mb-2").style("color: #1A1A1A !important;")
                ui.label("Candidates Placed").classes("text-sm font-semibold").style("color: #6B7280 !important; text-transform: uppercase; letter-spacing: 0.05em;")
            with ui.column().classes("text-center flex-1"):
                ui.label("92%").classes("text-5xl font-black mb-2").style("color: #1A1A1A !important;")
                ui.label("Success Rate").classes("text-sm font-semibold").style("color: #6B7280 !important; text-transform: uppercase; letter-spacing: 0.05em;")
            with ui.column().classes("text-center flex-1"):
                ui.label("$65K").classes("text-5xl font-black mb-2").style("color: #1A1A1A !important;")
                ui.label("Avg. Salary").classes("text-sm font-semibold").style("color: #6B7280 !important; text-transform: uppercase; letter-spacing: 0.05em;")
            with ui.column().classes("text-center flex-1"):
                ui.label("456").classes("text-5xl font-black mb-2").style("color: #1A1A1A !important;")
                ui.label("Companies").classes("text-sm font-semibold").style("color: #6B7280 !important; text-transform: uppercase; letter-spacing: 0.05em;")
        
        # Simple filter bar
        with ui.row().classes("gap-4 mb-8 pb-6 border-b").style("border-color: #E5E7EB;"):
            ui.label("Filter by:").classes("text-lg font-semibold").style("color: #1A1A1A !important;")
            ui.select(["All Programs", "Software Development", "Data Science", "Digital Marketing", "Cybersecurity", "UI/UX Design"], value="All Programs").classes("flex-1").props("outlined dense")
            ui.select(["All Industries", "Technology", "Finance", "Healthcare", "E-commerce"], value="All Industries").classes("flex-1").props("outlined dense")
        
        # Section heading
        ui.label("Featured Stories").classes("text-4xl font-black mb-8").style("color: #1A1A1A !important;")
        
        # Story cards in 2-column grid
        stories = _get_featured_stories() + _get_all_stories_formatted()
        with ui.element('div').classes('grid grid-cols-1 lg:grid-cols-2 gap-6'):
            for index, story in enumerate(stories):
                create_story_card(story, index)

def _get_all_stories_formatted():
    """Format compact stories to match featured format."""
    compact_stories = _get_all_stories()
    formatted = []
    for story in compact_stories:
        formatted.append({
            'name': story['name'],
            'avatar': story['avatar'],
            'position': story['position'],
            'company': story['company'],
            'program': story['program_short'],
            'quote': story['brief_quote'],
            'duration': story['timeline']
        })
    return formatted

def _get_featured_stories():
    """Returns featured success stories data."""
    return [
        {
            'name': 'Sarah Ochieng',
            'avatar': '👩‍💻',
            'position': 'Senior Software Developer',
            'company': 'Safaricom',
            'program': 'Software Development Bootcamp',
            'quote': 'TalentConnect Africa completely changed my life. I went from working retail to landing my dream job as a software developer at Safaricom. The hands-on training and mentorship were incredible.',
            'duration': '6 months',
            'salary_increase': '400%',
            'skills': ['React', 'Node.js', 'Python', 'AWS', 'Agile', 'Git'],
            'brief_quote': 'TalentConnect Africa completely changed my life'
        },
        {
            'name': 'Michael Adebayo',
            'avatar': '👨‍💼',
            'position': 'Data Scientist',
            'company': 'Flutterwave',
            'program': 'Data Science Intensive',
            'quote': 'The program gave me both technical skills and industry connections. Within 3 months of graduation, I had multiple job offers and chose to join Flutterwave as a Data Scientist.',
            'duration': '8 months',
            'salary_increase': '300%',
            'skills': ['Python', 'Machine Learning', 'SQL', 'Tableau', 'Statistics', 'TensorFlow'],
            'brief_quote': 'The program gave me both technical skills and industry connections'
        }
    ]

def _get_all_stories():
    """Returns all success stories data."""
    return [
        {
            'name': 'Grace Mwangi',
            'avatar': '👩‍🎨',
            'position': 'UX Designer',
            'company': 'Jumia',
            'brief_quote': 'From zero design experience to leading UX projects at Jumia',
            'program_short': 'UI/UX Design',
            'timeline': '4 months'
        },
        {
            'name': 'David Mensah',
            'avatar': '👨‍💻',
            'position': 'Cybersecurity Analyst',
            'company': 'Ecobank',
            'brief_quote': 'Transitioned from IT support to cybersecurity expert',
            'program_short': 'Cybersecurity',
            'timeline': '6 months'
        },
        {
            'name': 'Amina Hassan',
            'avatar': '👩‍💼',
            'position': 'Digital Marketing Manager',
            'company': 'Twiga Foods',
            'brief_quote': 'Built a successful marketing career from scratch',
            'program_short': 'Digital Marketing',
            'timeline': '3 months'
        },
        {
            'name': 'John Kamau',
            'avatar': '👨‍💼',
            'position': 'Full Stack Developer',
            'company': 'iHub',
            'brief_quote': 'From teacher to tech entrepreneur',
            'program_short': 'Full Stack Dev',
            'timeline': '7 months'
        },
        {
            'name': 'Fatima Abdullahi',
            'avatar': '👩‍💻',
            'position': 'Product Manager',
            'company': 'Paystack',
            'brief_quote': 'Leading product development at a fintech unicorn',
            'program_short': 'Product Mgmt',
            'timeline': '5 months'
        },
        {
            'name': 'Peter Tawfik',
            'avatar': '👨‍💼',
            'position': 'Cloud Architect',
            'company': 'Microsoft',
            'brief_quote': 'Achieved cloud expertise and joined Microsoft',
            'program_short': 'Cloud Computing',
            'timeline': '6 months'
        }
    ]
