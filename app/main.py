from flask import Flask

from app.db.mongo_database import emails_collection
from app.routes.email_route import email_blueprint
from app.services.admin import init_topics

app = Flask(__name__)

if __name__ == '__main__':
    init_topics()
    app.register_blueprint(email_blueprint, url_prefix="/api/email")
    app.run()
