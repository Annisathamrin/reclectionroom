from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Ganti dengan key yang aman
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journals.db'

# Quotes data
quotes = [
    {"text": "The pen is mightier than the sword, but the journal is mightier than the pen.", "author": "Chayy"},
    {"text": "Journaling is like whispering to oneself and listening at the same time.", "author": "Chayy"},
    {"text": "Write what should not be forgotten.", "author": "Isabel Allende"},
    {"text": "A personal journal is an ideal environment in which to 'become'.", "author": "CChayy"},
    {"text": "Keep a journal, and one day it will keep you.", "author": "Chayy"}
]
# Simulasi database untuk jurnal
journals = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Simulasi login tanpa database
    if username and password:
        session['username'] = username
        return redirect(url_for('write_journal'))
    else:
        flash('Invalid login', 'danger')
        return redirect(url_for('index'))

@app.route('/write', methods=['GET', 'POST'])
def write_journal():
    if 'username' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        date = request.form.get('date')

        # Simulasi menyimpan jurnal
        journals.append({
            'title': title,
            'content': content,
            'date': date
        })
        flash('Journal saved successfully!', 'success')
        return redirect(url_for('journals_list'))

    return render_template('write.html')


@app.route('/journals')
def journals_list():
    if 'username' not in session:
        return redirect(url_for('index'))

    return render_template('journals.html', journals=journals)

@app.route('/toggle_theme')
def toggle_theme():
    # Toggle tema gelap/terang
    current_theme = session.get('theme', 'light')
    new_theme = 'dark' if current_theme == 'light' else 'light'
    session['theme'] = new_theme
    return redirect(url_for('write_journal'))


if __name__ == '__main__':
    app.run(debug=True)

