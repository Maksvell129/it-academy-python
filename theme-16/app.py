from typing import Optional

from flask import Flask, render_template
from flask import request
from flask_migrate import Migrate

from routes import users_blueprint, products_blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(users_blueprint, name='users', url_prefix='/users')
app.register_blueprint(products_blueprint, name='products', url_prefix='/products')



from sqlalchemy.orm import Mapped, mapped_column


class User(db.Model):
    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column()

    email: Mapped[str] = mapped_column(
        unique=True
    )

    age: Mapped[Optional[int]] = mapped_column()


@app.route("/")
def index():
    is_admin = False

    return render_template(
        "index.html",
        is_admin=is_admin
    )

@app.get("/about")
def about():
    return "О нас"

@app.route("/contacts")
def contacts():
    # update_status(user_id, status)
    return "Контакты"