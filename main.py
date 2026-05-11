from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import randint

app = Flask(__name__)
app.json.sort_keys = False

# Connect to Database
app.config[
    'SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:\\Users\\ibunu\\Downloads\\003 Starting-Files-cafe-api-start\cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def dict_conversion(self):
        cafe = {
            "id": self.id,
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price,
        }
        return cafe


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=["GET"])
def random():
    random_number = randint(1, 20)
    selected_record = db.session.get(Cafe, random_number)
    modified_record = selected_record.dict_conversion()
    return jsonify(modified_record)


@app.route("/all", methods=["GET"])
def all_cafes():
    cafes_list = []
    for i in range(1, len(Cafe.query.all()) + 1):
        current_cafe = db.session.get(Cafe, i)
        modified_cafe = current_cafe.dict_conversion()
        cafes_list.append(modified_cafe)
    return jsonify(cafes_list)


@app.route("/search")
def search():
    cafes_list = []
    loc = request.args.get("loc")
    has_toilet = request.args.get("has_toilet")
    for i in range(1, len(Cafe.query.all()) + 1):
        current_cafe = db.session.get(Cafe, i)
        if current_cafe.has_toilet and loc in current_cafe.location:
            cafes_list.append(current_cafe.dict_conversion())
    return jsonify(cafes_list)


@app.route("/add", methods=["POST"])
def add():
    key = request.args.get("id")
    name = request.args.get("name")
    map_url = request.args.get("map_url")
    img_url = request.args.get("img_url")
    location = request.args.get("location")
    seats = request.args.get("seats")
    has_toilet = request.args.get("has_toilet")
    has_wifi = request.args.get("has_wifi")
    has_sockets = request.args.get("has_sockets")
    can_take_calls = request.args.get("can_take_calls")
    coffee_price = request.args.get("coffee_price")
    if has_toilet == "True":
        has_toilet = True
    else:
        has_toilet = False
    if has_wifi == "True":
        has_wifi = True
    else:
        has_wifi = False
    if has_sockets == "True":
        has_sockets = True
    else:
        has_sockets = False
    if can_take_calls == "True":
        can_take_calls = True
    else:
        can_take_calls = False
    new_cafe = Cafe(id=key, name=name, map_url=map_url, img_url=img_url, location=location, seats=seats,
                    has_toilet=has_toilet, has_wifi=has_wifi, has_sockets=has_sockets, can_take_calls=can_take_calls,
                    coffee_price=coffee_price)
    db.session.add(new_cafe)
    db.session.commit()

    cafe_list = []
    for i in range(1, len(Cafe.query.all()) + 1):
        current_cafe = db.session.get(Cafe, i)
        cafe_list.append(current_cafe.dict_conversion())

    return jsonify(cafe_list)


@app.route("/update/<int:key>")
def update(key):
    coffee_price = request.args.get("coffee_price")
    selected_coffee = db.session.get(Cafe, key)
    selected_coffee.coffee_price = coffee_price
    db.session.commit()
    selected_coffee_updated = selected_coffee.dict_conversion()
    return jsonify(selected_coffee_updated)


@app.route("/delete/<int:key>", methods=["DELETE"])
def delete(key):
    secret_key = "thisismysecretkey"
    user_secret_key = request.args.get("api_key")
    if secret_key == user_secret_key:
        selected_cafe = db.session.get(Cafe, key)
        if selected_cafe:
            db.session.delete(selected_cafe)
            db.session.commit()
            cafes_list = []
            for i in range(1, len(Cafe.query.all()) + 1):
                current_cafe = db.session.get(Cafe, i)
                modified_cafe = current_cafe.dict_conversion()
                cafes_list.append(modified_cafe)
            return jsonify(cafes_list)
        else:
            error_dict = {
                "error": {
                    "Not Found": "Sorry a cafe with that id was not found in the database."
                }
            }
            return jsonify(error_dict)
    else:
        error_dict = {
            "error": "Sorry, that's not allowed. Make sure you have the correct api key."
        }
        return jsonify(error_dict)


if __name__ == '__main__':
    app.run(debug=True)
