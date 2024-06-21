from prometheus_client import Counter, generate_latest, CollectorRegistry, multiprocess, make_wsgi_app
from prometheus_client import CONTENT_TYPE_LATEST
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask import Flask, request, jsonify
from volume_calculator import VolumeCalculator


app = Flask(__name__)

# Initialize Prometheus metrics
REQUEST_COUNT = Counter('request_count', 'Total number of requests', ['method', 'endpoint', 'http_status'])
ERROR_COUNT = Counter('error_count', 'Total number of errors', ['method', 'endpoint', 'http_status'])

@app.route('/calculate_volume', methods=['POST'])
def calculate_volume():
    REQUEST_COUNT.labels(method='POST', endpoint='/calculate_volume', http_status=200).inc()
    data = request.json
    shape = data.get('shape')
    dimensions = data.get('dimensions', {})

    if shape == 'cube':
        side_length = dimensions.get('side_length')
        if side_length is None:
            ERROR_COUNT.labels(method='POST', endpoint='/calculate_volume', http_status=400).inc()
            return jsonify(error="Missing 'side_length' for cube"), 400
        try:
            volume = VolumeCalculator.cube(side_length)
        except ValueError as e:
            ERROR_COUNT.labels(method='POST', endpoint='/calculate_volume', http_status=400).inc()
            return jsonify(error=str(e)), 400

    elif shape == 'sphere':
        radius = dimensions.get('radius')
        if radius is None:
            ERROR_COUNT.labels(method='POST', endpoint='/calculate_volume', http_status=400).inc()
            return jsonify(error="Missing 'radius' for sphere"), 400
        try:
            volume = VolumeCalculator.sphere(radius)
        except ValueError as e:
            ERROR_COUNT.labels(method='POST', endpoint='/calculate_volume', http_status=400).inc()
            return jsonify(error=str(e)), 400

    elif shape == 'cylinder':
        radius = dimensions.get('radius')
        height = dimensions.get('height')
        if radius is None or height is None:
            ERROR_COUNT.labels(method='POST', endpoint='/calculate_volume', http_status=400).inc()
            return jsonify(error="Missing 'radius' or 'height' for cylinder"), 400
        try:
            volume = VolumeCalculator.cylinder(radius, height)
        except ValueError as e:
            ERROR_COUNT.labels(method='POST', endpoint='/calculate_volume', http_status=400).inc()
            return jsonify(error=str(e)), 400

    elif shape == 'cone':
        radius = dimensions.get('radius')
        height = dimensions.get('height')
        if radius is None or height is None:
            ERROR_COUNT.labels(method='POST', endpoint='/calculate_volume', http_status=400).inc()
            return jsonify(error="Missing 'radius' or 'height' for cone"), 400
        try:
            volume = VolumeCalculator.cone(radius, height)
        except ValueError as e:
            ERROR_COUNT.labels(method='POST', endpoint='/calculate_volume', http_status=400).inc()
            return jsonify(error=str(e)), 400

    else:
        ERROR_COUNT.labels(method='POST', endpoint='/calculate_volume', http_status=400).inc()
        return jsonify(error="Invalid shape type"), 400

    return jsonify(volume=volume)

@app.route('/metrics')
def metrics():
    return generate_latest()

# Setup the DispatcherMiddleware to include the Prometheus WSGI application
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)

