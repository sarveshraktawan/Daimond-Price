from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method=='POST':
        carat = request.form.get('carat')
        table = request.form.get('table')
        x = request.form.get('x')
        y = request.form.get('y')
        z = request.form.get('z')
        color_encoded = request.form.get('color_encoded')
        return render_template('sucess.html',data = {'Diamond Price':69897})
    else:
        return render_template('predict.html')





if __name__ == "__main__":
    app.run()