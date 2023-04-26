from flask import render_template, url_for, flash, redirect,request,send_file,flash
from Result import app,db,bcrypt
from Result.forms import AdminForm,MarksForm,RegistrationForm,LoginForm
from Result.models import Marks,User
import pandas as pd
from flask_login import login_user,current_user,logout_user,login_required




@app.route("/")
@app.route("/home")


def home():
	return render_template('home.html')


@app.route("/login",methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(Regno=form.Regno.data).first()
		if user and bcrypt.check_password_hash(user.password,form.password.data):
			login_user(user,remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('userDashboard'))
		else:
			flash("Login Unsuccssful","danger")
	if current_user.is_authenticated:
		return redirect(url_for("userDashboard"))
	return render_template('login.html',form=form)

@app.route("/register",methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(name = form.name.data,Regno=form.Regno.data,email=form.email.data,password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Account created for {form.name.data}!', 'success')
		return redirect(url_for('login'))

	if current_user.is_authenticated:
		return redirect(url_for('userDashboard'))

	return render_template('register.html',form=form)

@app.route("/admin",methods=['GET','POST'])
def admin():
	form = AdminForm()
	if form.validate_on_submit():
		if form.email.data == "admin@gmail.com" and form.password.data =="admin":
			return redirect(url_for('adminDashboard'))
	return render_template('adminlogin.html',form=form)



@app.route("/user/dashboard")
def userDashboard():
	return render_template('dashboard/user.html')


@app.route("/admin/dashboard")
def adminDashboard():
	form = MarksForm()
	if form.validate_on_submit():
		exam_type = form.exam_type.data
		semester = form.semester.data
		return redirect(url_for('upload',exam_type=exam_type,semester=semester,form=form))
	return render_template('dashboard/admin.html',form=form)

@app.route('/upload', methods=['POST'])
def upload():
	file = request.files['marks_file']
	exam_type = request.form['exam_type']
	semester = request.form['semester']

	if file and file.filename.endswith(('.xls', '.xlsx', '.csv')):
		df = pd.read_excel(file)
		for index, row in df.iterrows():
			mark = Marks(name=row['name'],semester = semester,exam_type=exam_type,subject1_marks = row['subject1'],subject2_marks=row['subject2'],subject3_marks = row['subject3'],subject4_marks = row['subject4'],subject5_marks = row['subject5'],subject6_marks = row['subject6'])
			db.session.add(mark)
		db.session.commit()
		flash('File Uploaded','success')
		return redirect(url_for('adminDashboard'))





@app.route('/templates/sem-1-1')
def files():
	return "<h1> files is downloading</h1>"