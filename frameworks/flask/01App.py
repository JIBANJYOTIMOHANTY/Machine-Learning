from flask import Flask
''' 
It creates an instance of the Flask class, which is the WSGI(Web Security Gateway Interface) application.
'''

# Create an instance of the Flask class. This instance will be our WSGI application.
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the best Flask App. This should be an amazing course!"

@app.route("/index")
def indexPage():
    return "Welcome to the index page!"

if __name__ == "__main__":
    app.run(debug=True)