from flask import Blueprint, render_template, request


plus =Blueprint('plus',__name__, url_prefix='/plus')

@plus.route('/', methods=['POST', 'GET'])
def plusHome():
    if request.method == 'POST':
        n1 = int((request.form.get('number1')))
        n2 = int((request.form.get('number2')))
        result = n1 + n2
        return f'result is  {result}'
    else:
        return render_template('plus.html')
    

