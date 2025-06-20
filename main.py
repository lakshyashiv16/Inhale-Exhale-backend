from app import create_app, db
from app.routes.api import api_blueprint
from app.models import User
from flask_cors import CORS

app = create_app()
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)
app.register_blueprint(api_blueprint, url_prefix='/api')

@app.route('/')
def home():
    return {"message": "Inhale, Exhale Backend is running."}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
