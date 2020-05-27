from flask import Blueprint, render_template, jsonify

predict_routes = Blueprint("predict_routes", __name__)

# Create predict route
@predict_routes.route('/predict') #, methods=['POST'])
def predict():
    # TODO: app.logger.info("/predict beginning...")
    # TODO: request_data = request.get_json(force=True)
    # TODO: input_text = request_data['text']
    # TODO: var1, var2, var_n, ...  = machine_learning_model(input_text, params, params, params)
    # TODO: app.logger.info("/predict model complete...")
    # TODO: recommendation = machine_learning_model_output....
    # TODO: return jsonify(recommendation)

    return jsonify("So far so good...") # Return basic jsonified string to ensure things are working