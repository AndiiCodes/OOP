from flask import Flask, render_template, redirect, request, url_for , session
from collections import OrderedDict

app = Flask(__name__)

app.secret_key = 'sadasdas'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fees', methods=['GET', 'POST'])
def fees():
    if request.method == 'POST':
        name = request.form.get('name')
        id = request.form.get('id')
        institution = request.form.get('institution')
        campusLocation=request.form.get('campus-l')
        programCode = request.form.get('program-c')
        programName = request.form.get('program-name')
        courseCode = request.form.get('course-c')

        session['formData'] = OrderedDict([
            ('name' , name),
            ('id' , id),
            ('institution' , institution),
            ('camputLocation' , campusLocation),
            ('programCode' , programCode),
            ('programName' , programName),
            ('courseCode' , courseCode),
        ])
        
        return redirect(url_for('output'))

    return render_template('fees.html')

@app.route('/output')
def output():
    data= session.get('formData' , OrderedDict())
    session.pop('data',None)
    print(data)
    return render_template('output.html' , data=data)

if __name__ == '__main__':
    app.run(debug=True)
