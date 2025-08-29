from flask import Flask, render_template
import routes

app = Flask(__name__)

app.register_blueprint(routes.main)

if __name__ == "__main__":
    app.run(debug=True)
