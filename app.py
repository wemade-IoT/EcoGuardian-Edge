from flask import Flask

import iam
from analytics.interfaces.services import metric_api
from iam.interfaces.services import iam_api
from shared.infrastructre.database import init_db
from iam.application.services import AuthApplicationService

app = Flask(__name__)
app.register_blueprint(metric_api)
app.register_blueprint(iam_api)

init_db()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
