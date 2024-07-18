# FastAPI and NiceGUI Login Application

This project implements a simple login page using NiceGUI for the frontend and FastAPI for the backend. It provides a secure authentication system with JWT tokens.

## Dependencies

- FastAPI
- Uvicorn
- NiceGUI
- Pydantic
- bcrypt
- python-jose
- httpx
- python-multipart

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fastapi-nicegui-login.git
   cd fastapi-nicegui-login
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, use the following command:

```
python main.py
```

The application will be available at `http://localhost:8000`.

## Features

- User registration
- User login with JWT token authentication
- Secure password hashing
- Simple and intuitive UI using NiceGUI

## API Endpoints

- **POST /api/register** - Register a new user
- **POST /api/token** - Login and receive a JWT token
- **GET /api/users/me** - Get current user information (protected route)

## Frontend

The frontend is a simple login page created with NiceGUI. It communicates with the backend API to authenticate users.

## Security

- Passwords are hashed using bcrypt before storing
- JWT tokens are used for authentication
- CORS is enabled to allow frontend-backend communication

## Future Improvements

- Add email verification for new users
- Implement password reset functionality
- Add more protected routes and user profile management
- Replace in-memory user storage with a database
- Implement refresh tokens for better security
- Add input validation on the frontend

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).