from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market import app
from market.forms import RegisterForm
from market.models import U2Message

app_styles = {}
base_style = "body { background-color: purple; color: white }"
app_styles['base'] = base_style

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', app_styles=app_styles)


@app.route('/search')
def search_page():
    u2M = U2Message()
    planitems = u2M.get_planitems()
    return render_template('search.html', app_styles=app_styles, planitems=planitems)


@app.route('/select')
def select_page():
    u2M = U2Message()
    items = u2M.get_items()
    return render_template('select.html', app_styles=app_styles, items=items)


@app.route('/party')
def party_page():
    return render_template('party.html', app_styles=app_styles)


@app.route('/cart')
def cart_page():
    return render_template('cart.html', app_styles=app_styles)


@app.route('/places')
def places_page():
    return render_template('places.html', app_styles=app_styles)


@app.route('/routes')
def routes_page():
    return render_template('routes.html', app_styles=app_styles)


@app.route('/top_lists')
def top_lists_page():
    return render_template('top_lists.html', app_styles=app_styles)


@app.route('/offers')
def offers_page():
    return render_template('offers.html', app_styles=app_styles)


@app.route('/sponsors')
def sponsors_page():
    return render_template('sponsors.html', app_styles=app_styles)


@app.route('/subscriptions')
def subscriptions_page():
    return render_template('subscriptions.html', app_styles=app_styles)


@app.route('/bookings')
def bookings_page():
    return render_template('bookings.html', app_styles=app_styles)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
       # create user u2
       return redirect(url_for('home_page'))
#    print(f'no. errors = {form.errors}')
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an Error creating a User: {err_msg}', category="danger")
    return render_template('register.html', app_styles=app_styles, form=form)
