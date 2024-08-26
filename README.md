# BudgetMate

BudgetMate is a web-based budgeting application that helps users manage their income by automatically allocating it into predefined categories such as savings, expenses, and investments. Built using Django and Bootstrap, BudgetMate provides a simple and intuitive interface to make budgeting easy.

## Features

- **Income Input**: Users can input their income to get a detailed breakdown of their budget.
- **Predefined Percentages**: The application allocates income based on predefined percentages for savings, expenses, and investments.
- **Responsive UI**: The application features a responsive design using Bootstrap, making it accessible on various devices.
- **Error Handling**: The application includes error handling to ensure smooth operation.

## Technologies Used

- **Backend**: Django (Python 3.12)
- **Frontend**: Bootstrap 4.5.2
- **Database**: SQLite (default for Django projects)

## Installation

### Prerequisites

- Python 3.12 or higher
- Virtualenv (optional but recommended)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/michaelorina/budgetmate.git
   cd budgetmate
2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
4. **Run Migrations**
   ```bash
   python manage.py migrate
5. **Start the Development Server**
   ```bash
   python manage.py runserver
6. **Access the Application**
    Open your web browser and go to [http://localhost:8000/](http://localhost:8000/).

## Usage

- **Enter Income**: On the home page, enter your income and click "Calculate Budget".
- **View Results**: The application will display the breakdown of your income into savings, expenses, and investments.
- **Back to Input**: Click "Back" to enter a new income amount.

## Directory Structure

```plaintext
budgetmate/
├── budgetmate/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── budget/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── templates/
│       ├── budgetmate/
│           ├── base.html
│           ├── input.html
│           └── result.html
├── manage.py
└── README.md

## Custom Filters

This project includes a custom Django template filter for adding CSS classes to form fields. The filter is located in `budgetmate/templatetags/custom_filters.py`.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. Contributions are welcome!

## Acknowledgments

- **Django** - The web framework for perfectionists with deadlines.
- **Bootstrap** - The most popular HTML, CSS, and JS library in the world.
