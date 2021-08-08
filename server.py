from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def base_checkerboard():
    return render_template('checker.html', numY=4, numX=4)

@app.route('/<int:numY>')
def changeY(numY):
    return render_template('checker.html', numY=numY, numX=4)

@app.route('/<int:numY>/<int:numX>')
def changeXandY(numX, numY):
    return render_template('checker.html', numY=numY, numX=numX)

if __name__=="__main__":
    app.run(debug=True)