from flask import Blueprint
from auth.user_store import UserStore

def create_blueprint():
    from . import routes
    bp = Blueprint('auth', __name__)
    bp.user_store = UserStore()
    bp.register_blueprint(routes.bp)
    return bp
