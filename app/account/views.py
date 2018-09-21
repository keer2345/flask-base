from flask import Blueprint, redirect, render_template

account_bp= Blueprint('account', __name__)


@account_bp.route('/login', method=['GET'])
def login():
    """Log in an existing user."""
    return render_template('account/login.html')
