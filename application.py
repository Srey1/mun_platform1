import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
#from tempfile import mkdtemp
#from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

#from functions import login_required
from flask_sqlalchemy import SQLAlchemy

#from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from datetime import timedelta
# Configure application
app = Flask(__name__)
#app.secret_key = os.urandom(24)
app.config['SECRET_KEY'] = "This_is_the_seeeecccccreeet_thingzmagingz"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

#Session(app)
#login_manager.init_app(app)

app.permanent_session_lifetime = timedelta(days=1)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80))
    hand_up = db.Column(db.String(80))
    raise_up = db.Column(db.String(80))



# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response




amt = 0

forr = 0
agains = 0
obstain = 0

counter = []
counter1 = []
counter2 = []

final_count = []
final_vote = []

countries = []

# For Hand Raising
number_track = 0
number_hand = []
country_hand = []
type_hand = []

extra_count = []
extra_vote = []

sigh = [1, 2]

tli = []

#x = False



@app.route("/voting", methods=["GET", "POST"])
#@login_required
def voting():

    global amt
    global forr
    global agains
    global obstain
    global counter
    global counter1
    global counter2
    global final_count
    global final_vote
    global countries
    global number_track
    global number_hand
    global country_hand
    global type_hand


    options = ["In Favor", "Abstention", "Against"]


    if request.method == "GET":
        return render_template("voting.html", counter = counter, counter1 = counter1, counter2 = counter2, options = options)

    else:

        vote = request.form.get("vote")

        s = vote

        the_current_user = session["user_id"]

        acountry = User.query.filter_by(id=the_current_user).first()
        country = acountry.username

        #countries[country] = vote

        acountry.raise_up = vote
        db.session.commit()


        return redirect("/")


@app.route("/transfer_page", methods=["GET", "POST"])
def transf():

    options = ["In Favor", "Abstention", "Against"]


    if request.method == "POST":
        the_current_user = session["user_id"]
        acountry = User.query.filter_by(id=the_current_user).first()
        country = acountry.hand_up




        return redirect("/")
    else:
        return render_template("voting.html", counter = counter, counter1 = counter1, counter2 = counter2, options = options)



@app.route("/", methods=["GET", "POST"])
def vot():

    global country_hand
    global country_raise
    global final_count
    global final_vote
    global counter
    global counter1
    global counter2
    global forr
    global agains
    global amt

    final_count = []
    final_vote = []
    country_hand = []
    type_hand = []
    counter = []
    counter1 = []
    counter2 = []



    for i in User.query.filter_by(raise_up="In Favor").all():
        final_count.append(i.username)
        final_vote.append("In Favor")
        counter.append("a")
    for i in User.query.filter_by(raise_up="Abstention").all():
        final_count.append(i.username)
        final_vote.append("Abstention")
        counter1.append("a")
    for i in User.query.filter_by(raise_up="Against").all():
        final_count.append(i.username)
        final_vote.append("Against")
        counter2.append("a")

    forr = len(counter)
    agains = len(counter2)
    obstain = len(counter1)
    amt = len(final_vote)

    for i in User.query.filter_by(hand_up="Point of Information(POI)").all():
        country_hand.append(i.username)
        type_hand.append("Point of Information")
    for i in User.query.filter_by(hand_up="Speech").all():
        country_hand.append(i.username)
        type_hand.append("Speech")
    for i in User.query.filter_by(hand_up="Amendment").all():
        country_hand.append(i.username)
        type_hand.append("Amendment")
    for i in User.query.filter_by(hand_up="Amendment to the Second Degree").all():
        country_hand.append(i.username)
        type_hand.append("Amendment To The Second Degree")

    number_track = len(country_hand)




    return render_template("vote.html", final_count = final_count, final_vote = final_vote, amt = amt, forr = forr, obstain = obstain, agains = agains, country_hand = country_hand, type_hand = type_hand, number_track = number_track)



@app.route("/c", methods=["GET", "POST"])
def ccc():
    global country_hand
    global country_raise
    global final_count
    global final_vote
    global counter
    global counter1
    global counter2
    global forr
    global agains
    global amt

    final_count = []
    final_vote = []
    country_hand = []
    type_hand = []
    counter = []
    counter1 = []
    counter2 = []

    if session["user_id"] != None:

        for i in User.query.filter_by(raise_up="In Favor").all():
            final_count.append(i.username)
            final_vote.append("In Favor")
            counter.append("a")
        for i in User.query.filter_by(raise_up="Abstention").all():
            final_count.append(i.username)
            final_vote.append("Abstention")
            counter1.append("a")
        for i in User.query.filter_by(raise_up="Against").all():
            final_count.append(i.username)
            final_vote.append("Against")
            counter2.append("a")

        forr = len(counter)
        agains = len(counter2)
        obstain = len(counter1)
        amt = len(final_vote)

        for i in User.query.filter_by(hand_up="Point of Information(POI)").all():
            country_hand.append(i.username)
            type_hand.append("Point of Information")
        for i in User.query.filter_by(hand_up="Speech").all():
            country_hand.append(i.username)
            type_hand.append("Speech")
        for i in User.query.filter_by(hand_up="Amendment").all():
            country_hand.append(i.username)
            type_hand.append("Amendment")
        for i in User.query.filter_by(hand_up="Amendment to the Second Degree").all():
            country_hand.append(i.username)
            type_hand.append("Amendment To The Second Degree")

        number_track = len(country_hand)


        return render_template("chair.html", final_count = final_count, final_vote = final_vote, amt = amt, forr = forr, obstain = obstain, agains = agains, country_hand = country_hand, type_hand = type_hand, number_track = number_track)
    else:
        return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():




    """Log user in"""

    # Forget any user_id
    session.clear()

    if request.method == "GET":
        #print(generate_password_hash("33hello45"))

        #new_user = User(id = 21, username = "Austria", password = "33Austria45")
        #db.session.add(new_user)
        #db.session.commit()

        return render_template("login.html")


    # User reached route via POST (as by submitting a form via POST)
    else:


        #global country
        #country = request.form.get("username"):

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("login.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("login.html")

        gg = request.form.get("username")

        aa = request.form.get("password")




        # Query database for username
        rows = User.query.filter_by(username=gg).first()
        if rows == None:

            return render_template("login.html")




        #print(rows)

        # Ensure username exists and password is correct
        #if len(rows) != 1:
         #   return redirect("/login")

        #if request.form.get("password") != rows[0]["password"]:
        #    return redirect("/login")
        # Ensure username exists and password is correct
        #y = check_password_hash(rows[0]["password"], request.form.get("password"))
        if (str(rows.password) == str(aa)):

            session["user_id"] = rows.id

            if rows.username == "Chair":
                return redirect("/c")
            else:
                return redirect("/")



        return render_template("login.html")




        #if rows != "shouldnotbethis" or not check_password_hash(rows[0]["password"], request.form.get("password")):
        #    return render_template("login.html")

        #if rows[0]["password"] != request.form.get("password")):
           # return apology("invalid", 403)

        # Remember which user has logged in





@app.route("/chair", methods=["GET", "POST"])
#@login_required
def chair():
    if request.method == "POST":
        global final_count
        global final_vote
        global counter
        global counter1
        global counter2
        global forr
        global agains
        global amt

        final_count = []
        final_vote = []
        country_hand = []
        type_hand = []
        counter = []
        counter1 = []
        counter2 = []

        for i in User.query.filter_by(raise_up="In Favor").all():
            i.raise_up = "Nothing"
            db.session.commit()
        for i in User.query.filter_by(raise_up="Abstention").all():
            i.raise_up = "Nothing"
            db.session.commit()
        for i in User.query.filter_by(raise_up="Against").all():
            i.raise_up = "Nothing"
            db.session.commit()

        return redirect("/c")


@app.route("/quickrefresh", methods=["GET", "POST"])
#@login_required
def refresh():
    if request.method == "POST":
        return redirect("/c")

@app.route("/raise", methods=["GET", "POST"])
#@login_required
def raise_hand():
    if request.method == "GET":
        return render_template("raise.html")
    elif request.method == "POST":
        global type_hand
        global country_hand
        global number_track
        global final_count
        isit = False
        reason = request.form.get("raise_type")
        curent_user = session["user_id"]
        before = User.query.filter_by(id=curent_user).first()
        country_raise = before.username


        """
        for items in country_hand:
            if str(items) == str(country_raise):
                l = country_hand.index(country_raise)
                type_hand[l] = reason
                isit = True
                print(f"No hand {country_hand}")
                print(f"No hand {type_hand}")
                print(f"No hand {final_count}")
                print(f"No hand {final_vote}")

        """
        before.hand_up = reason
        db.session.commit()



        return redirect("/")





@app.route("/quickraise", methods=["GET", "POST"])
def quick_raise():
    if request.method == "POST":

        #sure = False
        #sure = False
        the_user = session["user_id"]
        before_country_raise = User.query.filter_by(id=the_user).first()
        current_count = before_country_raise.username


        if before_country_raise.hand_up != "Nothing":
            before_country_raise.hand_up = "Nothing"
            db.session.commit()

            return redirect("/")

        else:
            return render_template("raise.html")



        for items in country_hand:
            if str(items) == str(current_count):
                x = country_hand.index(current_count)
                country_hand.remove(current_count)
                type_hand.pop(x)

                return redirect("/")


        return render_template("raise.html")

@app.route("/the_check", methods=["GET", "POST"])
def lets_hope():
    if request.method == "POST":
        global country_hand
        global country_raise
        global final_count
        global final_vote

        return render_template("raise.html")


@app.route("/the_finish", methods=["GET", "POST"])
def final_hope():
    if request.method == "POST":
        #country_hand.append("bye")
        #type_hand.append("please")
        global extra_count
        global extra_vote

        return render_template("vote.html", final_count = final_count, final_vote = final_vote, amt = amt, forr = forr, obstain = obstain, agains = agains, country_hand = country_hand, type_hand = type_hand, number_track = number_track)



@app.route("/alldown", methods=["GET", "POST"])
#@login_required
def quick_close():
    global type_hand
    global country_hand
    global number_track
    global country_hand
    global country_raise

    country_hand = []
    type_hand = []

    for i in User.query.filter_by(hand_up="Point of Information(POI)").all():
        i.hand_up = "Nothing"
        db.session.commit()
    for i in User.query.filter_by(hand_up="Speech").all():
        i.hand_up = "Nothing"
        db.session.commit()
    for i in User.query.filter_by(hand_up="Amendment").all():
        i.hand_up = "Nothing"
        db.session.commit()
    for i in User.query.filter_by(hand_up="Amendment to the Second Degree").all():
        i.hand_up = "Nothing"
        db.session.commit()

    number_track = len(country_hand)
    return redirect("/c")
