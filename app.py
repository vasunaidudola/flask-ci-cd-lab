from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello from CI/CD Flask app!</h1><p>Deployed via GitHub Actions → Docker → EC2.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
