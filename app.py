from flask import Flask
# from apiv1 import blueprint as api1
# from apiX import blueprint as apiX

app = Flask(__name__)
app.register_blueprint(api1)
# app.register_blueprint(apiX)
app.run(debug=True)
