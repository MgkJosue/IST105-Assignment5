# Interactive Treasure Hunt - Django Web Application

## Project Description

This is a Django web application that creates an interactive treasure hunt game. Users submit a number and a text message through a form, and the application processes this data through three different puzzles:

### Features

1. **Number Puzzle**
   - Checks if the submitted number is even or odd
   - If even: calculates the square root
   - If odd: calculates the cube of the number

2. **Text Puzzle**
   - Converts the text message to binary representation
   - Counts the number of vowels in the text

3. **Treasure Hunt Simulation**
   - Simulates a guessing game trying to find a random number between 1-100
   - Uses a binary search algorithm to make smart guesses
   - The user "wins" if the target number is found within 5 attempts

## Technology Stack

- Python 3.x
- Django 5.2.6
- HTML/CSS for the frontend
- SQLite database (default Django database)

## Project Structure

```
assignment5/
├── assignment5/              # Main project folder
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── puzzle/                   # App folder
│   ├── forms.py             # Form definition
│   ├── views.py             # Business logic and view functions
│   ├── urls.py              # App URL routes
│   └── templates/
│       └── puzzle/
│           └── index.html   # Main template
├── manage.py                # Django management script
└── db.sqlite3               # Database file
```

## Installation and Setup

### Prerequisites

- Python 3.7 or higher installed on your system
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/IST105-Assignment5.git
cd IST105-Assignment5/assignment5
```

### Step 2: Install Django

```bash
pip install django
```

### Step 3: Run Database Migrations

```bash
py manage.py migrate
```

### Step 4: Start the Development Server

```bash
py manage.py runserver
```

### Step 5: Access the Application

Open your web browser and go to:
```
http://127.0.0.1:8000/
```

## How to Use

1. **Enter a Number**: Type any whole number (e.g., your birth year like 1995)
2. **Enter a Text Message**: Type any text (e.g., your name or a secret word)
3. **Click Submit**: The application will process your input and display:
   - Whether your number is even or odd, and its calculated result
   - Your text converted to binary code
   - The number of vowels in your text
   - A simulated treasure hunt showing the guessing attempts

## Example

**Input:**
- Number: 16
- Text: "Hello"

**Output:**
- Number Puzzle: 16 is EVEN, Square Root = 4.0
- Text Puzzle: "Hello" has 2 vowels, Binary: 01001000 01100101 01101100 01101100 01101111
- Treasure Hunt: Shows 5 attempts to guess a random number with success/failure result

## Code Explanation

### forms.py
Defines the input form with two fields: a number field and a text field with validation.

### views.py
Contains three main functions:
- `process_number_puzzle()`: Handles even/odd logic and calculations
- `process_text_puzzle()`: Converts text to binary and counts vowels
- `treasure_hunt_simulation()`: Simulates the guessing game using binary search

### index.html
Displays the form and shows all results in a clean, minimalist design.

## Development Branches

- `main`: Stable production version
- `development`: Integration and testing
- `feature1`: Initial development work
