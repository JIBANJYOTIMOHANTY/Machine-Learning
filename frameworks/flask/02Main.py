from flask import Flask, render_template
''' 
It creates an instance of the Flask class, which is the WSGI(Web Security Gateway Interface) application.
'''

# Create an instance of the Flask class. This instance will be our WSGI application.
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask course</h1></html>"

@app.route("/index")
def indexPage():
    return render_template('index.html')
 
@app.route("/about")
def aboutPage():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)