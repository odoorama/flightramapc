from flask import render_template, redirect, request, url_for, flash, get_flashed_messages, session
from market import app
from market.forms import RegisterForm, LoginForm
from market.models import U2Message, User

def set_app_context():
    url_root = request.url_root
#    url_root = 'hello'
    app_context = {}
    app_context['platform_code'] = '0001'
    app_context['platform_name'] = 'UniRama'
    channel_in = 'ghanarama'
    if url_root.find('unirama') >= 0:
        channel_in = 'unirama'
    if url_root.find('flightrama') >= 0:
        channel_in = 'flightrama'
    if url_root.find('ghanarama') >= 0:
        channel_in = 'ghanarama'
    if url_root.find('studentrama') >= 0:
        channel_in = 'studentrama'
    if url_root.find('safarirama') >= 0:
        channel_in = 'safarirama'
    if url_root.find('cruiserama') >= 0:
        channel_in = 'cruiserama'
    if url_root.find('ferryrama') >= 0:
        channel_in = 'ferryrama'
    if url_root.find('pakistanja') >= 0:
        channel_in = 'pakistanja'

    if channel_in == 'unirama':
        app_context['enterprise_code'] = '0001-0001'
        app_context['enterprise_name'] = 'Unirama'
        app_context['brand_code'] = '0001-0001-0001'
        app_context['brand_name'] = 'UniRama'
        app_context['channel_code'] = '0001-0001-0001-0001'
        app_context['channel_name'] = 'UniRama'
        app_context['channel_catchphrase'] = 'Unity and Dignity'
        app_context['channel_catchphrase'] = url_root
        app_context['channel_icon'] = 'fa fa-globe'
        app_context['base_style'] = "body { background-color: green; color: white }"

    if channel_in == 'flightrama':
        app_context['enterprise_code'] = '0001-0002'
        app_context['enterprise_name'] = 'FlightRama'
        app_context['brand_code'] = '0001-0002-0001'
        app_context['brand_name'] = 'FlightRama'
        app_context['channel_code'] = '0001-0002-0001-0001'
        app_context['channel_name'] = 'FlightRama'
        app_context['channel_catchphrase'] = 'The Home of Going Away'
        app_context['channel_catchphrase'] = url_root
        app_context['channel_icon'] = 'fa fa-globe'
        app_context['base_style'] = "body { background-color: purple; color: white }"

    if channel_in == 'ghanarama':
        app_context['enterprise_code'] = '0001-0003'
        app_context['enterprise_name'] = 'GhanaRama'
        app_context['brand_code'] = '0001-0003-0001'
        app_context['brand_name'] = 'GhanaRama'
        app_context['channel_code'] = '0001-0003-0001-0001'
        app_context['channel_name'] = 'GhanaRama'
        app_context['channel_catchphrase'] = 'The Beautiful Black Star of Africa'
        app_context['channel_icon'] = 'fa fa-star'
        app_context['base_style'] = "body { background-color: orange; color: black }"

    if channel_in == 'studentrama':
        app_context['enterprise_code'] = '0001-0004'
        app_context['enterprise_name'] = 'StudentRama'
        app_context['brand_code'] = '0001-0004-0001'
        app_context['brand_name'] = 'StudentRama'
        app_context['channel_code'] = '0001-0004-0001-0001'
        app_context['channel_name'] = 'StudentRama'
        app_context['channel_catchphrase'] = 'Broadening Minds'
        app_context['channel_catchphrase'] = url_root
        app_context['channel_icon'] = 'fa fa-globe'
        app_context['base_style'] = "body { background-color: blue; color: white }"

    if channel_in == 'safarirama':
        app_context['enterprise_code'] = '0001-0005'
        app_context['enterprise_name'] = 'SafariRama'
        app_context['brand_code'] = '0001-0005-0001'
        app_context['brand_name'] = 'SafariRama'
        app_context['channel_code'] = '0001-0005-0001-0001'
        app_context['channel_name'] = 'SafariRama'
        app_context['channel_catchphrase'] = 'The Love of Life'
        app_context['channel_catchphrase'] = url_root
        app_context['channel_icon'] = 'fa fa-globe'
        app_context['base_style'] = "body { background-color: orange; color: white }"

    if channel_in == 'ferryrama':
        app_context['enterprise_code'] = '0001-0006'
        app_context['enterprise_name'] = 'FerryRama'
        app_context['brand_code'] = '0001-0006-0001'
        app_context['brand_name'] = 'FerryRama'
        app_context['channel_code'] = '0001-0006-0001-0001'
        app_context['channel_name'] = 'FerryRama'
        app_context['channel_catchphrase'] = 'A Better Way to Travel'
        app_context['channel_catchphrase'] = url_root
        app_context['channel_icon'] = 'fa fa-globe'
        app_context['base_style'] = "body { background-color: blue; color: white }"


    if channel_in == 'cruiserama':
        app_context['enterprise_code'] = '0001-0007'
        app_context['enterprise_name'] = 'CruiseRama'
        app_context['brand_code'] = '0001-0007-0001'
        app_context['brand_name'] = 'CruiseRama'
        app_context['channel_code'] = '0001-0007-0001-0001'
        app_context['channel_name'] = 'CruiseRama'
        app_context['channel_catchphrase'] = 'The World in your Oyster'
        app_context['channel_catchphrase'] = url_root
        app_context['channel_icon'] = 'fa fa-globe'
        app_context['base_style'] = "body { background-color: blue; color: white }"

    if channel_in == 'pakistanja':
        app_context['enterprise_code'] = '0001-1001'
        app_context['enterprise_name'] = 'Pakistanja'
        app_context['brand_code'] = '0001-1001-0001'
        app_context['brand_name'] = 'Pakistanja'
        app_context['channel_code'] = '0001-1001-0001-0001'
        app_context['channel_name'] = 'Pakistanja'
        app_context['channel_catchphrase'] = 'Dreaming of Pakistan Skies'
        app_context['channel_catchphrase'] = url_root
        app_context['channel_icon'] = 'fa fa-globe'
        app_context['base_style'] = "body { background-color: green; color: white }"
    
    
    return app_context

def set_app_styles(in_context):

    app_styles = {}
    app_styles['base'] = in_context['base_style']
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


@app.route('/plan')
def plan_page():
    app_context = set_app_context()
    app_styles = set_app_styles(app_context)
    u2M = U2Message()
    planitems = u2M.get_planitems()
    return render_template('plan.html', app_context=app_context, app_styles=app_styles, planitems=planitems)


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
    u2M = U2Message()
    pax_list = u2M.get_pax_list()
    return render_template('party.html', app_context=app_context, app_styles=app_styles, pax_list=pax_list)


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
