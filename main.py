import flask

from holidays import views

app = flask.Flask(__name__)
app.url_map.strict_slashes = False

index = app.route('/')(views.index)
calendar = app.route('/calendar')(views.calendar_view)
