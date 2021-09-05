from flask import Flask
from flask_cors import CORS
from Views.charge_view import charge_view

app = Flask(__name__)
app.register_blueprint(charge_view)
CORS(app)
app.run(debug=True)
