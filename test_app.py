from flask import Flask,render_template


app=Flask(__name__)
questions={'1':'question 1 its a long logn dafkdjjajdfijnsf iaidjkjfdsjf kajiewnfk  dskfjiasjfijdskfm ijfkdjfie jfkfkdjfija sidfjkajf','2':'question 2','3':'question 3'}

@app.route('/')
def home():
    return render_template('feedback.html',title="Feedback",subjects=['18CS81','18CS82'],questions=questions)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=False)