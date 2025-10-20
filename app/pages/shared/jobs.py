def create_job_card(job: dict):
    """Create a job listing card"""
    with ui.card().classes(
        "p-4 shadow-lg hover:shadow-xl transition-all rounded-xl w-full flex flex-row items-center justify-between gap-4 mb-4"
    ).style(
        "background-color: #FFFFFF !important; border: 2px solid rgba(77, 77, 77, 0.1) !important;"
    ):
        # Job info (left side)
        with ui.row().classes("items-center gap-4 flex-1 min-w-0"):
            # Company logo placeholder
            with ui.card().classes(
                "w-12 h-12 flex items-center justify-center rounded-lg flex-shrink-0"
            ).style("background-color: #0055B8 !important;"):
                ui.label(job["company"][0]).classes(
                    "text-xl font-bold text-white"
                )

            with ui.column().classes("flex-1 min-w-0"):
                ui.label(job["title"]).classes(
                    "sub-heading-2 cursor-pointer transition-all truncate font-bold"
                ).style("color: #1A1A1A !important;")
                ui.label(job["company"]).classes("body-text truncate").style(
                    "color: #4D4D4D !important;"
                )
                if "description" in job:
                    ui.label(job["description"]).classes("body-text mt-1 line-clamp-1 truncate").style("color: #4D4D4D !important;")
                with ui.row().classes("items-center gap-4 mt-1 flex-wrap"):
                    ui.label(job["location"]).classes("caption").style("color: #4D4D4D !important;")
                    ui.label(job["type"]).classes("caption").style("color: #4D4D4D !important;")
                    ui.label(job["posted"]).classes("caption").style("color: #4D4D4D !important;")

        # Actions (right side)
        with ui.row().classes("items-center justify-end gap-3 flex-shrink-0"):
            ui.button(
                "Apply Now", on_click=lambda j=job: apply_job(j["id"])
            ).classes("button-label px-5 py-2 rounded-lg transition-all").style(
                "background-color: #0055B8 !important; color: white !important;"
            )
"""
Jobs page for Dompell Africa
"""

from nicegui import ui
from app.data import SAMPLE_JOBS


def jobs_page():
    """Browse jobs page"""
    ui.add_head_html('''
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <style>
            body { font-family: 'Raleway', sans-serif !important; background: #F2F7FB !important; color: #1A1A1A !important; }
            .jobs-hero {
                background: linear-gradient(135deg, #1A1A1A 0%, #0055B8 100%);
                color: white;
                padding: 64px 20px 48px 20px;
                text-align: center;
                border-radius: 0 0 32px 32px;
                position: relative;
                overflow: hidden;
            }
            .jobs-hero h1 { font-size: 48px; font-weight: 900; margin-bottom: 16px; letter-spacing: -0.02em; }
            .jobs-hero p { font-size: 20px; font-weight: 400; opacity: 0.95; max-width: 700px; margin: 0 auto; }
            .jobs-main { max-width: 1200px; margin: 48px auto 0 auto; padding: 0 20px; }
            @media (max-width: 900px) {
                .jobs-main { padding: 0 8px; }
            }
        </style>
    ''')

    # Hero Section with page title
    ui.html('''
    <section class="jobs-hero">
        <h1>Jobs & Opportunities</h1>
        <p>Discover the latest jobs and career opportunities across Africa. Use filters to find your perfect match and apply instantly.</p>
    </section>
    ''', sanitize=lambda s: s)

    with ui.column().classes("jobs-main"):
        # Modern search and filters
        with ui.card().classes("p-6 mb-8 bg-white shadow-lg rounded-xl border-2 border-slate-100"):
            with ui.row().classes("gap-4 items-center w-full flex-wrap"):
                search_input = ui.input(placeholder="Job Title, Keywords, or Company").classes("flex-1 border-2 rounded-lg").props("outlined")
                location_input = ui.input(placeholder="Location (e.g., Accra, Ghana)").classes("flex-1 border-2 rounded-lg").props("outlined")
                job_type_select = ui.select(["All Types", "Full-time", "Part-time", "Internship", "Contract"], value="All Types").classes("flex-1 min-w-[150px] border-2 rounded-lg").props("outlined dense")
                experience_select = ui.select(["All Levels", "Entry Level", "Mid Level", "Senior Level"], value="All Levels").classes("flex-1 min-w-[150px] border-2 rounded-lg").props("outlined dense")
                remote_select = ui.select(["All", "Remote Only", "On-site Only", "Hybrid"], value="All").classes("flex-1 min-w-[150px] border-2 rounded-lg").props("outlined dense")
                ui.button("Search Jobs", icon="search").classes("px-6 py-3 button-label rounded-lg transition-all").style("background-color: #0055B8 !important; color: white !important;")
        # Results header
        with ui.row().classes("items-center justify-between mb-8"):
            ui.label(f"{len(SAMPLE_JOBS)} jobs found").classes("sub-heading-2 brand-slate")
            with ui.row().classes("items-center gap-3"):
                ui.label("Sort by:").classes("button-label brand-slate")
                sort_select = ui.select(["Most Recent", "Relevance", "Company A-Z"], value="Most Recent").classes("w-40 border-2 rounded-lg").props("outlined dense")
        # Job listings
        with ui.column().classes("gap-4"):
            for job in SAMPLE_JOBS:
                create_job_card(job)


def apply_job(job_id: int):
    """Apply for a job"""
    ui.notify(f"Opening application form for job {job_id}", type="info")