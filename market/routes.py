from flask import render_template, redirect, request, url_for, flash, get_flashed_messages, session
from market import app
from market.forms import RegisterForm, LoginForm
from market.models import U2Message, User

def set_app_context():
    url_root = request.url_root
#    url_root = 'hello'
    app_context = {}
    app_context['platform_code'] = '00001'
    app_context['platform_name'] = 'UniRama'
    channel_in = 'flightrama'
    if url_root.find('ghanarama'):
        channel_in = 'ghanarama'
    if url_root.find('flightrama'):
        channel_in = 'flightrama'
    if url_root.find('unirama'):
        channel_in = 'unirama'
    if url_root.find('pakistanja'):
        channel_in = 'pakistanja'


    if channel_in == 'flightrama':
        app_context['enterprise_code'] = '00001-00001'
        app_context['enterprise_name'] = 'FlightRama'
        app_context['brand_code'] = '00001-00001-00001'
        app_context['brand_name'] = 'FlightRama'
        app_context['channel_code'] = '00001-00001-00001-00001'
        app_context['channel_name'] = 'FlightRama'
        app_context['channel_catchphrase'] = 'The Home of Going Away'
        app_context['channel_catchphrase'] = url_root
        app_context['channel_icon'] = 'fa fa-globe'
        app_context['base_style'] = "body { background-color: purple; color: white }"

    if channel_in == 'ghanarama':
        app_context['enterprise_code'] = '00001-00001'
        app_context['enterprise_name'] = 'GhanaRama'
        app_context['brand_code'] = '00001-00001-00001'
        app_context['brand_name'] = 'GhanaRama'
        app_context['channel_code'] = '00001-00001-00001-00001'
        app_context['channel_name'] = 'GhanaRama'
        app_context['channel_catchphrase'] = 'The Beautiful Black Star of Africa'
        app_context['channel_icon'] = 'fa fa-star'
        app_context['base_style'] = "body { background-color: orange; color: black }"

    return app_context

def set_app_styles(app_context):

    app_styles = {}
    app_styles['base'] = app_context['base_style']
    return app_styles


@app.route('/')
@app.route('/home')
def home_page():
    app_context = set_app_context()
    app_styles = set_app_styles(app_context)
    return render_template('home.html', app_context=app_context, app_styles=app_styles)

@app.route('/set/<value>')
def set_session(value):
    session['value'] = value
    return f'The value you set is: { value }'

@app.route('/get')
def get_session():
    return f'The value in the session is { session.get("value")}'


@app.route('/search')
def search_page():
    app_context = set_app_context()
    app_styles = set_app_styles(app_context)
    u2M = U2Message()
    planitems = u2M.get_planitems()
    return render_template('search.html', app_context=app_context, app_styles=app_styles, planitems=planitems)


@app.route('/select')
def select_page():
    app_context = set_app_context()
    app_styles = set_app_styles(app_context)
    u2M = U2Message()
    product_list = u2M.get_product_list()
    return render_template('select.html', app_context=app_context, app_styles=app_styles, product_list=product_list)


@app.route('/party')
def party_page():
    app_context = set_app_context()
    app_styles = set_app_styles(app_context)
    return render_template('party.html', app_context=app_context, app_styles=app_styles)


@app.route('/cart')
def cart_page():
    app_context = set_app_context()
    app_styles = set_app_styles(app_context)
    return render_template('cart.html', app_context=app_context, app_styles=app_styles)


@app.route('/places')
def places_page():
    app_context = set_app_context()
    app_styles = set_app_styles(app_context)
    return render_template('places.html', app_context=app_context, app_styles=app_styles)


@app.route('/routes')
def routes_page():
    app_context = set_app_context()
    app_styles = set_app_styles(app_context)
    return render_template('routes.html', app_context=app_context, app_styles=app_styles)


@app.route('/top_lists')
def top_lists_page():
    app_context = set_app_context()
    app_styles = set_app_styles(app_context)
    return render_template('top_lists.html', app_context=app_context, app_styles=app_styles)


@app.route('/offers')
def offers_page():
    app_context = set_app_context()
    app_styles = set_app_styles(app_context)
    return render_template('offers.html', app_context=app_context, app_styles=app_styles)


@app.route('/sponsors')
def sponsors_page():
    app_context = set_app_context()
    app_styles = set_app_styles(app_context)
    return render_template('sponsors.html', app_context=app_context, app_styles=app_styles)


@app.route('/subscriptions')
def subscriptions_page():
    app_context = set_app_context()
    app_styles = set_app_styles(app_context)
    return render_template('subscriptions.html', app_context=app_context, app_styles=app_styles)


@app.route('/bookings')
def bookings_page():
    app_context = set_app_context()
    app_styles = set_app_styles(app_context)
    return render_template('bookings.html', app_context=app_context, app_styles=app_styles)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    app_context = set_app_context()
    app_styles = set_app_styles(app_context)
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an Error creating a User: {err_msg}', category="danger")
    return render_template('login.html', app_context=app_context, app_styles=app_styles, form=form)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    app_context = set_app_context()
    app_styles = set_app_styles(app_context)
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email_address=form.email_address.data, password=form.password1.data)
        user_to_create.newuser()
        flash(f'User {user_to_create.username} created')
        return redirect(url_for('home_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an Error creating a User: {err_msg}', category="danger")
    return render_template('register.html', app_context=app_context, app_styles=app_styles, form=form)
