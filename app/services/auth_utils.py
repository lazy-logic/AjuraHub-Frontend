"""
Authentication utility functions for checking user status.
"""
from nicegui import app
from app.state import auth_events

def is_authenticated() -> bool:
    """Check if a user is authenticated."""
    return app.storage.user.get('is_authenticated', False)

def get_current_user() -> dict:
    """Get the current authenticated user's data."""
    return app.storage.user.get('user_data', {})

def logout():
    """Log out the current user and clear session."""
    auth_events.trigger('logout')

def get_user_role() -> str:
    """Get the role of the current authenticated user."""
    user = get_current_user()
    return user.get('role') if user else None

def get_user_id() -> str:
    """Get the ID of the current authenticated user."""
    user = get_current_user()
    return user.get('id') if user else None

def has_role(roles) -> bool:
    """Check if the current user has one of the specified roles."""
    user_role = get_user_role()
    if not user_role:
        return False
    if isinstance(roles, str):
        return user_role == roles
    return user_role in roles