from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder='static')

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/about')
def about_me():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
    

if __name__ == "__main__":
    app.run(debug=True)