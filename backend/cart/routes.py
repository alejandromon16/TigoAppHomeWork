from flask import Blueprint, request, jsonify
from cart.cart_store import CartStore

bp = Blueprint('cart', __name__)
cart_store = CartStore()

@bp.route('/add_plan', methods=['POST'])
def add_plan():
    plan_id = request.json['plan_id']
    cart_store.add_plan_to_cart(plan_id)
    return jsonify({'message': 'Plan added to cart'}), 200

@bp.route('/remove_plan', methods=['POST'])
def remove_plan():
    plan_id = request.json['plan_id']
    if cart_store.remove_plan_from_cart(plan_id):
        return jsonify({'message': 'Plan removed from cart'}), 200
    else:
        return jsonify({'message': 'Plan not found in cart'}), 400

@bp.route('/get_cart_contents', methods=['GET'])
def get_cart_contents():
    cart_contents = cart_store.get_cart_contents()
    return jsonify({'cart_contents': cart_contents}), 200