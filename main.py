import flask

from holidays import views

app = flask.Flask(__name__)
app.url_map.strict_slashes = False

@app.before_request
def hostname_redirect():
    if flask.request.host == 'german-holidays.fulc.ru':
        return flask.redirect('https://feiertage.vladmos.com' + flask.request.path)


index = app.route(r'/')(views.index)
calendar = app.route(r'/calendar')(views.calendar_view)
calendar = app.route(r'/calendar/<region>')(views.calendar_view)
warmup = app.route(r'/_ah/warmup')(views.warmup_view)
