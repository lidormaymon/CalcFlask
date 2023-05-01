from flask import Blueprint, render_template, request


minus = Blueprint('minus',__name__, url_prefix='/minus')

@minus.route('/', methods=['POST', 'GET'])
def minusHome():
    if request.method == 'POST':
        n1 = int((request.form.get('number1')))
        n2 = int((request.form.get('number2')))
        result = n1 - n2
        return f'result is  {result}'
    else:
        return render_template('minus.html')