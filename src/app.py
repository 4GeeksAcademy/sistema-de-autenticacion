"""
This module takes care of starting the API Server, loading the DB, and adding the endpoints.
"""
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from api.utils import APIException, generate_sitemap
from api.models import db
from api.routes import api
from api.admin import setup_admin
from api.commands import setup_commands

# Determine the environment
ENV = "development" if os.getenv("FLASK_DEBUG") == "1" else "production"
static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../public/')

# Initialize Flask app
app = Flask(__name__)
app.url_map.strict_slashes = False

# Database configuration
db_url = os.getenv("DATABASE_URL", "sqlite:////tmp/test.db").replace("postgres://", "postgresql://")
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JWT configuration
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')  # Ensure to set this in production
jwt = JWTManager(app)

# CORS configuration
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Allow all origins for API routes

# Initialize the database and migrations
MIGRATE = Migrate(app, db, compare_type=True)
db.init_app(app)

# Setup admin and commands
setup_admin(app)
setup_commands(app)

# Add all endpoints from the API with an "api" prefix
app.register_blueprint(api, url_prefix='/api') 

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    """Generate a sitemap for the API endpoints."""
    if ENV == "development":
        return generate_sitemap(app)
    return send_from_directory(static_file_dir, 'index.html')

# Serve any other endpoint as a static file
@app.route('/<path:path>', methods=['GET'])
def serve_any_other_file(path):
    """Serve static files or return the index page if not found."""
    full_path = os.path.join(static_file_dir, path)
    if not os.path.isfile(full_path):
        path = 'index.html'
    response = send_from_directory(static_file_dir, path)
    response.cache_control.max_age = 0  # Avoid cache memory
    return response

# Run the application
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3001))
    app.run(host='0.0.0.0', port=PORT, debug=True)
