from sqlalchemy import Column, Integer, String, Text, Numeric



def create_user_model(db):
    class User(db.Model):
        __tablename__ = 'users'

        id = Column(Integer, primary_key=True)
        first_name = Column(String(50), nullable=False)
        last_name = Column(String(50), nullable=False)
        email = Column(String(100), nullable=False, unique=True)
        mobile_no = Column(String(20), nullable=False)
        alternate_mobile_no = Column(String(20))
        address_1 = Column(Text, nullable=False)
        address_2 = Column(Text)
        address_3 = Column(Text)
        bank_name = Column(String(255))
        bank_acc_no = Column(String(50))
        ifsc_code = Column(String(20))
        branch_name = Column(String(255))
        broker_name = Column(String(255), nullable=False)
        broker_acc_no = Column(String(50), nullable=False)
        login_id = Column(String(50), nullable=False)
        password = Column(String(255), nullable=False)
        server_name = Column(String(255), nullable=False)
        amount_deposited = Column(Numeric, nullable=False)

        def __init__(self, first_name, last_name, email, mobile_no, alternate_mobile_no, address_1,
                    address_2, address_3, bank_name, bank_acc_no, ifsc_code, branch_name,
                    broker_name, broker_acc_no, login_id, password, server_name, amount_deposited):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.mobile_no = mobile_no
            self.alternate_mobile_no = alternate_mobile_no
            self.address_1 = address_1
            self.address_2 = address_2
            self.address_3 = address_3
            self.bank_name = bank_name
            self.bank_acc_no = bank_acc_no
            self.ifsc_code = ifsc_code
            self.branch_name = branch_name
            self.broker_name = broker_name
            self.broker_acc_no = broker_acc_no
            self.login_id = login_id
            self.password = password
            self.server_name = server_name
            self.amount_deposited = amount_deposited

    return User