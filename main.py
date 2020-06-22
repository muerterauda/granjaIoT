import os

from flask import Flask, send_from_directory, render_template

from servicios.servicios_basicos import granja_bp
from mongo.repository import medicion_repository, estado_repository

basedir = os.path.abspath(os.path.dirname(__file__))

"""APP creation and configuration"""
app = Flask(__name__, static_folder="static")


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('resources/static/js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('resources/static/css', path)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('resources/static/img', path)

@app.route('/')
def index():
    m_utlimo = medicion_repository.get_last()[0]
    return render_template("inicio.html", ultimo=m_utlimo, estado=estado_repository.get_estado())


app.register_blueprint(granja_bp, url_prefix="/granjaIoT/")

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(ssl_context='adhoc', host='0.0.0.0', port=443)
    # app.run(ssl_context='adhoc', host='localhost', port=5000, debug=True)
