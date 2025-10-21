"""
Training Program Directory (Public) - Dompell Africa
Public training directory with program listings, filters, and search functionality using brand guidelines.
"""

from nicegui import ui

def create_program_card(program: dict):
    """Create a training program listing card"""
    with ui.card().classes(
        "p-4 shadow-lg hover:shadow-xl transition-all rounded-xl w-full flex flex-row items-center justify-between gap-4 mb-4"
    ).style(
        "background-color: #FFFFFF !important; border: 2px solid rgba(77, 77, 77, 0.1) !important;"
    ):
        # Program info (left side)
        with ui.row().classes("items-center gap-4 flex-1 min-w-0"):
            # Institution logo placeholder
            with ui.card().classes(
                "w-12 h-12 flex items-center justify-center rounded-lg flex-shrink-0"
            ).style("background-color: #0055B8 !important;"):
                ui.label(program["institution"][0]).classes(
                    "text-xl font-bold text-white"
                )

            with ui.column().classes("flex-1 min-w-0"):
                ui.label(program["title"]).classes(
                    "sub-heading-2 cursor-pointer transition-all truncate font-bold"
                ).style("color: #1A1A1A !important;")
                ui.label(program["institution"]).classes("body-text truncate").style(
                    "color: #4D4D4D !important;"
                )
                if "summary" in program:
                    ui.label(program["summary"]).classes("body-text mt-1 line-clamp-1 truncate").style("color: #4D4D4D !important;")
                with ui.row().classes("items-center gap-4 mt-1 flex-wrap"):
                    ui.label(program["duration"]).classes("caption").style("color: #4D4D4D !important;")
                    ui.label(program["format"]).classes("caption").style("color: #4D4D4D !important;")
                    ui.label(program["level"]).classes("caption").style("color: #4D4D4D !important;")
                    ui.label(program["cost"]).classes("caption font-bold").style("color: #0055B8 !important;")

        # Actions (right side)
        with ui.row().classes("items-center justify-end gap-3 flex-shrink-0"):
            ui.button(
                "Apply Now", on_click=lambda p=program: apply_program(p["title"])
            ).classes("button-label px-5 py-2 rounded-lg transition-all").style(
                "background-color: #0055B8 !important; color: white !important;"
            )

def apply_program(program_title: str):
    """Apply for a training program"""
    ui.notify(f"Opening application form for {program_title}", type="info")

def training_program_directory_page():
    """Creates the public training program directory page with brand guidelines and icon fixes."""
    
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <style>
            body { font-family: 'Raleway', sans-serif !important; background: #F2F7FB !important; color: #1A1A1A !important; }
            .programs-hero {
                background: linear-gradient(135deg, #1A1A1A 0%, #0055B8 100%);
                color: white;
                padding: 64px 20px 48px 20px;
                text-align: center;
                border-radius: 0 0 32px 32px;
                position: relative;
                overflow: hidden;
            }
            .programs-hero::before {
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
            .programs-hero::after {
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
            .programs-hero h1,
            .programs-hero p {
                position: relative;
                z-index: 2;
            }
            .programs-hero h1 { font-size: 48px; font-weight: 900; margin-bottom: 16px; letter-spacing: -0.02em; }
            .programs-hero p { font-size: 20px; font-weight: 400; opacity: 0.95; max-width: 700px; margin: 0 auto; }
            .programs-main { max-width: 1200px; margin: 48px auto 0 auto; padding: 0 20px; }
            @media (max-width: 900px) {
                .programs-main { padding: 0 8px; }
            }
        </style>
    ''')

    # Hero Section with page title
    ui.html('''
    <section class="programs-hero">
        <h1>Training Programs</h1>
        <p>Discover professional training programs from leading institutions across Africa. Filter by type, duration, and level to find your perfect program.</p>
    </section>
    ''')

    with ui.column().classes("programs-main"):
        # Modern search and filters
        with ui.card().classes("p-6 mb-8 bg-white shadow-lg rounded-xl border-2 border-slate-100"):
            with ui.row().classes("gap-4 items-center w-full flex-wrap"):
                search_input = ui.input(placeholder="Program Title, Skills, or Institution").classes("flex-1 border-2 rounded-lg").props("outlined")
                type_select = ui.select(["All Types", "Bootcamp", "Certificate", "Diploma", "Short Course"], value="All Types").classes("flex-1 min-w-[150px] border-2 rounded-lg").props("outlined dense")
                duration_select = ui.select(["All Durations", "Under 1 month", "1-3 months", "3-6 months", "6+ months"], value="All Durations").classes("flex-1 min-w-[150px] border-2 rounded-lg").props("outlined dense")
                level_select = ui.select(["All Levels", "Beginner", "Intermediate", "Advanced"], value="All Levels").classes("flex-1 min-w-[150px] border-2 rounded-lg").props("outlined dense")
                cost_select = ui.select(["All Prices", "Free", "Under $100", "$100-$500", "Over $500"], value="All Prices").classes("flex-1 min-w-[150px] border-2 rounded-lg").props("outlined dense")
                ui.button("Search Programs", icon="search").classes("px-6 py-3 button-label rounded-lg transition-all").style("background-color: #0055B8 !important; color: white !important;")
        
        # Results header
        with ui.row().classes("items-center justify-between mb-8"):
            ui.label("247 programs found").classes("sub-heading-2 brand-slate")
            with ui.row().classes("items-center gap-3"):
                ui.label("Sort by:").classes("button-label brand-slate")
                sort_select = ui.select(["Most Recent", "Relevance", "Institution A-Z", "Price (Low to High)"], value="Most Recent").classes("w-40 border-2 rounded-lg").props("outlined dense")
        
        # Program listings
        programs = [
                {
                    'title': 'Full Stack Web Development Bootcamp',
                    'institution': 'Moringa School',
                    'duration': '15 weeks',
                    'level': 'Beginner',
                    'cost': 'KSh 120,000',
                    'rating': 4.8,
                    'students': 2847,
                    'start_date': 'Jan 15, 2024',
                    'format': 'Hybrid',
                    'technologies': ['HTML/CSS', 'JavaScript', 'React', 'Node.js', 'MongoDB'],
                    'summary': 'An intensive, project-based program covering modern full-stack development with emphasis on practical, job-ready skills.'
                },
                {
                    'title': 'Data Science with Python Certificate',
                    'institution': 'University of Nairobi',
                    'duration': '12 weeks',
                    'level': 'Intermediate',
                    'cost': 'KSh 80,000',
                    'rating': 4.6,
                    'students': 1523,
                    'start_date': 'Feb 1, 2024',
                    'format': 'Online',
                    'technologies': ['Python', 'Pandas', 'Machine Learning', 'SQL'],
                    'summary': 'Hands-on coverage of data analysis, machine learning, and model evaluation using Python and core data science tools.'
                },
                {
                    'title': 'Mobile App Development (Flutter)',
                    'institution': 'ALX Africa',
                    'duration': '8 weeks',
                    'level': 'Beginner',
                    'cost': 'Free',
                    'rating': 4.7,
                    'students': 3241,
                    'start_date': 'Jan 22, 2024',
                    'format': 'Online',
                    'technologies': ['Flutter', 'Dart', 'Firebase', 'API Integration'],
                    'summary': 'Build cross-platform mobile apps with Flutter and Dart, from UI layouts to backend integration and deployment.'
                },
                {
                    'title': 'UI/UX Design Masterclass',
                    'institution': 'Design Institute',
                    'duration': '6 weeks',
                    'level': 'Beginner',
                    'cost': 'KSh 45,000',
                    'rating': 4.9,
                    'students': 897,
                    'start_date': 'Feb 5, 2024',
                    'format': 'Hybrid',
                    'technologies': ['Figma', 'Adobe XD', 'Prototyping', 'User Research'],
                    'summary': 'A practical introduction to product design, user research, wireframing, prototyping, and usability testing.'
                }
            ]

        # Program cards
        with ui.column().classes("gap-4"):
            for program in programs:
                create_program_card(program)