from flask import Blueprint, render_template, request, redirect, url_for
from api import find_book_link
from sql_connector import add_book, delete_book, load_books

views = Blueprint(__name__, 'views')
names = load_books()
@views.route('/', methods=['GET', 'POST'])
def home():
    global names
    if request.method == 'POST':
        user_input = request.form['user_input']
        print(f"Received input: {user_input}")  # DEBUG
        names.append([user_input,find_book_link(user_input)])
        add_book([user_input,find_book_link(user_input)])
        load_books()
        return redirect(url_for('views.home'))  # Prevent resubmission
    return render_template('index.html', name=names)

@views.route('/profile', methods=['GET', 'POST'])
def profile():
    args = request.args
    name = args.get('name')
    if name == 'developer':
        global names
        if request.method == 'POST':
            if 'delete' in request.form.keys():
                user_input = request.form.get('delete')
                delete_book(names[int(user_input)][0])
                names.pop(int(user_input))
            else:
                names = load_books()
                return redirect(url_for('views.profile', name='carmel'))
        return render_template('developer.html', name=names)

@views.route('/developer-mode')
def developer_mode():
    return redirect(url_for('views.profile', name='developer'))