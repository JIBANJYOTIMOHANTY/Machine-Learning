from flask import Flask, render_template, request
''' 
It creates an instance of the Flask class, which is the WSGI(Web Security Gateway Interface) application.
'''

# Create an instance of the Flask class. This instance will be our WSGI application.
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask course</h1></html>"

@app.route("/index", methods=['GET'])
def indexPage():
    return render_template('index.html')
 
@app.route("/about")
def aboutPage():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}"
    return render_template('form.html')

@app.route('/submitform', methods=['GET', 'POST'])
def submitform():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}"
    return render_template('submit.html')

@app.route('/submit', methods=['GET', 'POST'])
def submitForm():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}"
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)