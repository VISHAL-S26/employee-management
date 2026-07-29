from flask import Flask,render_template,request,redirect
app=Flask(__name__)
employees=[]
@app.route("/")
def index(): return render_template("index.html",employees=employees)
@app.route("/add",methods=["GET","POST"])
def add():
    if request.method=="POST":
        employees.append({"name":request.form["name"],"dept":request.form["dept"],"salary":request.form["salary"]})
        return redirect("/")
    return render_template("add.html")
if __name__=="__main__": app.run(host="0.0.0.0",port=5000)
