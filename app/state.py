"""
Global state management for TalentConnect Africa
"""

from nicegui import ui

class AppState:
    """Global application state"""
    def __init__(self):
        self.current_user = None
        self.user_role = None  # 'trainee', 'employer', 'institution', 'admin'
        self.current_page = 'home'
        self.notifications = []
    
    def login(self, email: str, role: str):
        """Login user"""
        self.current_user = email
        self.user_role = role
    
    def logout(self):
        """Logout user"""
        self.current_user = None
        self.user_role = None
        ui.navigate.to('/')
    
    def is_authenticated(self) -> bool:
        """Check if user is authenticated"""
        return self.current_user is not None

# Global state instance
app_state = AppState()
