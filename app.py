from flask import Flask,render_template,request,redirect,url_for,session
from email_send_test import send_otp
from db_connect import Connector
from otp_generator import otp
from student_model import Student_table
from otp_model import Otp_table
from feedback_model import Feedback_table,Status_table
from functools import wraps
from flask_session import Session
from subject_feedback import Subject_feedback_table

app=Flask(__name__)

app.config['SECRET_KEY']='mysecret key'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# session['login_flag']=0

questions={'one':'1. Has the teacher covered entire syllabus as prescribed by University',
           'two':'2. Has the teacher covered relevant topics beyond syllabus ',
           'three':'3. Effectiveness of teacher in terms of: (a) Technical content/ course content, (b) Communication skills , (c) Use of teaching aids',
           'four':'4. Pace on which contents were covered',
           'five':'5. Motivation and inspiration for students to learn',
           'six':'6. Support for development of Students skill (a) Practical Demonstration (b) Hands on training',
           'seven':'7. Clarity of expectations of students',
           'eight':'8. Feedback provided on students progress ',
           'nine':'9. Willingness to offer help and advice to students ',}

subjects=['18CS81','18CS82','18CS83']

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        usn=request.form.get('usn')
        usn=usn.capitalize()
        session['usn']=usn
        student=Student_table()
        email=student.get_email(usn=usn)
        if email:
            gen_otp=otp()
            otp_table=Otp_table()
            otp_table.add_otp(usn=usn,otp=gen_otp)
            send_otp(email,otp=gen_otp)
            session['email']=email
            return redirect(url_for('otp_login'))
        
        
            
        else:
            return redirect(url_for('home'))
            #return "PLEASE USE VALID USN"
  
    return render_template('home.html',title='Home')

@app.route('/otp_login',methods=['GET','POST'])
def otp_login():
    try:
        if request.method=='POST':
            user_otp=request.form.get('otp')
            usn=session['usn']
            
            if usn:
                if user_otp:
                    otp_table=Otp_table()
                    otp=otp_table.get_otp(usn=usn)
                    if otp==None:
                        return render_template('error.html',error_string="the time may have exceded please re login")
                        #return "the time may have exceded please re login"
                    else:
                        if otp==user_otp:
                            status=Status_table()
                            stud_status=status.get_status(usn=usn)
                            if stud_status==1:
                                return render_template('error.html',error_string="you already submitted feedback")
                                #return "you already submitted feedback"
                            else:
                                session['login_flag']=1
                                return redirect(url_for('feedback'))
                        
                        else:
                            return render_template('error.html',error_string="entered otp doesn't match")
                            #return "entered otp doesn't match"
                        
            else:
                return render_template('error.html',error_string="PLEASE ENTER USN IN LOGIN PAGE FIRST")
                #return "PLEASE ENTER USN IN LOGIN PAGE FIRST"
        if session['email']:
            user_email=session['email'][0]
        else:
            user_email=None
        return render_template('otp_login.html',title="OTP",email=user_email)
    except:
        return render_template('error.html')


@app.route('/feedback',methods=['GET','POST'])
def feedback():
    try:

            
        if request.method=='POST':
            if session['login_flag']==1:
                feedback=request.form.get('feedback')
                usn=session['usn']
                
                for subject in subjects:
                    qa_dict={}
                    for question,val in questions.items():
                        var=" ".join((subject,question))
                        ans=request.form.get(var)
                        try:
                            ans=int(ans)
                            qa_dict[question]=ans

                        except:
                            print("nothing done")
                        
                    sub=Subject_feedback_table(subject=subject)
                    sub.add_subject_rating(subject=subject,rating=qa_dict)
                    
                if usn:
                    status=Status_table()
                    feedback_db=Feedback_table()
                    feedback_db.add_feedback(feedback_text=feedback)
                    status.add_status(usn=usn,status=1)
                    session.clear()
                    return render_template('error.html',error_string="your feedback recorded successfully") 
                    #return "your feedback recorded successfully"
        elif session['login_flag']!=1:
            return render_template('error.html',error_string="please login first don't just put feedback")
            #return "please login first don't just put feedback"      
        return render_template('feedback.html',title="Feedback",subjects=subjects,questions=questions)

    except:
        # return render_template('feedback.html')
        # return redirect(url_for('home'))
        return render_template('error.html',error_string="please login first")
        # return "please login first"



@app.route('/about')
def about():
    return render_template('about.html',title='about')


@app.errorhandler(400)
def not_found(e):
    return "error 400"

if __name__=="__main__":
    app.run(debug=False)