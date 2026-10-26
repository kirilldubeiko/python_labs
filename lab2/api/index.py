import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from flask import Flask, render_template
from lab.io_utils import load_students
from lab.processing import count_group_statistics
from lab.errors import AppError

DATA_FILE = os.path.join(BASE_DIR, "data", "students.csv")

app = Flask(__name__, template_folder=".")


@app.route("/")
def root():
    try:
        students = load_students(DATA_FILE, has_header=True)
    except AppError:
        students = []

    stats = count_group_statistics(students)

    return render_template(
        "index.html",
        students=students,
        stats=stats
    )


if __name__ == "__main__":
    app.run(debug=True)