import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    category_recipes = mongo.db.categories.find().sort(
        "category_name", -1).limit(6)
    recipes = list(mongo.db.recipes.find())
    return render_template("index.html", recipes=recipes,
                           category_recipes=category_recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    register new user and insert new user into session cookie
    """
    if request.method == "POST":
        confirm_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if confirm_user:
            flash("Sorry but the username choosen is taken," +
                  "try another")
            return redirect(url_for("register"))

        confirm_password1 = request.form.get("password")
        confirm_password2 = request.form.get("confirm-password")
        if confirm_password1 != confirm_password2:
            flash("Passwords do not match, try again!")
            return redirect(url_for("register"))

        register_user = {
            "full_name": request.form.get("full-name").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "about": request.form.get("aboutme")
        }
        mongo.db.users.insert_one(register_user)

        session["user"] = request.form.get("username").lower()
        flash("Congratulations! Account created")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Function allows user to log to their account,
    check if the user has been created already    
    and if password exist if not found display an error.
    """
    if request.method == "POST":
        confirm_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if confirm_user:
            if check_password_hash(
                    confirm_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Hola! Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Sorry the details provided do not" +
                      "match our system try again!")
                return redirect(url_for("login"))

        else:
            flash("Username and Password invalid, try again")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>")
def profile(username):
    """
    retrieve user and recipe information from the dabase
    """
    if "user" in session:
        if session["user"] == username:
            user = mongo.db.users.find_one(
                {"username": session["user"]})
            recipes_user = mongo.db.recipes.find(
                {"created_by": session["user"]})
            return render_template(
                "profile.html", user=user, recipes_user=recipes_user)
        else:
            flash("Please try Login again")
    
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You've been logged out !")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    Check if the user is logged in
    and add recipe to
    the user profile.
    """
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    if "user" in session:
        if request.method == "POST":
            is_vegetarian = "on" if request.form.get(
                                    "is_vegetarian") else "off"
            recipe = {
                "recipe_name": request.form.get("recipe_name"),
                "recipe_description": request.form.get("recipe_description"),
                "ingredients": request.form.getlist("ingredients"),
                "recipe_instructions": request.form.getlist(
                                            "recipe_instructions"),
                "recipe_time": request.form.get("recipe_time"),
                "category_name": request.form.getlist("category_name"),
                "is_vegetarian": is_vegetarian,
                "image_url": request.form.get("image_url"),
                "rate": request.form.get("rate"),
                "created_by": session["user"]
            }
            mongo.db.recipes.insert_one(recipe)
            flash("Recipe sucessfully created")
            return redirect(url_for("profile", username=session["user"]))

        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template(
            "addrecipe.html", categories=categories, user=user)
    else:
        flash("Please Login/Signup to create a recipe ")
        return redirect(url_for("login"))


@app.route("/single_recipe/<recipe_id>")
def single_recipe(recipe_id):
    """
    Display single recipe details.
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("single-recipe.html", recipe=recipe)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    If the user is logged in
    allow user edit the recipe
    and return to recipe profile.
    """
    if "user" in session:
        if request.method == "POST":
            is_vegetarian = "on" if request.form.get(
                                    "is_vegetarian") else "off"
            submit = {
                "recipe_name": request.form.get("recipe_name"),
                "recipe_description": request.form.get("recipe_description"),
                "ingredients": request.form.getlist("ingredients"),
                "recipe_instructions": request.form.getlist(
                                            "recipe_instructions"),
                "recipe_time": request.form.get("recipe_time"),
                "category_name": request.form.getlist("category_name"),
                "is_vegetarian": is_vegetarian,
                "image_url": request.form.get("image_url"),
                "rate": request.form.get("rate"),
                "created_by": session["user"]
            }
            
            mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {"$set": submit})
            flash("Recipe sucessfully updated")
            return redirect(url_for("single_recipe",recipe_id=recipe_id))
    
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit-recipe.html",
                            recipe=recipe, 
                            categories=categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    Allow user delete recipe created
    """
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe sucessfully deleted")
    return redirect(url_for('profile', username=session["user"]))


@app.route("/view_category/<category_id>")
def view_category(category_id):
    """
    View each recipe category individually.
    """
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    allrecipe = list(mongo.db.recipes.find(
        {"category_name": category["category_name"]}))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("view-category.html",
                            allrecipe=allrecipe, 
                            category=category)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
