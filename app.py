from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Config
from utils.email_util import send_registration_email
from models.user_model import create_user_model
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
User = create_user_model(db)




@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        mobile_no = request.form.get('mobile_no')
        alternate_mobile_no = request.form.get('alternate_mobile_no')
        address_1 = request.form.get('address_1')
        address_2 = request.form.get('address_2')
        address_3 = request.form.get('address_3')
        bank_name = request.form.get('bank_name')
        bank_acc_no = request.form.get('bank_acc_no')
        ifsc_code = request.form.get('ifsc_code')
        branch_name = request.form.get('branch_name')
        broker_name = request.form.get('broker_name')
        broker_acc_no = request.form.get('broker_acc_no')
        login_id = request.form.get('login_id')
        password = request.form.get('password')
        server_name = request.form.get('server_name')
        amount_deposited = request.form.get('amount_deposited')

        hashed_password = generate_password_hash(password)

        # Create a new User object with data from the form and hashed password
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile_no=mobile_no,
            alternate_mobile_no=alternate_mobile_no,
            address_1=address_1,
            address_2=address_2,
            address_3=address_3,
            bank_name=bank_name,
            bank_acc_no=bank_acc_no,
            ifsc_code=ifsc_code,
            branch_name=branch_name,
            broker_name=broker_name,
            broker_acc_no=broker_acc_no,
            login_id=login_id,
            password=hashed_password,  # Store hashed password
            server_name=server_name,
            amount_deposited=amount_deposited
        )

        # Attempt to add the new user to the database
        try:
            db.session.add(new_user)
            db.session.commit()

            # Send Email notification
            send_registration_email(email, broker_acc_no, app.config.get('EMAIL_SENDER'))

            flash('User registered successfully!', 'success')
            return redirect(url_for('list_users'))

        except Exception as e:
            db.session.rollback()
            flash(f'Error registering user: {str(e)}', 'error')
    return render_template('register.html')


@app.route('/users')
def list_users():
    users = User.query.all()
    return render_template('user_list.html', users=users)


@app.route('/users/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)

    if request.method == 'POST':
        # Update user data from form submission
        user.first_name = request.form.get('first_name')
        user.last_name = request.form.get('last_name')
        user.email = request.form.get('email')
        user.mobile_no = request.form.get('mobile_no')
        user.alternate_mobile_no = request.form.get('alternate_mobile_no')
        user.address_1 = request.form.get('address_1')
        user.address_2 = request.form.get('address_2')
        user.address_3 = request.form.get('address_3')
        user.bank_name = request.form.get('bank_name')
        user.bank_acc_no = request.form.get('bank_acc_no')
        user.ifsc_code = request.form.get('ifsc_code')
        user.branch_name = request.form.get('branch_name')
        user.broker_name = request.form.get('broker_name')
        user.broker_acc_no = request.form.get('broker_acc_no')
        user.login_id = request.form.get('login_id')
        user.server_name = request.form.get('server_name')
        user.amount_deposited = request.form.get('amount_deposited')

        try:
            db.session.commit()
            flash('User updated successfully!', 'success')
            return redirect(url_for('list_users'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating user: {str(e)}', 'error')

    return render_template('edit_user.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)