from flask import Flask

import iam
from analytics.interfaces.services import metric_api
from iam.interfaces.services import iam_api
from shared.infrastructre.database import init_db
from analytics.infrastructure.services import start_periodic_metrics_push

app = Flask(__name__)
app.register_blueprint(metric_api)
app.register_blueprint(iam_api)

init_db()

start_periodic_metrics_push('b1e2c3d4-5f6a-7b8c-9d0e-1f2a3b4c5d6e')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
