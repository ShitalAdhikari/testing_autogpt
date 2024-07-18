# FastAPI and NiceGUI Login Application

This project implements a simple login page using NiceGUI for the frontend and FastAPI for the backend. It provides a secure authentication system with JWT tokens.

## Dependencies

- FastAPI (>=0.68.0, <0.103.0)
- Uvicorn (>=0.15.0, <0.24.0)
- NiceGUI (1.3.8)
- Pydantic (>=2.0.0, <3.0.0)
- bcrypt (>=3.2.0, <4.1.0)
- python-jose (3.3.0)
- httpx (>=0.23.0, <0.26.0)
- python-multipart (0.0.5)
- python-dotenv (1.0.0)

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

4. Create a `.env` file in the project root and add the following:
   ```
   SECRET_KEY=your_secret_key_here
   ```
   Replace `your_secret_key_here` with a secure random string.

## Running the Application

### Development Setup

For development, you can run the frontend and backend separately:

1. Run the backend:
   ```
   python backend.py
   ```
   The backend API will be available at `http://localhost:8000`.

2. In a new terminal, run the frontend:
   ```
   python frontend.py
   ```
   The frontend will be available at `http://localhost:8080`.

### Production Setup

To run the full application with both frontend and backend combined:

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
- Environment variables are used for sensitive information

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