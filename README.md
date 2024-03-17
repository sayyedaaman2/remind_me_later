# Remind Me Later

## Introduction
Remind Me Later is a web application designed to help users stay organized and manage their tasks effectively. This repository contains the source code for the Remind Me Later application.

## Technologies Used
- **Python**: Backend development using Django and Celery
- **Django**: Web framework for building the backend server
- **Celery**: Distributed task queue for background processing
- **HTML/CSS/JavaScript**: Frontend development for user interface
- **FontAwesome**: Icon library for UI enhancements
- **Redis**: In-memory data structure store used as a message broker for Celery tasks

## Installation
To run Remind Me Later on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/remind_me_later.git
   ```

2. Navigate to the project directory:
   ```bash
   cd remind_me_later
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

5. Open another terminal window and start the Celery worker:
   ```bash
   celery -A remind_me_later worker -l INFO
   ```

6. Access Remind Me Later in your web browser at `http://localhost:8000`.

## Pages
1. **Login**: Allows users to authenticate by providing their username and password.
2. **Sign Up**: Enables new users to create an account by providing a username, email, and password.
3. **Logout**: Allows users to securely log out of their accounts.
4. **Reminder List**: Displays a list of reminders for the logged-in user.
5. **Create Reminder**: Allows users to create new reminders.
6. **Delete Reminder**: Allows users to delete existing reminders.
7. **Homepage**: The landing page of the application.

## Features
1. **User Authentication**: Users can log in with their username and password, ensuring secure access to their accounts.
2. **User Registration**: New users can sign up for an account using their email, username, and password.
3. **Reminder Management**: Users can create, view, and delete reminders to keep track of their tasks effectively.

## Contributing
Contributions are welcome! Please fork the repository, make changes, and submit a pull request. For major changes, please open an issue first to discuss the proposed changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Additional Modules
- **Celery**: Asynchronous task queue/job queue based on distributed message passing.
- **Redis**: In-memory data structure store used as a message broker for Celery tasks.

Please make sure to install these additional modules (`celery`, `celery[redis]`, and `redis`) using `pip install` before running the application.

## Database
This project uses SQLite database, which is included by default with Django. You don't need to perform any additional setup for the database.
```
