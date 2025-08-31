from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/submit2', methods=['GET', 'POST'])
def submitForm():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}"
    return render_template('form.html')

# Variable rule
# This is a variable rule that captures an integer value from the URL and passes it to the function as a parameter. The variable part of the URL is enclosed in angle brackets (< >) and can be of different types (int, float, string, etc.). In this case, the variable part is named "score" and it is expected to be an integer.
@app.route('/success/<int:score>')
def success(score):
    return f"Your score is {str(score)}"


@app.route('/successres/<int:score>')
def result(score):
    res = ""
    if score >= 33:
        res = "PASS"
    else:
        res = "FAIL"
    
    exp = {'score' : score, 'res' : res}
    return render_template('result.html', results=exp)


@app.route('/resultIf/<int:score>')
def resultIf(score):
    res = ""
    return render_template('result1.html', results=score)


@app.route('/submitform', methods = ['POST', 'GET'])
def getResult(score):
    res = ""
    return render_template('result1.html', results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('result',score=total_score))
            

if __name__ == "__main__":
    app.run(debug=True)