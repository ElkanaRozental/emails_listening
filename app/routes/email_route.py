from flask import Blueprint, request, jsonify

from app.repository.emails_repository import get_all_details_by_email
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

@email_blueprint.route('/find_by_email/<string:email>', methods=['GET'])
def find_by_email(email):
    try:
        res = get_all_details_by_email(email)
        print(res)
        res = res.to_dict()
        return jsonify({
            **res,
        }), 200
    except Exception as e:
        print(str(e))