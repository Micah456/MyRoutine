from flask import Flask, request


port = 5016
app = Flask("MyRoutine")

if __name__ == "__main__":
    app.run(debug=True, port=port)
    # When no port is specified, starts at default port 5000
