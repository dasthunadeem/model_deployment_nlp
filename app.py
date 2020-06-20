from flask import Flask,render_template,url_for,redirect
from forms import Input_Form
import pickle

app=Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
model= pickle.load(open('model.pkl','rb'))
cv= pickle.load(open('cv.pkl','rb'))

@app.route('/',methods=['GET','POST'])
def home():	
	return render_template('home.html',title='Result')


@app.route('/result',methods=['GET','POST'])
def result():
	form=Input_Form()
	if form.validate_on_submit():	
		message=[form.text.data]
		message=cv.transform(message).toarray()
		result=model.predict(message)
		if result ==1:
			a='Postive Review'
		else:
			a='Negetive Review'
		return render_template('result.html', title='Result',a=' Prediction : {}'.format(a),form=form)
	return render_template('result.html', title='Result',form=form)

if __name__ == ('__main__'):
    app.run(debug=True)
    