from flask import Flask, render_template
import json
import os

app = Flask(__name__)

REPORT_PATH = os.path.join("app", "output", "report.json")


def load_report():
    if not os.path.exists(REPORT_PATH):
        return {"alerts": [], "total_events": 0}

    try:
        with open(REPORT_PATH, "r") as f:
            content = f.read().strip()
            if not content:
                return {"alerts": [], "total_events": 0}
            return json.loads(content)
    except json.JSONDecodeError:
        return {"alerts": [], "total_events": 0}


@app.route("/")
def index():
    report = load_report()
    return render_template("index.html", report=report)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
