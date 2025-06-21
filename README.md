# RoutingApp

None

## About

This is a FletX application built with FletX a GetX-like tiny framework for Python and Flet. FletX provides state management, dependency injection, and routing capabilities similar to GetX in Flutter.

## Features

- 🚀 **Fast Development**: Hot reload and rapid prototyping
- 🏗️ **Clean Architecture**: Separation of concerns with controllers, views, and services
- 💉 **Dependency Injection**: Automatic dependency management
- 🔄 **State Management**: Reactive state management with automatic UI updates
- 🗺️ **Routing**: Declarative routing with named routes
- 📱 **Cross-platform**: Run on web, desktop, and mobile

## Project Structure

```sh
routing_app/
├── app/
│   ├── controllers/     # Business logic controllers
│   ├── services/       # Business services and API calls
│   ├── models/         # Data models
│   ├── components/     # Reusable widgets
│   ├── pages/          # Application pages
│   └── routes.py       # App routing modules
├── assets/             # Static assets (images, fonts, etc.)
├── tests/              # Test files
├── .python-version     # Python dependencies
├── pyproject.toml      # Python dependencies
├── README.md           # Quick start README
└── main.py            # Application entry point
```

## Getting Started 🚀

### Prerequisites

- Python 3.12+
- pip (Python package manager)

### Installation

1. Clone or download this project
2. Install dependencies:
   ```bash
   # Using pip
   pip install -r requirements.txt

   # NOTE: you can use your favorite python package manager (uv, poetry, pipenv etc...)
   ```

### Running the Application

```bash
# Run with FletX CLI (recommended)
fletx run

# Or run directly with Python
python main.py

# Run in web mode
fletx run --web

# Run in desktop mode
fletx run --desktop

# Run with custom host and port
fletx run --host 0.0.0.0 --port 8080
```

## Development

### Creating New Components

```bash
# Create a new controller
fletx generate controller UserController

# Create a new view
fletx generate view UserView

# Create a new service
fletx generate service ApiService

# Create a new page
fletx generate page ProfilePage
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_controllers.py
```

### Code Formatting

```bash
# Format code with black
black .

# Check code style with flake8
flake8 app/

# Type checking with mypy
mypy app/
```

---


## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request


## Author

pro2015

## Version

0.1.0