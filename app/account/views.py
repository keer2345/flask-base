from flask import Blueprint, flash, redirect, render_template

from app.account.forms import LoginForm
from app.models import User

account_bp = Blueprint('account', __name__)


@account_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Log in an existing user."""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if (user is not None and user.password_hash is not None
                and user.verify_password(form.password.data)):
            flash('You are now logged in. Welcome back!', 'success')
        else:
            flash('Invalid email or password.', 'form-error')

    return render_template('account/login.html', form=form)
