from flask import Flask

import iam
from analytics.interfaces.services import metric_api
from iam.interfaces.services import iam_api
from shared.infrastructre.database import init_db
from analytics.infrastructure.services import start_periodic_fetch, process_sensor_data

app = Flask(__name__)
app.register_blueprint(metric_api)
app.register_blueprint(iam_api)

init_db()

start_periodic_fetch(process_sensor_data)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
