from flask import Flask, render_template, request, redirect

app = Flask(__name__)

employees = []

@app.route("/")
def index():
    return render_template("index.html", employees=employees)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        employees.append({
            "name": request.form["name"],
            "dept": request.form["dept"],
            "salary": request.form["salary"]
        })
        return redirect("/")

    return render_template("add.html")


@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(employees):
        employees.pop(index)
    return redirect("/")


@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    if index >= len(employees):
        return redirect("/")

    if request.method == "POST":
        employees[index]["name"] = request.form["name"]
        employees[index]["dept"] = request.form["dept"]
        employees[index]["salary"] = request.form["salary"]
        return redirect("/")

    return render_template("edit.html", employee=employees[index])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
