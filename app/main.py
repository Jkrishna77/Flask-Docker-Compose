from flask import Flask, render_template
import routes
import os

app = Flask(__name__)

app.register_blueprint(routes.main)

@app.context_processor
def inject_app_name():
    return dict(app_name=os.getenv("APP_NAME", "Flask-App"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
