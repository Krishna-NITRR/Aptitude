# Day of Week Web Application

This project is a web application that allows users to convert a date into the corresponding day of the week using a simple interface. The application is built using Flask and utilizes a custom Python function to perform the date-to-day conversion.

## Project Structure

```
day-of-week-webapp
├── src
│   ├── app.py                # Main entry point of the web application
│   ├── dayfromdate.py        # Contains the function to calculate the day of the week
│   ├── templates
│   │   └── index.html        # HTML template for user interface
│   └── static
│       └── css
│           └── style.css     # CSS styles for the web application
├── tests
│   └── test_dayfromdate.py   # Unit tests for the day_from_date_odd_days function
├── requirements.txt           # Lists project dependencies
├── .gitignore                 # Specifies files to be ignored by Git
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd day-of-week-webapp
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python src/app.py
   ```

5. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- Enter a date in the format `dd-mm-yyyy` in the input field.
- Click the "Submit" button to see the corresponding day of the week displayed on the page.

## Testing

To run the unit tests for the `day_from_date_odd_days` function, use the following command:

```bash
python -m unittest tests/test_dayfromdate.py
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.