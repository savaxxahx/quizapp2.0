import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set in Heroku (Settings->Config Vars).  

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear()
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/terms')
def renderPage1():
    return render_template('page1.html')

@app.route('/answering',methods=['GET','POST'])
def renderPage2():
    session[vocabTerms1] = request.form["vocabTerms1"]
    session[vocabTerms2] = request.form["vocabTerms2"]
    return render_template('page2.html')
    
@app.route('/correctornot',methods=['GET','POST'])
def renderPage3():
    session[vocabAnswers] = request.form["vocabAnswers"]
    return render_template('page3.html')
  
@app.route('/grading',methods=['GET','POST'])
def renderPage4():
    session[grade] = request.form["grade"]
    return render_template('page4.html')
    
if __name__=="__main__":
    app.run(debug=False)
