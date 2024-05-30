from flask import Flask, request, jsonify
from volume_calculator import VolumeCalculator

app = Flask(__name__)

@app.route('/calculate_volume', methods=['POST'])
def calculate_volume():
    data = request.json
    shape = data.get('shape')
    dimensions = data.get('dimensions', {})

    if shape == 'cube':
        side_length = dimensions.get('side_length')
        if side_length is None:
            return jsonify(error="Missing 'side_length' for cube"), 400
        try:
            volume = VolumeCalculator.cube(side_length)
        except ValueError as e:
            return jsonify(error=str(e)), 400

    elif shape == 'sphere':
        radius = dimensions.get('radius')
        if radius is None:
            return jsonify(error="Missing 'radius' for sphere"), 400
        try:
            volume = VolumeCalculator.sphere(radius)
        except ValueError as e:
            return jsonify(error=str(e)), 400

    elif shape == 'cylinder':
        radius = dimensions.get('radius')
        height = dimensions.get('height')
        if radius is None or height is None:
            return jsonify(error="Missing 'radius' or 'height' for cylinder"), 400
        try:
            volume = VolumeCalculator.cylinder(radius, height)
        except ValueError as e:
            return jsonify(error=str(e)), 400

    elif shape == 'cone':
        radius = dimensions.get('radius')
        height = dimensions.get('height')
        if radius is None or height is None:
            return jsonify(error="Missing 'radius' or 'height' for cone"), 400
        try:
            volume = VolumeCalculator.cone(radius, height)
        except ValueError as e:
            return jsonify(error=str(e)), 400

    else:
        return jsonify(error="Invalid shape type"), 400

    return jsonify(volume=volume)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)
