from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home_pge():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_pge(page_name):
    return render_template(page_name)


def writetotxtfile(p1data):
    with open('database.txt', mode='a') as dbtxtfile:
        email = p1data['email']
        subject = p1data['subject']
        message = p1data['message']
        txtfile = dbtxtfile.write(f'\n {email}, {subject}, {message}')


def writetocsvfile(p2data):
    with open('database.csv', mode='a', newline='') as db_csv_file:
        email = p2data['email']
        subject = p2data['subject']
        message = p2data['message']
        o_csv_writer = csv.writer(db_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        o_csv_writer.writerow([email, subject, message])

 # newline='',

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        writetotxtfile(data)
        writetocsvfile(data)
        return redirect('thanku.html')
    else:
        return 'something went wrong please try again'

# @app.route('/about.html')
# def about_pge():
#     return render_template('about.html')
#
# @app.route('/works.html')
# def works_pge():
#     return render_template('works.html')

#


## for windows cmd
## cd C:\Users\pro81\Videos\Captures\webserver_playground
## set FLASK_APP=server0001.py
## set FLASK_ENV=development
## flask run
## http://127.0.0.1:5000/


##
##
##
##from flask import Flask, render_template,url_for
##app = Flask(__name__)
##print(__name__)
##
####@app.route('/')
####def cdagi():
####    return 'I am the most Powerful person'
##
####@app.route('/blog')
####def blogg():
####    return 'My Name is Barkha Tiwari'
####@app.route('/blog/sanjay/girlfriends')
####def gf():
####    return 'I have Fifty one girlfriends'
####@app.route('/sanjay')
####def snj():
####    return render_template('scratch1.html')
##
##@app.route('/<usrnme>')
##def rot(usrnme = None):
##    return render_template('inddex1.html',nme =usrnme)


## for windows cmd
## C:\Users\pro81\Videos\Captures\webserver_playground
## set FLASK_APP=serrver.py
## flask run
## http://127.0.0.1:5000/


##from flask import Flask
##app = Flask(__name__)
####print(__name__)
##
##@app.route('/')
##def hello_world():
##    return 'Sanjay Barkha Shobha'


## Flask run
