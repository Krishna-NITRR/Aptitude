import logging
import os
import sys

# make workspace root importable so dayfromdate.py at /workspaces/Aptitude can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

try:
    from flask import Flask, render_template, request
except ImportError as e:
    raise SystemExit(
        "Flask is not installed in the current environment.\n\n"
        "Install and activate a virtual env, then install Flask:\n\n"
        "  python3 -m venv .venv\n"
        "  source .venv/bin/activate\n"
        "  pip install -U pip flask\n"
    ) from e

from dayfromdate import day_from_date_odd_days

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    day_of_week = None
    date_str = ''
    if request.method == 'POST':
        date_str = request.form.get('date', '').strip()
        try:
            day_of_week = day_from_date_odd_days(date_str)
        except Exception as e:
            day_of_week = f'Error: {e}'
    return render_template('index.html', day_of_week=day_of_week, date_str=date_str)


@app.route('/_health', methods=['GET'])
def health():
    """Simple health-check route used when debugging Cannot GET / issues."""
    return 'ok', 200


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info('Starting Flask app on 0.0.0.0:5000')
    app.run(host='0.0.0.0', port=5000, debug=True)