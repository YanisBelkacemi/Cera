from nera import app
from flask import render_template , redirect , url_for , flash , request
from nera.forms import posting , register , login 
from nera.models import post , user
from nera import db
from flask_login import current_user, login_required, login_user , logout_user

@app.errorhandler(404)
def error404(error):
    error = '404'
    return render_template("404.html", error = error),404
@app.errorhandler(401)
def error401(error):
    error = '401'
    return render_template('404.html' , error = error), 401
@app.errorhandler(500)
def error401(error):
    error = '500'
    return render_template('404.html', error = error), 500
@app.errorhandler(405)
def error401(error):
    error = '405'
    return render_template('404.html', error = error), 405



@app.route('/', methods = ["POST","GET"])
@app.route('/home', methods = ["POST", "GET"])
def home():
    page_num = request.args.get('page' , 1 , type=int)
    form = posting()
    data = post.query.order_by(post.date.desc()).paginate( page= page_num  , per_page = 10)
    if current_user.is_authenticated == False:
        flash("You are not loged in please login or register!")
    if form.validate_on_submit():
        if current_user.is_authenticated:
            newpost = post(text = form.text.data,
                            author = current_user.username,
                           )
            db.session.add(newpost)
            db.session.commit()
            return redirect(url_for('home'))
        elif current_user.is_authenticated == False:
            form.text.data = ""
    if form.errors != {}:
        print(form.errors)
    return render_template('home.html' , form=form, datas = data)

@app.route("/register" , methods = ["POST","GET"])
def Register():
    form = register()
    if form.validate_on_submit():
        newuser = user( username = form.firstname.data + " " + form.familyname.data,
                        password = form.password.data,
                        Email = form.Email.data,
                        ip = request.remote_addr
                        )
        db.session.add(newuser)
        db.session.commit()
        login_user(newuser)
        return redirect(url_for("home"))
    return render_template('register.html' , form = form)
@app.route("/login", methods = ["POST","GET"] )
def loginpage():
    form = login()
    if form.validate_on_submit():
        attempted_user = user.query.filter_by(username= form.username.data).first()
        if attempted_user and attempted_user.check_pass(entpassword = form.password.data) :
            login_user(attempted_user)
            return redirect(url_for('home'))
    return render_template("login.html" , form = form)
@app.route("/accounts/<int:id>=<name>", methods = ["POST","GET"])
def account(id , name):

    return render_template("account.html", account = account)


@app.route("/chat")
def chat():
    return render_template('chat.html')


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("loginpage"))
@app.route("/map" , methods = ["POST" , "GET"])
def map():
    

    return render_template("Mylocation.html")
    
@app.route("/more")
@login_required
def more():
    
    return render_template("more.html" )


@app.route("/admin" , methods = ['POST', 'GET'])
@login_required
def admin():
    users = user.query.all()
    posts = post.query.all()
    id = current_user.id

    if id == 1 or id == 0:
        return render_template("admin_login.html" , users = users, posts = posts )
    else:
        error = "Permission denied!"
        return render_template("404.html" , error = error)




    