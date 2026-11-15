from flask import Flask
from pathlib import Path
from auth import auth
import secrets

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app = Flask(
    __name__,
    static_folder=str(FRONTEND_DIR),
    static_url_path=""
)

app.secret_key = secrets.token_hex(32)

app.secret_key = "secureaccess-development-key"
app.register_blueprint(auth, url_prefix="/api")

@app.route("/")
def home():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(debug=True)