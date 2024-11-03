import flask

from holidays import views

app = flask.Flask(__name__)
app.url_map.strict_slashes = False

index = app.route(r'/')(views.index)
calendar = app.route(r'/calendar')(views.calendar_view)
warmup = app.route(r'/_ah/warmup')(views.warmup_view)
