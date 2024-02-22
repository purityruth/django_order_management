# Django Order Management

**Description:**  
Django Order Management is a web application for managing customer orders. It allows users to add orders, send SMS alerts to customers, and provides an authentication system with OpenID Connect.

## Features

- Order creation and management
- Integration with Africa's Talking API for SMS alerts
- Authentication and authorization via OpenID Connect
- RESTful API for customer and order operations

## Getting Started

### Prerequisites

- Python
- Django
- Africa's Talking account for SMS integration
- OpenID Connect for authentication

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/django-order-management.git
   cd django-order-management
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   ```bash
   source venv/bin/activate  # On Linux/macOS
   venv\Scripts\activate  # On Windows
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables:

   Create a `.env` file in the project root and add the necessary credentials. Refer to the `.env.example` file.

6. Run migrations:

   ```bash
   python manage.py migrate
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

1. Visit `http://localhost:8000/admin/` to log in and manage orders.
2. Use the provided API endpoints for customer and order operations.
3. Integrate Africa's Talking credentials for SMS alerts.

## Contributing

We welcome contributions! Please follow our [Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Africa's Talking](https://www.africastalking.com/)
- [python-social-auth](https://github.com/python-social-auth/social-core)

Thank you!
