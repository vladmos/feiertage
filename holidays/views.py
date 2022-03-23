import datetime

import flask

from holidays import dates, calendar


def index():
    regions = sorted(dates.REGIONS.items())
    return flask.render_template('index.html', regions=regions)


def calendar_view():
    region = flask.request.args.get('region', '').upper()
    if region not in dates.REGIONS:
        return flask.Response(
            'Unknown region: %s' % region,
            status=404,
            mimetype='text/plain',
        )

    current_year = datetime.date.today().year
    feed = calendar.Calendar(
        summary='Feiertage in %s, Deutschland' % dates.REGIONS[region],
        prodid='fulc.ru'
    )

    for year in range(current_year - 1, dates.MAXIMUM_KNOWN_YEAR + 1):
        for name, (date, regions) in dates.HOLIDAYS.items():
            if regions is not None and region not in regions:
                if year not in dates.GLOBAL_EXCEPTIONS.get(name, []):
                    continue
            if callable(date):
                date = date(year)

            feed.add_event(name, year, *date)

    return flask.Response(
        feed.to_ical(),
        mimetype='text/calendar',
    )
