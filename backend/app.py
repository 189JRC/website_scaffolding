from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

# db connection
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:postgres@postgresql_db:5432/postgres"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)


@app.route("/")
def index():
    with app.app_context():
        # Simple query to test the database connection
        result = db.session.execute(text("SELECT 1")).fetchone()
        return jsonify({"result": result[0]})


@app.route("/add/<string:name>")
def add_user(name):
    new_user = User(name=name, password="password")
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"result": "User added"})


@app.route("/users")
def get_users():
    users = User.query.all()
    result = [{"id": user.id, "name": user.name} for user in users]
    return jsonify(result)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)
