from app_conf import db


class Feedback(db.Model):
    __tablename__ = 'feedback'
    _id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(50), nullable=False, unique=True)
    dealer = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return self.customer

    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments
