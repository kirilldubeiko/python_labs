import os
import sys
from flask import Flask, render_template, send_file, jsonify

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from lab.io_utils import load_students
from lab.processing import count_group_statistics
from lab.errors import AppError

DATA_FILE = os.path.join(BASE_DIR, "data", "students.csv")
app = Flask(__name__, template_folder=".")


def get_version() -> str:

    try:
        st = os.stat(DATA_FILE)
        return f"{st.st_mtime_ns}-{st.st_size}"
    except OSError:
        return "0"


@app.route("/")
def root():
    version = get_version()
    try:
        students = load_students(DATA_FILE, has_header=True)
    except AppError:
        students = []

    stats = count_group_statistics(students)

    return render_template(
        "index.html",
        students=students,
        stats=stats,
        passed=60,
        version=version,
    )


@app.route("/version")
def version():
    return jsonify(version=get_version())


@app.route("/data/students.csv")
def get_csv():
    return send_file(DATA_FILE, mimetype="text/csv")


if __name__ == "__main__":
    app.run(debug=True)