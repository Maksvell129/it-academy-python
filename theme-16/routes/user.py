from flask import Blueprint, render_template, request, redirect, url_for

users_blueprint = Blueprint("users", __name__)


@users_blueprint.get("/<int:user_id>")
def user_detail(user_id):
    from app import db, User

    user = db.session.get(User, user_id)

    if user is None:
        return "User not found", 404

    return render_template("user.html",  user=user)


@users_blueprint.route("/create", methods=["GET", "POST"])
def create_user():
    from app import db, User


    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        age = request.form["age"]
        user = User( name=name, email=email, age=int(age) )
        db.session.add(user)
        db.session.commit()
        return redirect( url_for("users.users_all") )

    return render_template("create_user.html",)



@users_blueprint.get("")
def users_all():
    from app import db, User

    users = db.session.execute(db.select(User)).scalars().all()
    return render_template("users.html", users=users)


@users_blueprint.post("/<int:user_id>/delete")
def delete_user(user_id):
    from app import db, User

    user = db.session.get(User, user_id)

    if user is None:
        return "User not found", 404

    db.session.delete(user)
    db.session.commit()

    return redirect(url_for("users.users_all") )
