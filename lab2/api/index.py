import os
import sys
import io
import csv
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from flask import Flask, render_template
from lab.models import Student
from lab.processing import count_group_statistics
from lab.errors import AppError

NGROK_URL = 'https://resisting-yippee-maybe.ngrok-free.dev'

app = Flask(__name__, template_folder=".")


@app.route("/")
def root():
    students = []
    
    try:
        response = requests.get(NGROK_URL, timeout=5)
        response.raise_for_status()

        reader = csv.reader(io.StringIO(response.text))
        next(reader, None)

        for row in reader:
            if not row or not row[0].strip():
                continue
            sid = int(row[0])
            name = row[1]
            grades = [int(x) if x.strip() else None for x in row[2:]]
            students.append(Student(sid, name, grades))
            
    except Exception as e:
        print(f"Ошибка: {e}")

    stats = count_group_statistics(students)
            
    return render_template(
        "index.html",
        students=students,
        stats=stats,
        passed=60
    )


if __name__ == "__main__":
    app.run(debug=True)
