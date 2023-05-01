from flask import Blueprint, render_template, request


divide = Blueprint('divide',__name__, url_prefix='/divide')

@divide.route('/', methods=['POST', 'GET'])
def divideHome():
    if request.method == 'POST':
        n1 = int((request.form.get('number1')))
        n2 = int((request.form.get('number2')))
        result = n1 // n2
        return f'result is  {result}'
    else:
        return render_template('divide.html')