from flask import Flask,render_template,flash,request,session,redirect
from surveys import satisfaction_survey as survey


app=Flask(__name__)
responses =[]


app.config['SECRET_KEY'] = 'itsasekrit'

@app.route("/")
def home():

    return render_template('start_survey.html',survey=survey)

@app.route('/begin', methods=['POST'])
def start_survey():
    return redirect('/question/0')



@app.route('/question/<int:id>')
def get_question(id):

    question = survey.questions[id]




    return render_template('question.html',question=question,id=id)

@app.route('/answer',methods=['POST'])
def get_answer():

    choice = request.form['answer']

    responses.append(choice)
    l1= {len(responses)}
    l2={len(survey.questions)}

    if l1 ==l2:
        message=flash("Thanks for Taking the Survey")
        return render_template('complete_survey.html',answers=responses,message=message,survey=survey)
    else:

        return redirect(f"question/{len(responses)}")