from app_conf import *
from models import Feedback
from utils import send_email


@app.route('/', strict_slashes=False, methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/submit', strict_slashes=False, methods=['POST'])
def submit():
    session = db.session
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        # ################### validation #######################

        if dealer == '' or len(customer) < 3 or len(comments) < 5:
            return render_template('index.html', message='Invalid Data')

        # ################## saving to db & check customer ##################
        is_customer_exists = session.query(Feedback).filter(Feedback.customer == customer)
        if is_customer_exists.count() > 0:
            message = 'Already Submit'
            return render_template('index.html', message=message)
        else:
            feedback = Feedback(customer, dealer, rating, comments)
            # feedback = Feedback()
            session.add(feedback)
            session.commit()
            send_email(customer, dealer, rating, comments)
            return render_template('success.html')


if __name__ == '__main__':
    app.run(port=8081, debug=DEBUG)