from flask import Flask

from analytics.interfaces.services import metric_api
from shared.infrastructre.database import init_db

app = Flask(__name__)
app.register_blueprint(metric_api)
first_request = True

@app.before_request
def setup():
    global first_request
    if first_request:
        first_request = False
        init_db()
        # Setup auth

if __name__ == '__main__':
    app.run(port=8000,debug=True)
