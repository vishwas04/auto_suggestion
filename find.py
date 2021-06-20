from flask import Flask,render_template,request,jsonify
from predict import get_suggestions ,i2
app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/find",methods=["POST"])
def find():
    x=request.form['x']
    # print(x)
    x=x.lower()
    x=x.split(" ")
    #x=x[:len(x)-1]
    if(x[-1] in i2):
        out=get_suggestions(x)
    else:
        out=get_suggestions(x[:len(x)-1],start_with=x[-1])
    print(out)
    return jsonify({"x":out})

if __name__ == "__main__":
    app.run(debug=True)