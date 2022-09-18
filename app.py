from flask import Flask ,render_template as r ,request , redirect ,flash  ,url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import requests
import os
server = Flask(__name__)
db = SQLAlchemy(server)
server.secret_key = 'super secret key'
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tesla.sqlite3'
UPLOAD_FOLDER='static/img/'
server.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
class Products(db.Model):
    __tablename___="page_tshirt"
    id           = db.Column(db.Integer, primary_key=True)
    date         = db.Column(db.BLOB)#LargeBinary
    filename     = db.Column(db.String(999))
    title        = db.Column(db.String(999)) 
    description  = db.Column(db.String(999)) 
    prix         = db.Column(db.String(999))
    def __init__(self,date,filename,title,description,prix):
        self.filename = filename
        self.date     = date
        self.title    = title
        self.description = description
        self.prix     = prix
class Products_totebag(db.Model):
    __tablename___="page_totebag"
    id           = db.Column(db.Integer, primary_key=True)
    date         = db.Column(db.BLOB)#LargeBinary
    filename     = db.Column(db.String(999))
    title        = db.Column(db.String(999)) 
    description  = db.Column(db.String(999)) 
    prix         = db.Column(db.String(999))
    def __init__(self,date,filename,title,description,prix):
        self.filename = filename
        self.date     = date
        self.title    = title
        self.description = description
        self.prix     = prix
class Products_pp(db.Model):
    __tablename___="page_pp"
    id           = db.Column(db.Integer, primary_key=True)
    date         = db.Column(db.BLOB)#LargeBinary
    filename     = db.Column(db.String(999))
    title        = db.Column(db.String(999)) 
    description  = db.Column(db.String(999)) 
    prix         = db.Column(db.String(999))
    def __init__(self,date,filename,title,description,prix):
        self.filename = filename
        self.date     = date
        self.title    = title
        self.description = description
        self.prix     = prix
@server.route('/admin/dash')
def dash():
    return r('dash.html')
@server.route('/admin/dash/new_tshirt',methods=['GET','POST'])
def new_tshirt():
    if request.method == 'POST':
      if not request.form['title'] or not request.form['description'] or not request.form['prix']:
         flash('Please enter all the fields', 'error')
      else:
         file = request.files['file']
         #file.save(file.filename)
         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),server.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
      #file.save(os.path.join(app.config['UPLOAD_FOLDER']))
         pd = Products(title = request.form['title'], description = request.form['description'], 
            prix = request.form['prix'], filename=file.filename, date=file.read())
         db.session.add(pd)
         db.session.commit()
         return redirect('/')
    return r('add_products/new_index.html', products = Products.query.all())

@server.route('/admin/dash/new_totebag',methods=['GET','POST'])
def new_totebag():
    if request.method == 'POST':
      if not request.form['title'] or not request.form['description'] or not request.form['prix']:
         flash('Please enter all the fields', 'error')
      else:
         file = request.files['file']
         #file.save(file.filename)
         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),server.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
      #file.save(os.path.join(app.config['UPLOAD_FOLDER']))
         pd = Products_totebag(title = request.form['title'], description = request.form['description'], 
            prix = request.form['prix'], filename=file.filename, date=file.read())
         db.session.add(pd)
         db.session.commit()
         return redirect('/')
    return r('add_products/new_totebag.html', products = Products_totebag.query.all())

@server.route('/admin/dash/new_pp',methods=['GET','POST'])
def new_pp():
    if request.method == 'POST':
      if not request.form['title'] or not request.form['description'] or not request.form['prix']:
         flash('Please enter all the fields', 'error')
      else:
         file = request.files['file']
         #file.save(file.filename)
         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),server.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
      #file.save(os.path.join(app.config['UPLOAD_FOLDER']))
         pd = Products_pp(title = request.form['title'], description = request.form['description'], 
            prix = request.form['prix'], filename=file.filename, date=file.read())
         db.session.add(pd)
         db.session.commit()
         return redirect('/')
    return r('add_products/new_pp.html', products=Products_pp.query.all())

@server.route('/')
def index():
    return r('index.html',product = Products.query.all())

@server.route('/totebag')
def totebag():
    return r('totebag.htm',product = Products_totebag.query.all())

@server.route('/printingpersone')
def pp():
    return r('pp.html',product = Products_pp.query.all())

@server.route('/buy/<int:id>/<string:title>/<string:prix>/<string:description>/<string:filename>', methods=['GET','POST'])
def buy(id,title,prix,description,filename):
    if request.method=='POST':
        id         =  id
        title      =  title
        prix       =  prix
        filename   =  filename
        description=  description
    return r('buy.html', id=id , title=title , prix=prix , description=description , filename=filename,)

@server.route('/buy/products/<int:id>/<string:title>', methods=['POST', 'GET'])
def rt(id,title):
    if request.method=='POST':
        fullname = request.form['fullname']
        adress   = request.form['adress']
        tel      = request.form['tel']
        id       = id 
        title    = title
        TOKEN = "5501495930:AAFdc-5WHgPAhNELTWcRzY_rqmj81x7g3F0"
        chat_id = "1966259244"
        text = f"\n>>>Fullname : \n"+fullname+"\n>>>Address : \n"+adress+"\n>>>Telephone : \n"+tel+"\n<<<Title :\n"+title+"\n<<<Id : \n{}".format(id)
        url = 'https://api.telegram.org/bot'+ TOKEN +'/sendMessage?chat_id='+ chat_id +'&text='+ text
        r = requests.get(url)
        print('ok!')
        return redirect('/') ,r.json()
    else:
        return 'not found api'

@server.route('/delete/Pb/<int:id>',methods=['GET','POST'])
def deletesPt(id):
    productss = Products_totebag.query.filter_by(id=id).first()
    if request.method=='POST':
        if productss:
            db.session.delete(productss)
            db.session.commit()
            flash("ok!")  
    return redirect('/')

@server.route('/delete/Pp/<int:id>',methods=['GET','POST'])
def deletesPp(id):
    productss = Products_pp.query.filter_by(id=id).first()
    if request.method=='POST':
        if productss:
            db.session.delete(productss)
            db.session.commit()
            flash("ok!")  
    return redirect('/')   

@server.route('/delete/Pt/<int:id>',methods=['GET','POST'])
def deletesPb(id):
    productss = Products.query.filter_by(id=id).first()
    if request.method=='POST':
        if productss:
            db.session.delete(productss)
            db.session.commit()
            flash("ok!")  
    return redirect('/')     

@server.route('/bass')
def dass():
    return r('layout/base_dash.html')

if __name__=="__main__":
    db.create_all()
    server.run(debug=True)
