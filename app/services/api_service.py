"""
API Service for Dompell Africa
This module handles all interactions with the Dompell backend API.
Updated based on API documentation: https://dompell-server.onrender.com/api-docs
"""

import requests
from typing import Dict, Any, Optional, List
from app.config import API_BASE_URL

class ApiService:
    """A service class for handling API requests to the Dompell API."""
    
    def __init__(self):
        self.base_url = API_BASE_URL
        self.session = requests.Session()
        self.token = None  # Initialize token attribute

    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None, 
                     params: Optional[Dict] = None, headers: Optional[Dict] = None,
                     files: Optional[Dict] = None) -> requests.Response:
        """Make a generic API request with error handling."""
        url = f"{self.base_url}{endpoint}"
        
        try:
            if method.upper() == 'GET':
                response = self.session.get(url, params=params, headers=headers)
            elif method.upper() == 'POST':
                if files:
                    response = self.session.post(url, data=data, files=files, headers=headers)
                else:
                    response = self.session.post(url, json=data, headers=headers)
            elif method.upper() == 'PATCH':
                response = self.session.patch(url, json=data, headers=headers)
            elif method.upper() == 'DELETE':
                response = self.session.delete(url, headers=headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
                
            return response
        except requests.RequestException as e:
            print(f"API request error: {e}")
            raise

    # ===== AUTHENTICATION ENDPOINTS =====
    
    def register(self, user_data: Dict[str, Any]) -> requests.Response:
        """
        Register a new user.
        
        Args:
            user_data: RegisterDto containing user registration information
            
        Returns:
            API response
        """
        return self._make_request('POST', '/auth/register', data=user_data)

    def verify_account(self, token: str, code: str) -> requests.Response:
        """
        Verify a user account with verification code.
        
        CORRECT FORMAT (tested and verified):
        - Token is passed as QUERY PARAMETER (not path!)
        - Code is sent as JSON object in body
        
        Args:
            token: JWT registration token from signup
            code: 6-digit verification code
            
        Returns:
            API response
        """
        # CORRECT format: token as query param, code in body
        url = f"{self.base_url}/auth/verify-account?token={token}"
        
        response = self.session.post(
            url,
            json={'code': code},
            headers={'Content-Type': 'application/json'}
        )
        
        return response

    def login(self, email: str, password: str) -> requests.Response:
        """
        Authenticate a user and return login response.

        Args:
            email: The user's email
            password: The user's password

        Returns:
            API response containing authentication token
        """
        payload = {
            "email": email,
            "password": password,
        }
        return self._make_request('POST', '/auth/login', data=payload)

    def forgot_password(self, email: str) -> requests.Response:
        """
        Send password reset code to user email.
        
        Args:
            email: User's email address
            
        Returns:
            API response
        """
        return self._make_request('POST', '/auth/forgot-password', data={"email": email})

    def reset_password(self, reset_data: Dict[str, Any]) -> requests.Response:
        """
        Reset user password using verification code.
        
        Args:
            reset_data: ResetPasswordDto containing email, code, and new password
            
        Returns:
            API response
        """
        return self._make_request('POST', '/auth/reset-password', data=reset_data)

    def resend_code(self, email: str) -> requests.Response:
        """
        Resend verification code to user.
        
        Args:
            email: User's email address
            
        Returns:
            API response
        """
        return self._make_request('POST', '/auth/resend-code', data={"email": email})

    def resend_email(self, email: str) -> requests.Response:
        """
        Resend verification email to user.
        
        Args:
            email: User's email address
            
        Returns:
            API response
        """
        return self._make_request('POST', '/auth/resend-email', data={"email": email})

    def refresh_token(self, refresh_token: str) -> requests.Response:
        """
        Generate a new access token using refresh token.
        
        Args:
            refresh_token: The refresh token
            
        Returns:
            API response with new access token
        """
        return self._make_request('POST', '/auth/refresh-token', 
                                data={"refresh_token": refresh_token})

    # ===== USER ENDPOINTS =====

    def get_all_users(self, params: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        """
        Get all users (admin/authorized access required).
        
        Args:
            params: Query parameters (e.g., pagination, search filters)
            headers: Authorization headers
            
        Returns:
            API response with users list
        """
        return self._make_request('GET', '/users/all', params=params, headers=headers)

    def get_user_profile(self, user_id: str, headers: Optional[Dict] = None) -> requests.Response:
        """
        Get a specific user's profile.
        
        Args:
            user_id: The user's ID
            headers: Authorization headers
            
        Returns:
            API response with user profile
        """
        return self._make_request('GET', f'/users/{user_id}', headers=headers)

    def update_user(self, user_id: str, user_data: Dict[str, Any], 
                   headers: Optional[Dict] = None) -> requests.Response:
        """
        Update a user's information.
        
        Args:
            user_id: The user's ID
            user_data: UserUpdateDto with updated information
            headers: Authorization headers
            
        Returns:
            API response
        """
        return self._make_request('PATCH', f'/users/{user_id}', 
                                data=user_data, headers=headers)

    def delete_user(self, user_id: str, headers: Optional[Dict] = None) -> requests.Response:
        """
        Delete a user.
        
        Args:
            user_id: The user's ID
            headers: Authorization headers
            
        Returns:
            API response
        """
        return self._make_request('DELETE', f'/users/{user_id}', headers=headers)

    # ===== FILE UPLOAD ENDPOINTS =====

    def upload_file(self, file_data: Dict, headers: Optional[Dict] = None) -> requests.Response:
        """
        Upload a file to AWS S3 bucket.
        
        Args:
            file_data: File data and metadata
            headers: Authorization headers
            
        Returns:
            API response with file URL
        """
        return self._make_request('POST', '/upload', files=file_data, headers=headers)

    # ===== ORGANIZATION ENDPOINTS =====

    def create_organization(self, user_id: str, org_data: Dict[str, Any], 
                          headers: Optional[Dict] = None) -> requests.Response:
        """
        Create or update an organization profile.
        
        Args:
            user_id: The user's ID
            org_data: OrganizationProfileDto with organization details
            headers: Authorization headers
            
        Returns:
            API response
        """
        return self._make_request('POST', f'/organization/create/{user_id}', 
                                data=org_data, headers=headers)

    def get_all_organizations(self, params: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        """
        Get all organizations.
        
        Args:
            params: Query parameters (e.g., pagination, filters)
            headers: Authorization headers
            
        Returns:
            API response with organizations list
        """
        return self._make_request('GET', '/organization', params=params, headers=headers)

    def get_organization(self, org_id: str, headers: Optional[Dict] = None) -> requests.Response:
        """
        Get an organization profile.
        
        Args:
            org_id: The organization's ID
            headers: Authorization headers
            
        Returns:
            API response with organization details
        """
        return self._make_request('GET', f'/organization/{org_id}', headers=headers)

    def delete_organization(self, org_id: str, headers: Optional[Dict] = None) -> requests.Response:
        """
        Delete an organization profile.
        
        Args:
            org_id: The organization's ID
            headers: Authorization headers
            
        Returns:
            API response
        """
        return self._make_request('DELETE', f'/organization/{org_id}', headers=headers)

    def get_organization_programs(self, org_id: str, 
                                headers: Optional[Dict] = None) -> requests.Response:
        """
        Get all programs for an organization.
        
        Args:
            org_id: The organization's ID
            headers: Authorization headers
            
        Returns:
            API response with programs list
        """
        return self._make_request('GET', f'/organization/programs/{org_id}', headers=headers)

    # ===== TRAINEE PROFILE ENDPOINTS =====

    def get_trainee_profile_by_user(self, user_id: str, headers: Optional[Dict] = None) -> requests.Response:
        """
        Retrieve a trainee profile using the associated user ID.
        """
        return self._make_request('GET', f'/trainee/{user_id}', headers=headers)

    def get_all_trainees(self, params: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        """Retrieve all trainee profiles."""
        return self._make_request('GET', '/trainee', params=params, headers=headers)

    def get_trainee_experience(self, trainee_profile_id: str,
                               headers: Optional[Dict] = None) -> requests.Response:
        """Retrieve all experience records for a trainee profile."""
        return self._make_request('GET', f'/trainee/experience/{trainee_profile_id}', headers=headers)

    def get_trainee_education(self, trainee_profile_id: str,
                              headers: Optional[Dict] = None) -> requests.Response:
        """Retrieve all education records for a trainee profile."""
        return self._make_request('GET', f'/trainee/education/{trainee_profile_id}', headers=headers)

    def get_trainee_certifications(self, trainee_profile_id: str,
                                   headers: Optional[Dict] = None) -> requests.Response:
        """Retrieve all certifications for a trainee profile."""
        return self._make_request('GET', f'/trainee/certification/{trainee_profile_id}', headers=headers)

    def get_trainee_portfolio(self, trainee_profile_id: str,
                              headers: Optional[Dict] = None) -> requests.Response:
        """Retrieve all portfolio projects for a trainee profile."""
        return self._make_request('GET', f'/trainee/portfolio/{trainee_profile_id}', headers=headers)

    # ===== EMPLOYER ENDPOINTS =====

    def get_all_employers(self, params: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        """Retrieve all employer profiles."""
        return self._make_request('GET', '/employer', params=params, headers=headers)

    # ===== TRAINING PROGRAMS ENDPOINTS =====

    def create_training_program(self, user_id: str, program_data: Dict[str, Any], 
                              headers: Optional[Dict] = None) -> requests.Response:
        """
        Post a new or upcoming training program.
        
        Args:
            user_id: The user's ID (institution owner)
            program_data: CreateTrainingProgramDto with program details
            headers: Authorization headers
            
        Returns:
            API response
        """
        return self._make_request('POST', f'/programs/create/{user_id}', 
                                data=program_data, headers=headers)

    def get_new_programs(self, user_id: str, headers: Optional[Dict] = None) -> requests.Response:
        """
        Get newly created or ongoing training programs for a user.
        
        Args:
            user_id: The user's ID
            headers: Authorization headers
            
        Returns:
            API response with new programs list
        """
        return self._make_request('GET', f'/programs/new/{user_id}', headers=headers)

    def get_upcoming_programs(self, user_id: str, headers: Optional[Dict] = None) -> requests.Response:
        """
        Get upcoming training programs (future start date) for a user.
        
        IMPORTANT: API spec shows '/api/programs/upcoming{userId}' without slash before userId
        
        Args:
            user_id: The user's ID
            headers: Authorization headers
            
        Returns:
            API response with upcoming programs list
        """
        return self._make_request('GET', f'/programs/upcoming{user_id}', headers=headers)

    # ===== UTILITY METHODS =====

    def set_auth_token(self, token: str):
        """
        Set the authorization token for all subsequent requests.
        
        Args:
            token: The JWT token
        """
        self.token = token  # Store token
        self.session.headers.update({'Authorization': f'Bearer {token}'})
        print(f"[API_SERVICE] Token set: {token[:20]}...")

    def clear_auth_token(self):
        """Remove the authorization token from session headers."""
        self.token = None
        if 'Authorization' in self.session.headers:
            del self.session.headers['Authorization']

    def get_api_status(self) -> requests.Response:
        """
        Check API server status.
        
        Returns:
            API response with server status
        """
        return self._make_request('GET', '')

# Create a singleton instance of the API service
api_service = ApiService()

