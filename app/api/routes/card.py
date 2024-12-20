from aws import db
from flask import Blueprint, abort, jsonify
import logging

bp_cards = Blueprint("card", __name__, url_prefix="/card")


@bp_cards.route("/<int:card_id>", methods=["GET"])
def read_card(card_id):
    try:
        user = db.get_user_by_card(str(card_id))
        if user is None:
            abort(404, description="This keycard is not linked to an Employee.")
        return jsonify(user), 200
    except Exception as e:
        logging.error("Error creating user: %s", str(e))
        return jsonify({"error": "An internal error has occurred."}), 400
