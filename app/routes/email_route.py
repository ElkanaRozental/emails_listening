from flask import Blueprint, request, jsonify

from app.services.producer import produce_email

email_blueprint = Blueprint('menu', __name__)


@email_blueprint.route('', methods=['POST'])
def fetch_emails():
    try:
        email = request.get_json()
        print(email)
        produce_email(email)

        return jsonify({
            **email,
        }), 200
    except Exception as e:
        print(str(e))

