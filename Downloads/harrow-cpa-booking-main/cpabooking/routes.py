from flask import render_template, url_for, flash, redirect, request, jsonify
from flask_login import login_user, current_user, logout_user
from . import app, db, ROOMS
from .forms import RegisterForm, LoginForm, BookingForm
from .models import User, Bookings
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

@app.route("/", methods=["GET", "POST"])
def index():
    available_rooms = ROOMS
    # Do some logic to display the available rooms
    return render_template("index.html", rooms=available_rooms, title="Home")


@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = RegisterForm()
    
    if form.validate_on_submit(): # if the register form has been submitted
        
        username = form.username.data
        email = form.email.data
        password = form.password.data
        year = form.year.data
        house = form.house.data
        tutor_group = house + str(year) 
        
        # hash email and password
        password_hash = generate_password_hash(password)

        # adding user to the database
        new_user = User(email=email, username=username, password=password_hash, tutor_group=tutor_group)

        db.session.add(new_user)
        db.session.commit()

        flash("Account created. Please login with your credentials.", 'success')
        login_user(new_user)
        return redirect(url_for('index'))

    return render_template("register.html", title="Sign Up", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()

    if form.validate_on_submit(): # if the login form has been submitted
        # checking if there is a record with the email that is inputted, will return a User object if there is. Will return None if there is no record with that email
        user = User.query.filter_by(email=form.email.data).first()

        # do verification checks here
        if user and check_password_hash(user.password, form.password.data): # change the bcrypt stuff to your hash module thing
            login_user(user)
            flash('Successfully logged in', category='success')
            return redirect(url_for('index'))
        else:
            flash('Your email or password is incorrect.', 'danger')
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    # Redirect user to login form
    flash('Successfully logged out', category='success')
    return redirect(url_for("index"))

@app.route('/layout')
def layout():
    return render_template("layout.html")

@app.route('/book', methods=["POST"])
def book():
    if request.method == "POST" and current_user.is_authenticated: 
        room_id = request.form.get("room_id")
        num_people = request.form.get("num_people")
        timeslot = request.form.get("timeslot")
        date = datetime.strptime(request.form.get("date"), '%d-%m-%Y')
        booking_records = Bookings.query.filter_by(rid=room_id, date=date, time_slot=timeslot).first()
        print("not booking records is: ", not booking_records)
        if not booking_records:
            if len(current_user.bookings) <= 3:
                booking = Bookings(rid=room_id, uid=current_user.id, date=date, num_people=num_people, time_slot=timeslot)
                print(booking)
                db.session.add(booking) 
                db.session.commit()
                flash(f"Successfully booked Room {room_id} at time slot {timeslot} on {date}", category="success")
            else:
                flash("Booking unsuccessful. There cannot be more than 3 people.")
        else:
            # send a message to user saying there is a booking already
            flash("Booking unsuccessful. The room is already booked", category="danger")
    else:
        flash("You need to login first.", category="warning")
    return redirect(url_for("index"))


@app.route('/getAvailableRooms', methods=["POST"])
def getavailablerooms():
    selected_date = datetime.strptime(request.get_json()[0]["selected_date"], '%d-%m-%Y')
    # print(selected_date)
    # database queries here
    # check each room if there are 3 bookings at the given date
    
    available_rooms = []
    for room in ROOMS:
        # select * from bookings
        # where date = selected_date
        no_bookings = Bookings.query.filter_by(rid=room, date=selected_date).count()  
        # print(no_bookings, room)
        if no_bookings < 3:
            available_rooms.append(room)

    # print(available_rooms)
    
    return jsonify(available_rooms)