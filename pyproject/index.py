from flask import *
import mysql.connector
import uuid
import time
import enchant
from better_profanity import profanity
from nltk.tokenize import word_tokenize
dict = enchant.Dict("en_US")

app= Flask(__name__)
app.secret_key=uuid.uuid4().hex

myconn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="M@nnu$14520",
  database="newfeedbackschema"
)

@app.route("/")
def mainpage():
	return render_template("homepage.html")

@app.route("/admin",methods=['GET','POST'])
def admin():
	if request.method=="POST":
		uname=request.form['uname']
		pwd=request.form['pwd']
		cur=myconn.cursor()
		type = 'Student'
		cur.execute("select * from login where username=%s and userpasswd=%s and usertype=%s" ,(uname,pwd,type))
		data=cur.fetchall()
		if data:
			session['loggedin']=True
			print(session)
			flash("Login successfully")
			cur = myconn.cursor()
			cur.execute("SELECT * FROM courseteacher")
			data = cur.fetchall()
			print(data)
			return render_template("feedback.html",uname=uname,data=data)#,uname=uname) #for student login
		else:
			flash("Invalid username or password")
			return render_template("admin.html")
	else:
		return render_template("admin.html")

#for teacher login
# @app.route("/") #index page
@app.route("/teacherAdmin",methods=['GET','POST'])
def admin1():
	if request.method=="POST":
		uname=request.form['uname']
		pwd=request.form['pwd']
		cur=myconn.cursor()
		type = 'Teacher'
		cur.execute("select * from login where username=%s and userpasswd=%s and usertype=%s" ,(uname,pwd,type))
		data=cur.fetchall()
		if data:
			cur.execute("select * ,((q1+q2+q3)/3) as score_avg from feedback_table where teachername=%s",(uname,))
			data1 = cur.fetchall()
			session['loggedin']=True
			flash("Login successfully")
			return render_template("viewnew.html",data = data1) #for teacher login
		else:
			flash("Invalid username or password")
			return render_template("adminteacher.html")
	else:
		return render_template("adminteacher.html")


# @app.route("/newevent",methods=['GET','POST'])
# def newevent():
# 	if not session.get('loggedin'):
# 		return render_template("admin.html")
# 	if request.method=="POST":
# 		event_name=request.form['event_name']
# 		course=request.form.getlist('course') #["Python","RPA","WT"]
# 		course=','.join(course) #"Python,RPA,WT"
# 		mycur=myconn.cursor()
# 		mycur.execute("""insert into event1(event_name,courses)values(%s,%s)""",(event_name,course))
# 		myconn.commit()
# 		flash("Event created successfully")
#
# 		return redirect(url_for('newevent'))
# 	else:
# 		return render_template("index.html")
#
# @app.route("/register",methods=['GET','POST'])
# def register():
# 	if request.method == "POST":
# 		rollno=request.form['rollno']
# 		name=request.form['name']
# 		email=request.form['email']
# 		phno=request.form['phno']
# 		college=request.form['college']
# 		branch=request.form['branch']
# 		section=request.form['section']
# 		gen=request.form['gender']
# 		event_name=request.form['event_name']
# 		course=request.form['course']
# 		mycur=myconn.cursor()
# 		mycur.execute("select * from students where rollno=%s and eventname=%s and courses=%s",(rollno,event_name,course))
# 		data=mycur.fetchall()
# 		if len(data)==0:
# 			mycur.execute("""insert into students(rollno,name,college,branch,section,email,
# 			phno,gender,event_name,courses)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
# 			(rollno,name,college,branch,section,email,phno,gen,event_name,course))
# 			myconn.commit()
# 			flash("Registered Successfully")
# 		# else:
# 			# flash("Already registered")
# 		return redirect(url_for('register'))
# 	else:
# 		cur=myconn.cursor()
# 		cur.execute("SELECT DISTINCT event_name FROM `event1` where status=2")
# 		data=cur.fetchall()
# 		return render_template("reg.html",data=data)
#
# @app.route("/justcreated",methods=['GET','POST'])
# def justcreated():
# 	if not session.get('loggedin'):
# 		return render_template("admin.html")
# 	cur=myconn.cursor()
# 	cur.execute("select * ,((q1+q2+q3)/3) as score_avg from feedback_table")
# 	data=cur.fetchall()
# 	print(data)
# 	return render_template("view.html",data=data)
#
# @app.route("/regopened",methods=['GET','POST'])
# def regopened():
# 	if request.method=="POST":
# 		id=request.form['regopened']
# 		cur=myconn.cursor()
# 		cur.execute("update event1 set status=2 where sno=%s"%(id))
# 		myconn.commit()
# 		return redirect(url_for('regopened'))
# 	if not session.get('loggedin'):
# 		return render_template("admin.html")
# 	cur=myconn.cursor()
# 	cur.execute("select * from event1 where status=2")
# 	data=cur.fetchall()
# 	print(data)
# 	return render_template("status2.html",data=data)
#
# @app.route("/regclosed",methods=['GET','POST'])
# def regclosed():
# 	if request.method=="POST":
# 		id=request.form['regclosed']
# 		cur=myconn.cursor()
# 		cur.execute("update event1 set status=3 where sno=%s"%(id))
# 		myconn.commit()
# 		return redirect(url_for('regclosed'))
# 	if not session.get('loggedin'):
# 		return render_template("admin.html")
# 	cur=myconn.cursor()
# 	cur.execute("select * from event1 where status=3")
# 	data=cur.fetchall()
# 	print(data)
# 	return render_template("status3.html",data=data)
#
# @app.route("/eventclosed",methods=['GET','POST'])
# def eventclosed():
# 	if request.method == "POST":
# 		event_name=request.form['event_name']
# 		course=request.form['course']
# 		cur=myconn.cursor()
# 		cur.execute("select * from students where event_name=%s and courses=%s",(event_name,course))
# 		records=cur.fetchall()
# 		cur.execute("SELECT DISTINCT event_name FROM `event1` where status=3")
# 		data=cur.fetchall()
#
# 		return render_template("ucs.html",records=records,data=data)
# 	else:
# 		cur=myconn.cursor()
# 		cur.execute("SELECT DISTINCT event_name FROM `event1` where status=3")
# 		data=cur.fetchall()
# 		return render_template("ucs.html",data=data)
#
# @app.route("/delete",methods=['GET','POST'])
# def delete():
# 	if not session.get('loggedin'):
# 		return render_template("admin.html")
# 	if request.method == "POST":
# 		id=request.form['delete']
# 		cur=myconn.cursor()
# 		cur.execute("delete from event1 where sno=%s"%(id))
# 		myconn.commit()
# 		flash("Deleted successfully")
# 		return redirect(url_for('justcreated'))
#
# @app.route("/edit",methods=['GET','POST'])
# def edit():
# 	if not session.get('loggedin'):
# 		return render_template("admin.html")
# 	if request.method == "POST":
# 		id=request.form['edit']
# 		cur=myconn.cursor()
# 		cur.execute("select * from event1 where sno=%s"%(id))
# 		data=cur.fetchall()
# 		course=data[0][2].split(',')
# 		return render_template("edit.html",data=data,course=course)
#
# @app.route("/update",methods=['GET','POST'])
# def update():
# 	if not session.get('loggedin'):
# 		return render_template("admin.html")
# 	if request.method=="POST":
# 		id=request.form['id']
# 		event_name=request.form['event_name']
# 		course=request.form.getlist('course')
# 		course=','.join(course)
# 		mycur=myconn.cursor()
# 		mycur.execute("update event1 set event_name=%s,courses=%s where sno=%s",(event_name,course,id))
# 		myconn.commit()
# 		flash("Updated successfully")
# 		return redirect(url_for('justcreated'))

@app.route("/feedback",methods=['GET','POST'])
def feedback():
	cur1 = myconn.cursor()
	cur1.execute("SELECT * FROM courseteacher")
	data = cur1.fetchall()
	if request.method == "POST":
		print(session['loggedin'])
		uname=request.form['uname']
		coursename=request.form['coursename']
		teachername=request.form['teachername']
		cur=myconn.cursor()
		cur.execute("Select * from courseteacher where coursename=%s and tearchername=%s",(coursename,teachername))
		records = cur.fetchall()
		print("records::",records)

		if records !=[]:
		# cur.execute("select * from students where rollno=%s and eventname=%s and courses=%s",(rollno,event_name,course))
		# records=cur.fetchall()
		# if records:
		# 	cur1 = myconn.cursor()
		#and coursename=%s
			print(coursename)
			cur.execute("select * from feedback_table where username=%s  and teachername=%s",(uname,teachername))
			data=cur.fetchall()
			print("data::",data)
			if len(data)==0:
				# flash("Feedback submitted successfully")
				return render_template("fbform.html",uname=uname,coursename=coursename,teachername=teachername)
			else:
				flash("You had already given the feedback")
				return render_template("feedback.html", uname=uname, data=data)
				
		else:
			flash("Wrong combination of Course and Teacher selected!!")
			return render_template("feedback.html",uname=uname,data=data)
	else:
		return render_template("feedback.html",data=data)

@app.route("/feedbackpage",methods=['GET','POST'])
def feedbackpage():
	if request.method=='POST':
		uname=request.form['uname']
		coursename=request.form['coursename']
		teachername=request.form['teachername']
		print(uname,coursename,teachername)
		secq=request.form['secq']
		thirdq=request.form['thirdq']
		fourthq=request.form['fourthq']
		comment=request.form['comment']
		cur=myconn.cursor()
		print(comment)
		# cur.execute("""insert into feedback_table(username,coursename,teachername,q1,q2,q3,comment)
		# 	values(%s,%s,%s,%s,%s,%s,%s)""",(uname,coursename,teachername,secq,thirdq,fourthq,comment))
		# myconn.commit()
		
		#profanity-check
		# custom_badwords = ['abusive']
		# profanity.add_censor_words(custom_badwords)
		path = "E:\\my data\\Downloads\\hello_MANTHAN\\hello_MANTHAN\\Feedback-system-project-master\\Feedback-system-project-master\\pyproject\\"
		filename = path+'profanity_wordlist.txt'
		profanity.load_censor_words_from_file(filename)
		# text = "Your course is shit."
		censored_text = profanity.censor(comment)
		censored_text_check = profanity.contains_profanity(comment)
		print(censored_text, censored_text_check)
		
		#misspelled words
		words = word_tokenize(comment)
		misspelled = []
		for word in words:
			if dict.check(word) == False:
				misspelled.append(word)
		print("The misspelled words are : " + str(misspelled))
		for word in misspelled:
			print("Suggestion for " + word + " : " + str(dict.suggest(word)))
			
		if censored_text_check == True:
			flash("ALERTT... Bad language found. Please correct before sending your feedback!")
			return render_template("fbform.html", uname=uname, coursename=coursename, teachername=teachername,)
		else:
			if misspelled == []:
				cur.execute("""insert into feedback_table(username,coursename,teachername,q1,q2,q3,comment)
									values(%s,%s,%s,%s,%s,%s,%s)""",
				            (uname, coursename, teachername, secq, thirdq, fourthq, comment))
				myconn.commit()
				flash("Feedback submitted successfully!")
				return render_template("admin.html")
			else:
				flash("Misspelled words found are.."+str(misspelled)+". Please correct before sending your feedback!")
			# return redirect(url_for('feedback'))
				return render_template("fbform.html",uname=uname,coursename=coursename,teachername=teachername,wrong=','.join(misspelled))

@app.route("/viewfeedback",methods=['GET','POST'])
def viewfeedback():	
	if request.method=='POST':
		course=request.form['course']
		cur=myconn.cursor()
		cur.execute("SELECT q1,q2,q3  FROM `feedback_table` where course=%s",(course,))
		percentage=cur.fetchall()
		percentage = (((int(percentage[0][0]) + int(percentage[0][1]) + int(percentage[0][2])) * 100) / 15)
		# percentage=int(percentage[0][0])
		cur.execute("SELECT DISTINCT course FROM `feedback_table`")
		data=cur.fetchall()
		return render_template("viewfeedback.html",data=data,percentage=percentage,course=course)	
	else:
		cur=myconn.cursor()
		cur.execute("SELECT DISTINCT course FROM feedback_table")
		data=cur.fetchall()
		return render_template("viewfeedback.html",data=data)


@app.route("/logout")
def logout():
	session['loggedin']=False
	flash("You are successfully logged out.")
	return render_template("admin.html")

@app.route("/logoutTeacher")
def logoutTeacher():
	session['loggedin']=False
	flash("You are successfully logged out.")
	return render_template("adminteacher.html")

# @app.route("/process",methods=['GET','POST'])
# def process():
# 	course=request.form['event']
# 	cur=myconn.cursor()
# 	cur.execute("""select courses from event1 where event_name=%s""",(course,))
# 	data=cur.fetchall()
# 	print(data)
# 	data=data[0][0]
# 	data=data.split(',')
# 	print(data)
# 	return jsonify({'course':data})

#
# @app.route("/details",methods=['GET','POST'])
# def details():
# 	if request.method=='POST':
# 		ids=request.form.getlist('ids')
# 		cur=myconn.cursor()
# 		for id in ids:
# 			cur.execute("update students set status=1 where sno=%s",(id,))
# 			myconn.commit()
# 		return redirect(url_for('eventclosed'))


if __name__=="__main__":
	app.run(debug=True,port=5008)
