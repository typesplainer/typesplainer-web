import os
import re

from flask import Flask, send_from_directory, render_template, request, url_for
from flask.helpers import get_debug_flag
from mypy.errors import CompileError
from typesplainer import parse_code, get_json
from werkzeug.exceptions import HTTPException


app = Flask(__name__)
app.config["TRAP_HTTP_EXCEPTIONS"] = True
app.cache = {}

if get_debug_flag():
    from flask_rich import RichApplication
    from rich.logging import RichHandler

    rich = RichApplication(app)

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@app.errorhandler(HTTPException)
def http_error_handler(error):
    return render_template(
        "error.html", title=error.code, description=error.description
    )


@app.route("/typesplain", methods=["POST"])
def typesplain():
    code = request.form.get("code")

    if code.strip() == "import this":
        return render_template(
            "error.html",
            title="The Zen of Python",
            description='Beautiful is better than ugly.<br>Explicit is better than implicit.<br>Simple is better than complex.<br>Complex is better than complicated.<br>Flat is better than nested.<br>Sparse is better than dense.<br>Readability counts<br><small style=\"font-size: 0.6em;margin-top:0px\">(shortened)</small>',
        )

    if len(code) > 5_242_880:
        return render_template(
            "error.html",
            title="Sorry :(",
            description='For files over 5 MB, please use <a target="_blank" href="https://pypi.org/project/typesplainer/">typesplainer CLI</a> instead',
        )

    if code in app.cache:
        return render_template("typesplain.html", data=app.cache[code])
    type_defs = parse_code(code)
    try:
        typesplained_json = get_json(type_defs)
    except CompileError as e:
        return render_template("error.html", title="Compile Error", description=str(e))
    return render_template("typesplain.html", data=typesplained_json)
