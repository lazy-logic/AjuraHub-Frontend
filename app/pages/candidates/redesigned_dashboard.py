"""
Candidate dashboard backed entirely by live Dompell API data.
"""

from __future__ import annotations

import asyncio
from typing import Any, Dict, List, Optional, Tuple

from nicegui import ui, app

from app.components.footer import footer
from app.components.header import header
from app.services.api_service import api_service
from app.services.auth_utils import get_current_user, is_authenticated, logout

StatsMap = Dict[str, ui.label]
SectionContainers = Dict[str, ui.column]


def redesigned_candidate_dashboard() -> None:
    """Render the candidate dashboard using real backend data."""

    if not is_authenticated():
        ui.notify('Please login to access the dashboard', type='negative')
        ui.navigate.to('/login')
        return

    user = get_current_user() or {}
    user_id = user.get('id') or user.get('_id')
    if not user_id:
        ui.notify('Unable to determine your account. Please log in again.', type='negative')
        ui.navigate.to('/login')
        return

    token = app.storage.user.get('token')
    if token:
        api_service.set_auth_token(token)

    header('/candidates/dashboard')
    _inject_styles()

    stats_labels: StatsMap = {}
    section_containers: SectionContainers = {}

    with ui.column().classes('dashboard-wrapper min-h-screen pb-16'):
        _render_top_bar(user)
        with ui.column().classes('max-w-6xl mx-auto px-4 md:px-8 pt-10 pb-16 gap-8'):
            stats_labels = _render_stats_row()
            section_containers = _render_core_sections()

    async def load_data() -> None:
        profile_payload = await _fetch_user_profile(user_id)
        if not profile_payload:
            ui.notify('Unable to load your profile data.', type='negative')
            return

        trainee_profile = profile_payload.get('traineeProfile') or {}
        trainee_id = _extract_profile_id(trainee_profile)

        experiences: List[Dict[str, Any]] = []
        education: List[Dict[str, Any]] = []
        certifications: List[Dict[str, Any]] = []
        portfolio: List[Dict[str, Any]] = []
        applications: List[Dict[str, Any]] = _ensure_list(
            trainee_profile.get('applications')
            or trainee_profile.get('jobApplications')
            or []
        )

        if trainee_id:
            experiences = await _fetch_collection(
                lambda: api_service.get_trainee_experience(trainee_id)
            )
            education = await _fetch_collection(
                lambda: api_service.get_trainee_education(trainee_id)
            )
            certifications = await _fetch_collection(
                lambda: api_service.get_trainee_certifications(trainee_id)
            )
            portfolio = await _fetch_collection(
                lambda: api_service.get_trainee_portfolio(trainee_id)
            )

        stats_data = _build_stats_snapshot(
            trainee_profile=trainee_profile,
            experiences=experiences,
            education=education,
            certifications=certifications,
            applications=applications,
        )

        _update_stats_cards(stats_labels, stats_data)
        _populate_section(section_containers['applications'], applications, _render_application_row,
                          empty_message='No applications found yet.')
        _populate_section(section_containers['experience'], experiences, _render_experience_row,
                          empty_message='Add your first experience to showcase your work history.')
        _populate_section(section_containers['education'], education, _render_education_row,
                          empty_message='Education records will appear here once added.')
        _populate_section(section_containers['certifications'], certifications, _render_certification_row,
                          empty_message='Upload certifications to highlight your achievements.')
        _populate_section(section_containers['portfolio'], portfolio, _render_portfolio_row,
                          empty_message='Share portfolio projects to stand out to employers.')

    ui.timer(0.1, lambda: asyncio.create_task(load_data()), once=True)
    footer()


# ---------------------------------------------------------------------------
# Rendering helpers
# ---------------------------------------------------------------------------

def _inject_styles() -> None:
    ui.add_head_html(
        '''
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            * { font-family: 'Raleway', sans-serif; }
            .dashboard-wrapper { background: linear-gradient(135deg, #f5f7fa 0%, #e4e9f2 100%); }
            .stat-card {
                background: white;
                border-radius: 16px;
                padding: 20px 24px;
                box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08);
                position: relative;
                overflow: hidden;
            }
            .stat-card::after {
                content: '';
                position: absolute;
                right: -40px;
                top: -40px;
                width: 120px;
                height: 120px;
                background: rgba(0, 85, 184, 0.08);
                border-radius: 50%;
            }
            .section-card {
                background: white;
                border-radius: 16px;
                padding: 24px;
                box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06);
            }
            .section-title {
                font-size: 22px;
                font-weight: 700;
                color: #1a1a1a;
            }
            .empty-state {
                background: rgba(0, 85, 184, 0.05);
                border-radius: 12px;
                padding: 16px;
                color: #1a3a5f;
                font-size: 15px;
            }
            .list-row {
                border: 1px solid rgba(15, 23, 42, 0.08);
                border-radius: 12px;
                padding: 16px;
                background: white;
                transition: border-color 0.2s ease, box-shadow 0.2s ease;
            }
            .list-row:hover {
                border-color: rgba(0, 85, 184, 0.35);
                box-shadow: 0 12px 20px rgba(15, 23, 42, 0.08);
            }
            .logout-button {
                color: #ef4444;
                font-weight: 600;
            }
        </style>
        '''
    )


def _render_top_bar(user: Dict[str, Any]) -> None:
    with ui.row().classes('w-full bg-white shadow-md px-4 md:px-16 py-6 justify-between items-center'):
        with ui.column().classes('gap-1'):
            ui.label(f"Welcome back, {user.get('name', 'Candidate')}!").classes('text-2xl font-bold text-gray-900')
            ui.label('Here is the latest snapshot of your career journey.').classes('text-sm text-gray-500')
        ui.button('Logout', icon='logout', on_click=logout).classes('logout-button').props('flat')


def _render_stats_row() -> StatsMap:
    stats_labels: StatsMap = {}
    with ui.row().classes('grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4'):
        for key, title in [
            ('applications', 'Applications Submitted'),
            ('experience', 'Experience Records'),
            ('education', 'Education Entries'),
            ('profile', 'Profile Completion'),
        ]:
            with ui.card().classes('stat-card'):
                ui.label(title).classes('text-sm text-gray-500')
                value_label = ui.label('--').classes('text-3xl font-bold text-gray-900 mt-2')
                stats_labels[key] = value_label
    return stats_labels


def _render_core_sections() -> SectionContainers:
    containers: SectionContainers = {}
    with ui.column().classes('gap-6'):
        with ui.row().classes('grid grid-cols-1 lg:grid-cols-2 gap-6'):
            with ui.card().classes('section-card'):
                ui.label('Recent Applications').classes('section-title mb-4')
                containers['applications'] = ui.column().classes('gap-3')

            with ui.card().classes('section-card'):
                ui.label('Experience').classes('section-title mb-4')
                containers['experience'] = ui.column().classes('gap-3')

        with ui.row().classes('grid grid-cols-1 lg:grid-cols-2 gap-6'):
            with ui.card().classes('section-card'):
                ui.label('Education').classes('section-title mb-4')
                containers['education'] = ui.column().classes('gap-3')

            with ui.card().classes('section-card'):
                ui.label('Certifications').classes('section-title mb-4')
                containers['certifications'] = ui.column().classes('gap-3')

        with ui.card().classes('section-card'):
            ui.label('Portfolio Projects').classes('section-title mb-4')
            containers['portfolio'] = ui.column().classes('gap-3')
    return containers


# ---------------------------------------------------------------------------
# Data fetching and processing
# ---------------------------------------------------------------------------

async def _fetch_user_profile(user_id: str) -> Dict[str, Any]:
    def request():
        return api_service._make_request('GET', f'/users/{user_id}')

    response = await asyncio.to_thread(request)
    return _extract_data_dict(response)


async def _fetch_collection(requester) -> List[Dict[str, Any]]:
    response = await asyncio.to_thread(requester)
    return _extract_data_list(response)


def _extract_profile_id(profile: Dict[str, Any]) -> Optional[str]:
    for key in ('id', '_id', 'profileId', 'traineeProfileId'):
        value = profile.get(key)
        if isinstance(value, str) and value:
            return value
    return None


def _build_stats_snapshot(*, trainee_profile: Dict[str, Any],
                          experiences: List[Dict[str, Any]],
                          education: List[Dict[str, Any]],
                          certifications: List[Dict[str, Any]],
                          applications: List[Dict[str, Any]]) -> Dict[str, Any]:
    profile_completion = _calculate_profile_completeness(trainee_profile)
    return {
        'applications': len(applications),
        'experience': len(experiences),
        'education': len(education),
        'profile': f'{int(profile_completion * 100)}%',
    }


def _calculate_profile_completeness(trainee_profile: Dict[str, Any]) -> float:
    sections = {
        'bio': trainee_profile.get('bio'),
        'skills': trainee_profile.get('skills'),
        'experience': trainee_profile.get('experience'),
        'education': trainee_profile.get('education'),
        'cvUrl': trainee_profile.get('cvUrl'),
        'portfolio': trainee_profile.get('portfolio'),
    }
    total = len(sections)
    if total == 0:
        return 0.0
    completed = sum(1 for value in sections.values() if value)
    return completed / total


# ---------------------------------------------------------------------------
# UI update helpers
# ---------------------------------------------------------------------------

def _update_stats_cards(stats_labels: StatsMap, stats_data: Dict[str, Any]) -> None:
    for key, label in stats_labels.items():
        value = stats_data.get(key, '--')
        label.text = str(value)


def _populate_section(container: ui.column,
                      items: List[Dict[str, Any]],
                      row_renderer,
                      empty_message: str) -> None:
    container.clear()
    if not items:
        with container:
            ui.label(empty_message).classes('empty-state')
        return

    for item in items:
        with container:
            row_renderer(item)


def _render_application_row(item: Dict[str, Any]) -> None:
    title = _select_first(item, ['jobTitle', 'title', 'role'], default='Application')
    company = _select_first(item, ['companyName', 'company', 'employer'], default='Unknown company')
    status = _select_first(item, ['status', 'applicationStatus'], default='Pending')
    updated = _select_first(item, ['updatedAt', 'submittedAt', 'createdAt'], default='')

    with ui.row().classes('list-row justify-between items-start gap-4'):
        with ui.column().classes('gap-1 flex-1'):
            ui.label(title).classes('text-base font-semibold text-gray-800')
            ui.label(company).classes('text-sm text-gray-500')
            if updated:
                ui.label(f'Updated: {updated}').classes('text-xs text-gray-400')
        ui.label(status.title()).classes('px-3 py-1 text-xs font-semibold rounded-full bg-blue-50 text-blue-700')


def _render_experience_row(item: Dict[str, Any]) -> None:
    role = _select_first(item, ['role', 'title', 'position'], default='Experience')
    company = _select_first(item, ['companyName', 'company'], default='')
    duration = _format_duration(item)
    summary = item.get('description') or item.get('summary') or ''

    with ui.column().classes('list-row gap-2'):
        ui.label(role).classes('text-base font-semibold text-gray-800')
        if company or duration:
            ui.label(' • '.join(filter(None, [company, duration]))).classes('text-sm text-gray-500')
        if summary:
            ui.label(summary).classes('text-sm text-gray-600')


def _render_education_row(item: Dict[str, Any]) -> None:
    school = _select_first(item, ['institution', 'school', 'university'], default='Education')
    degree = _select_first(item, ['degree', 'qualification'], default='')
    duration = _format_duration(item)

    with ui.column().classes('list-row gap-2'):
        ui.label(school).classes('text-base font-semibold text-gray-800')
        if degree:
            ui.label(degree).classes('text-sm text-gray-500')
        if duration:
            ui.label(duration).classes('text-xs text-gray-400')


def _render_certification_row(item: Dict[str, Any]) -> None:
    title = _select_first(item, ['title', 'name'], default='Certification')
    issuer = _select_first(item, ['issuer', 'organization'], default='')
    year = _select_first(item, ['year', 'issuedAt'], default='')

    with ui.column().classes('list-row gap-2'):
        ui.label(title).classes('text-base font-semibold text-gray-800')
        if issuer or year:
            ui.label(' • '.join(filter(None, [issuer, year]))).classes('text-sm text-gray-500')


def _render_portfolio_row(item: Dict[str, Any]) -> None:
    title = _select_first(item, ['title', 'name'], default='Project')
    summary = _select_first(item, ['description', 'summary'], default='')
    link = _select_first(item, ['url', 'link', 'projectUrl'], default='')

    with ui.column().classes('list-row gap-2'):
        ui.label(title).classes('text-base font-semibold text-gray-800')
        if summary:
            ui.label(summary).classes('text-sm text-gray-600')
        if link:
            ui.link(link, link).classes('text-xs text-blue-600')


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def _extract_data_dict(response) -> Dict[str, Any]:
    if not response or not getattr(response, 'ok', False):
        _log_response_error(response)
        return {}

    try:
        payload = response.json()
    except Exception as exc:  # noqa: BLE001
        print(f"[DASHBOARD] Failed to parse JSON: {exc}")
        return {}

    if isinstance(payload, dict):
        if isinstance(payload.get('data'), dict):
            return payload['data']
        return payload
    return {}


def _extract_data_list(response) -> List[Dict[str, Any]]:
    if not response or not getattr(response, 'ok', False):
        _log_response_error(response)
        return []

    try:
        payload = response.json()
    except Exception as exc:  # noqa: BLE001
        print(f"[DASHBOARD] Failed to parse list JSON: {exc}")
        return []

    if isinstance(payload, list):
        return payload

    if isinstance(payload, dict):
        for key in ('data', 'items', 'results'):
            value = payload.get(key)
            if isinstance(value, list):
                return value
        if isinstance(payload.get('data'), dict):
            inner = payload['data']
            for key in ('items', 'results'):
                value = inner.get(key)
                if isinstance(value, list):
                    return value
    return []


def _log_response_error(response) -> None:
    if not response:
        print('[DASHBOARD] No response received from API.')
        return
    status = getattr(response, 'status_code', 'unknown')
    try:
        content = response.json()
    except Exception:
        content = getattr(response, 'text', '<unavailable>')
    print(f'[DASHBOARD] API error ({status}): {content}')


def _ensure_list(value: Any) -> List[Dict[str, Any]]:
    if isinstance(value, list):
        return value
    if isinstance(value, dict):
        return [value]
    return []


def _select_first(obj: Dict[str, Any], keys: List[str], default: str = '') -> str:
    for key in keys:
        value = obj.get(key)
        if value:
            return str(value)
    return default


def _format_duration(item: Dict[str, Any]) -> str:
    start = _select_first(item, ['startDate', 'start', 'from'], default='')
    end = _select_first(item, ['endDate', 'end', 'to'], default='Present')
    if not start and not end:
        return ''
    if start and end:
        return f'{start} — {end}'
    return start or end
