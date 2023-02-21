import json

from flask import Flask, request, jsonify, make_response
from loguru import logger
from loko_extensions.business.decorators import extract_value_args
from loko_extensions.model.components import Component, Arg, save_extensions
from rpy2.robjects.numpy2ri import rpy2py

app = Flask("")

import rpy2.robjects as robjects
import numpy as np

c = Component("R", args=[Arg("code", type="code", value="seq(from = 5, to = 100, by = 5)")],
              description="A components that allows to run R code")

save_extensions([c])


def json_response(o):
    if isinstance(o, np.ndarray):
        return o.tolist()
    else:
        return o


@app.errorhandler(Exception)
def handle_exception(e):
    logger.exception(e)
    response = make_response(f"Error {e}", 500)
    return response


@app.route("/", methods=["POST"])
@extract_value_args(_request=request)
def execute(value, args):
    code = args.get("code")
    _value = json.dumps(value)

    fcode = f"""secretfunctionname <- function(data) {{
      {code}
    }}
    secretfunctionname({_value})
    """
    logger.debug(fcode)
    result = robjects.r(fcode)
    result = rpy2py(result)

    return jsonify(json_response(result))


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)

if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
