import os

import sentry_sdk

from bottle import Bottle
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://7d6b9cd1b4764ff3bf936c83a1e64a11@o420737.ingest.sentry.io/5339473",
    integrations=[BottleIntegration()]
)

app = Bottle()


@app.route('/')
def index():
    return """
        <!doctype html>
        <html lang="en">
          <head>
            <title>D2</title>
          </head>
          <body>
            <div class="container">
              <h1>Hi!</h1>
              <div>
                Доступны пути /success и /fail
              </div>
            </div>
          </body>
        </html>
        """


@app.route('/success')
def succeed():
    return """
        <!doctype html>
        <html lang="en">
          <head>
            <title>D2</title>
          </head>
          <body>
            <div class="container">
              <h1>Hi!</h1>
            </div>
          </body>
        </html>
        """


@app.route('/fail')
def fail():
    raise RuntimeError("There is an new error!")
    return """
        <!doctype html>
        <html lang="en">
          <head>
            <title>D2</title>
          </head>
          <body>
            <div class="container">
              <h1>500</h1>
            </div>
          </body>
        </html>
        """


if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)
