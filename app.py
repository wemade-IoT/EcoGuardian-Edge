from flask import Flask, request

import iam
from analytics.interfaces.services import metric_api
from iam.interfaces.services import iam_api
from shared.infrastructre.database import init_db

app = Flask(__name__)
app.register_blueprint(metric_api)
app.register_blueprint(iam_api)
first_request = True

@app.before_request
def setup():
    global first_request
    if first_request:
        first_request = False
        init_db()
        # Setup auth
        auth_application_service = iam.application.services.AuthApplicationService()
        data = request.json
        api_key = request.headers.get('X-API-Key')
        device_id = data['device_id']
        auth_application_service.get_or_create_test_device(device_id,api_key)

if __name__ == '__main__':
    app.run(port=8000,debug=True)
