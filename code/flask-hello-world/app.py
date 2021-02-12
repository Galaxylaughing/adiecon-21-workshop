from flask import Flask, request, jsonify


app = Flask(__name__)


# The @ line above a function signature is a Python decorator. Follow this syntax to make an endpoint.
@app.route('/api/hello', methods=['GET'])
def hello_world_tacocat():
    # Return our response
    return "Hello, World!"


@app.route('/api/hello-json', methods=['GET'])
def hello_world_json():
    # jsonify, imported from Flask, let's us jsonify
    return jsonify({
        "Hello": "World"
    })


@app.route('/api/handles-many-methods', methods=['GET', 'POST', 'DELETE'])
def hello_methods():
    # If we wanted a method that handled many methods,
    # we can use a conditional and read through request
    # request, imported from Flask, gives us info about the request

    if request.method == 'GET':
        return "Nice GET method!"


@app.route('/api/handles-many-methods', methods=['GET'])
def hello_duplicate_matches():
    return "This will never be seen, because the request matched on the route above."
