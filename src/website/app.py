import re

from flask import Flask, send_from_directory, render_template, request, url_for
from mypy.errors import CompileError
from typesplainer import parse_code, get_json
from werkzeug.exceptions import HTTPException


app = Flask(__name__)
app.config["TRAP_HTTP_EXCEPTIONS"] = True
app.cache = {}
app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon.ico'))

@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.errorhandler(HTTPException)
def http_error_handler(error):
    return render_template(
        "error.html", title=error.code, description=error.description
    )


@app.route("/typesplain", methods=["POST"])
def typesplain():
    code = request.form.get("code")
    formatted_code = "\n".join(re.findall(r"'[^;]*'(?=;|$)|([^;]+)(?=;|$)", code))

    if len(formatted_code) > 5_242_880:
        return render_template(
            "error.html",
            title="Sorry :(",
            description='For files over 5 MB, please use <a target="_blank" href="https://pypi.org/project/typesplainer/">typesplainer CLI</a> instead',
        )

    if formatted_code in app.cache:
        return render_template("typesplain.html", data=app.cache[formatted_code])
    type_defs = parse_code(formatted_code)
    try:
        typesplained_json = get_json(type_defs)
    except CompileError as e:
        return render_template("error.html", title="Compile Error", description=str(e))
    return render_template("typesplain.html", data=typesplained_json)
