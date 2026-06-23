from flask import Flask
from models import db
from controllers.cinema_controller import cinema_bp

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cinema.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



app.config["SECRET_KEY"] = "sua_chave_secreta"

db.init_app(app)
app.register_blueprint(cinema_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)