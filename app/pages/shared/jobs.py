"""
Jobs page for TalentConnect Africa
"""

from nicegui import ui
from app.data import SAMPLE_JOBS


def jobs_page():
    """Browse jobs page"""
    ui.add_head_html(
        """
            ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <style>
            /* Brand Typography */
            body {
                font-family: 'Raleway', sans-serif !important;
                background: #F2F7FB !important;
                color: #1A1A1A !important;
                line-height: 125% !important;
            }
            
            /* Typography Hierarchy */
            .heading-1 { font-size: 56px; font-weight: 700; color: #1A1A1A; line-height: 110%; letter-spacing: -0.02em; }
            .heading-2 { font-size: 40px; font-weight: 600; color: #1A1A1A; line-height: 115%; letter-spacing: -0.01em; }
            .heading-3 { font-size: 32px; font-weight: 500; color: #1A1A1A; line-height: 120%; }
            .sub-heading { font-size: 24px; font-weight: 600; color: #1A1A1A; line-height: 125%; }
            .sub-heading-2 { font-size: 18px; font-weight: 600; color: #1A1A1A; line-height: 125%; }
            .body-text { font-size: 16px; font-weight: 400; color: #1A1A1A; line-height: 125%; }
            .button-label { font-size: 14px; font-weight: 600; color: #1A1A1A; line-height: 125%; }
            .form-placeholder { font-size: 14px; font-weight: 500; color: #4D4D4D; line-height: 125%; }
            .caption { font-size: 12px; font-weight: 400; color: #4D4D4D; letter-spacing: 8%; line-height: 125%; }
            
            /* Brand Colors */
            .brand-primary { color: #0055B8 !important; }
            .brand-primary-bg { background-color: #0055B8 !important; }
            .brand-charcoal { color: #1A1A1A !important; }
            .brand-slate { color: #4D4D4D !important; }
            .brand-light-mist { background-color: #F2F7FB !important; }
            
            /* Aggressive Brand Color Enforcement */
                        /* Force brand font family but EXCLUDE icons */
            *:not(.material-icons):not(.q-icon):not([class*="material-icons"]):not(i) {
                font-family: 'Raleway', sans-serif !important;
            }
            
            /* Ensure Material Icons work properly */
            .material-icons, .q-icon, i.material-icons, i[class*="material-icons"] {
                font-family: 'Material Icons' !important;
                font-weight: normal !important;
                font-style: normal !important;
                font-variant: normal !important;
                text-transform: none !important;
                line-height: 1 !important;
                letter-spacing: normal !important;
                word-wrap: normal !important;
                white-space: nowrap !important;
                direction: ltr !important;
                -webkit-font-smoothing: antialiased !important;
                -moz-osx-font-smoothing: grayscale !important;
                -webkit-font-feature-settings: 'liga' !important;
            }
            
            /* Force all blue colors to brand primary */
            [class*="text-blue"], [class*="bg-blue"], [class*="border-blue"],
            .bg-blue-50, .text-blue-700, .border-primary { 
                color: #0055B8 !important; 
                background-color: rgba(0, 85, 184, 0.1) !important;
                border-color: #0055B8 !important;
            }
            
            /* Force all gray colors to brand slate */
            [class*="text-gray"], [class*="text-slate"], .text-slate-400,
            .text-gray-600, .text-gray-800 {
                color: #4D4D4D !important;
            }
            
            /* Force dark colors to charcoal */
            h1, h2, h3, h4, h5, h6, .text-gray-800, .text-black {
                color: #1A1A1A !important;
            }
            
            /* Background colors */
            [class*="bg-gray"], [class*="bg-slate"], .bg-slate-50, .bg-slate-100 {
                background-color: #F2F7FB !important;
            }
            
            .bg-white { background-color: #FFFFFF !important; }
            body, .min-h-screen { background-color: #F2F7FB !important; }
            
            /* Border colors */
            [class*="border-gray"], [class*="border-slate"], .border-slate-100, .border-slate-200 {
                border-color: rgba(77, 77, 77, 0.2) !important;
            }
            
            /* Button styling */
            .q-btn:not([class*="outline"]) { background-color: #0055B8 !important; color: white !important; }
            .q-btn--outline, [class*="outline"] { border-color: #0055B8 !important; color: #0055B8 !important; background-color: transparent !important; }
        </style>
    """
    )

    with ui.column().classes("min-h-screen brand-light-mist pt-20 py-8"):
        with ui.column().classes("max-w-7xl mx-auto px-4"):
            # Page header
            with ui.row().classes("items-center justify-between mb-8 flex-wrap gap-4"):
                with ui.column():
                    ui.label("Browse Jobs").classes("heading-2 brand-charcoal")
                    ui.label("Find your next opportunity across Africa").classes(
                        "sub-heading-2 brand-slate"
                    )

                ui.button("Create Job Alert", icon="notifications_active").props(
                    "outline"
                ).classes("button-label rounded-lg transition-all px-6 py-3").style(
                    "border: 2px solid #0055B8 !important; color: #0055B8 !important; background: transparent !important;"
                )

            # Search and filters
            with ui.card().classes(
                "p-8 mb-8 bg-white shadow-lg rounded-xl border-2 border-slate-100"
            ):
                with ui.column().classes("gap-6 w-full"):
                    # Main search
                    with ui.row().classes("gap-6 items-end w-full"):
                        with ui.column().classes("flex-1"):
                            ui.label("Job Title or Keywords").classes(
                                "button-label brand-charcoal mb-2"
                            )
                            search_input = (
                                ui.input(
                                    placeholder="e.g., Software Developer, Data Analyst"
                                )
                                .classes("w-full border-2 rounded-lg")
                                .props("outlined")
                            )

                        with ui.column().classes("flex-1"):
                            ui.label("Location").classes(
                                "button-label brand-charcoal mb-2"
                            )
                            location_input = (
                                ui.input(placeholder="City or Country")
                                .classes("w-full border-2 rounded-lg")
                                .props("outlined")
                            )

                        ui.button("Search Jobs", icon="search").classes(
                            "px-8 py-3 button-label rounded-lg transition-all"
                        ).style(
                            "background-color: #0055B8 !important; color: white !important;"
                        )

                    # Filters
                    with ui.row().classes("gap-6 flex-wrap"):
                        with ui.column().classes("flex-1 min-w-[200px]"):
                            ui.label("Job Type").classes(
                                "button-label brand-charcoal mb-2"
                            )
                            job_type_select = (
                                ui.select(
                                    [
                                        "All Types",
                                        "Full-time",
                                        "Part-time",
                                        "Internship",
                                        "Contract",
                                    ],
                                    value="All Types",
                                )
                                .classes("w-full border-2 rounded-lg")
                                .props("outlined")
                            )

                        with ui.column().classes("flex-1 min-w-[200px]"):
                            ui.label("Experience Level").classes(
                                "button-label brand-charcoal mb-2"
                            )
                            experience_select = (
                                ui.select(
                                    [
                                        "All Levels",
                                        "Entry Level",
                                        "Mid Level",
                                        "Senior Level",
                                    ],
                                    value="All Levels",
                                )
                                .classes("w-full border-2 rounded-lg")
                                .props("outlined")
                            )

                        with ui.column().classes("flex-1 min-w-[200px]"):
                            ui.label("Remote").classes(
                                "button-label brand-charcoal mb-2"
                            )
                            remote_select = (
                                ui.select(
                                    ["All", "Remote Only", "On-site Only", "Hybrid"],
                                    value="All",
                                )
                                .classes("w-full border-2 rounded-lg")
                                .props("outlined")
                            )

            # Results header
            with ui.row().classes("items-center justify-between mb-8"):
                ui.label(f"{len(SAMPLE_JOBS)} jobs found").classes(
                    "sub-heading-2 brand-slate"
                )

                with ui.row().classes("items-center gap-3"):
                    ui.label("Sort by:").classes("button-label brand-slate")
                    sort_select = (
                        ui.select(
                            ["Most Recent", "Relevance", "Company A-Z"],
                            value="Most Recent",
                        )
                        .classes("w-40 border-2 rounded-lg")
                        .props("outlined dense")
                    )

            # Job listings
            with ui.column().classes("gap-4"):
                for job in SAMPLE_JOBS:
                    create_job_card(job)


def create_job_card(job: dict):
    """Create a job listing card"""
    with ui.card().classes(
        "p-8 shadow-lg hover:shadow-xl transition-all rounded-xl w-full"
    ).style(
        "background-color: #FFFFFF !important; border: 2px solid rgba(77, 77, 77, 0.1) !important;"
    ):
        with ui.row().classes("items-start justify-between gap-4"):
            # Job info
            with ui.column().classes("flex-1"):
                with ui.row().classes("items-start gap-4"):
                    # Company logo placeholder
                    with ui.card().classes(
                        "w-16 h-16 flex items-center justify-center rounded-xl"
                    ).style("background-color: #0055B8 !important;"):
                        ui.label(job["company"][0]).classes(
                            "text-2xl font-bold text-white"
                        )

                    with ui.column().classes("flex-1"):
                        ui.label(job["title"]).classes(
                            "sub-heading cursor-pointer transition-all"
                        ).style("color: #1A1A1A !important;")
                        ui.label(job["company"]).classes("sub-heading-2").style(
                            "color: #4D4D4D !important;"
                        )

                        with ui.row().classes("items-center gap-6 mt-3 flex-wrap"):
                            with ui.row().classes(
                                "items-center gap-2 button-label"
                            ).style("color: #4D4D4D !important;"):
                                ui.icon("location_on", size="sm").style(
                                    "color: #4D4D4D !important;"
                                )
                                ui.label(job["location"])

                            with ui.row().classes(
                                "items-center gap-2 button-label"
                            ).style("color: #4D4D4D !important;"):
                                ui.icon("work", size="sm").style(
                                    "color: #4D4D4D !important;"
                                )
                                ui.label(job["type"])

                            with ui.row().classes(
                                "items-center gap-2 button-label"
                            ).style("color: #4D4D4D !important;"):
                                ui.icon("schedule", size="sm").style(
                                    "color: #4D4D4D !important;"
                                )
                                ui.label(job["posted"])

                        # Description
                        if "description" in job:
                            ui.label(job["description"]).classes(
                                "body-text mt-4"
                            ).style("color: #4D4D4D !important;")

                        # Skills
                        with ui.row().classes("gap-2 mt-4 flex-wrap"):
                            for skill in job["skills"]:
                                ui.chip(skill).classes(
                                    "caption font-semibold rounded-lg px-3 py-1"
                                ).style(
                                    "background-color: rgba(0, 85, 184, 0.1) !important; color: #0055B8 !important;"
                                )

            # Actions
            with ui.column().classes("gap-3 items-end"):
                ui.button(
                    "Apply Now", icon="send", on_click=lambda j=job: apply_job(j["id"])
                ).classes("button-label px-6 py-3 rounded-lg transition-all").style(
                    "background-color: #0055B8 !important; color: white !important;"
                )
                ui.button(icon="bookmark_border").props("flat round").classes(
                    "transition-all p-2"
                ).style("color: #4D4D4D !important;").tooltip("Save job")
                ui.button(icon="share").props("flat round").classes(
                    "transition-all p-2"
                ).style("color: #4D4D4D !important;").tooltip("Share job")


def apply_job(job_id: int):
    """Apply for a job"""
    ui.notify(f"Opening application form for job {job_id}", type="info")
