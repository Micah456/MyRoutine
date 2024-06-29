from flask import Flask, request
import support as sp
import data_transfer as dt


port = 5016
app = Flask("MyRoutine")

@app.route("/database/user", methods=["POST"])
def create_user():
    raw_resource = sp.convert_resource_from_json(request.json)
    result = dt.create_object(dt.user_table, raw_resource)
    return sp.set_resource_response(result, "User")

@app.route("/database/routine", methods=["POST"])
def create_routine():
    raw_resource = sp.convert_resource_from_json(request.json)
    result = dt.create_object(dt.routine_table, raw_resource)
    return sp.set_resource_response(result, "Routine")

@app.route("/database/step", methods=["POST"])
def create_step():
    raw_resource = sp.convert_resource_from_json(request.json)
    result = dt.create_object(dt.step_table, raw_resource)
    return sp.set_resource_response(result, "Step")
    

if __name__ == "__main__":
    app.run(debug=True, port=port)
    # When no port is specified, starts at default port 5000
