# Foodies Shop Web Application

Welcome to the Foodies Shop Web Application! This project is designed to provide a seamless online shopping experience for food lovers. Users can explore various food items.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)


## Technologies Used

- **Frontend**: HTML, CSS (for styling), JavaScript (for interactivity)
- **Backend**: Django
- **Database**: SQLite (for development), but can be changed to MySQL or other databases
- **Python**: For backend logic and data handling

## Features

- **Product Showcase**: Display various food products.
- **User Authentication**: Sign up and log in to manage orders and personal information.
- **Shopping Cart**: Add food items to the cart and proceed to checkout.
- **Wishlist Management**: Users can add foods to wishlist.

## Installation

Follow these steps to get the application up and running:

1. Clone the repository:
    ```bash
    git clone https://github.com/AbhikSalian/foodies-website.git
    ```

2. Navigate into the project directory:
    ```bash
    cd Foodies-Shop
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run migrations to set up the database:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

7. Access the application by visiting `http://127.0.0.1:8000/` in your web browser.


## Usage

Once the application is running, you can:

- **Browse Products**: View food items displayed on the homepage.
- **Sign Up / Log In**: Create a new account or log in to place orders.
- **Add to Cart**: Select food items and add them to your shopping cart.
- **Add to wishlist**: Select food items and add them to your wishlist.

