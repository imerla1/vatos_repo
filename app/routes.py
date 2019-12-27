from flask import render_template, redirect, url_for, flash
from app.form import InputField
from app import app



def calculate(n):
    'Tu n udris 1-s daabrunebs 1-s sxva shemtxveashi output lists emateba yvela mteli gamyofi magrad daabrunebs lists meore wevrs'
    i = 1
    ai = [] # Output list
    while i <= n: 
        if (n % i==0) : 
            ai.append(i)
        i = i + 1

    if n == 1:
        return 1
    else:
        return ai[1]


methods = ["GET", "POST"]

@app.route('/', methods=methods)
@app.route('/index', methods=methods)
def index():
    form = InputField()
    if form.validate_on_submit():
        number = form.num_input.data
        try:
            x = int(number)
            flash("Calculate Finished Succesfully", 'success')
            return redirect(url_for('result', number=number))
            

        except:
            
            flash("Please Enter Valid Input", 'danger')

    return render_template('index.html', form=form)

@app.route('/result/<number>', methods=methods)
def result(number):
    res = calculate(int(number))
    return render_template('result.html', number=number, calculate=calculate, res=res)

