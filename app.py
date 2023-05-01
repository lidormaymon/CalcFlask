from flask import Flask, render_template
from pages.BP_Plus import plus
from pages.BP_divide import divide
from pages.BP_minus import minus
from pages.BP_multipe import multipe


app = Flask(__name__)   

app.register_blueprint(plus)
app.register_blueprint(divide)
app.register_blueprint(minus)
app.register_blueprint(multipe)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
