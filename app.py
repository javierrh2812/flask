from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        print(request.form, request.method)
        #if email in users and users[email] == password:
        #    return render_template("login.html", message ="Successfully Logged In")
        return render_template("login.html", message ="From post login")
    return render_template("login.html")


@app.route('/square/<int:number>')
def show_square(number):
    """View that shows the square of the number passed by URL"""
    return "Square of "+ str(number) +" is: "+ str(number * number)

@app.route('/<my_name>')
def greatings(my_name):
    """View function to great the user bby name"""
    return "Welcome " + my_name + "!!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)


