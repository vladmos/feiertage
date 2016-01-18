from __future__ import unicode_literals, absolute_import, print_function

import datetime

import webapp2
from webapp2_extras import jinja2

from holidays import dates, calendar


class MainPage(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, template, **context):
        # Renders a template and writes the result to the response.
        rendered_template = self.jinja2.render_template(template, **context)
        self.response.write(rendered_template)

    def get(self):
        regions = dates.REGIONS.items()
        regions.sort()
        self.render_response('index.html', regions=regions)


class Calendar(webapp2.RequestHandler):
    def get(self):
        region = self.request.get('region', '').upper()
        if region not in dates.REGIONS:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.status = 404
            self.response.write('Unknown region: %s' % region)
            return

        current_year = datetime.date.today().year
        feed = calendar.Calendar(
            summary='Feiertage in %s, Deutschland' % dates.REGIONS[region],
            prodid='fulc.ru'
        )

        for year in xrange(current_year, dates.MAXIMUM_KNOWN_YEAR + 1):
            for name, (date, regions) in dates.HOLIDAYS.iteritems():
                if regions is not None and region not in regions:
                    continue
                if callable(date):
                    date = date(year)

                day, month = date

                feed.add_event(name, '%04d%02d%02d' % (year, month, day))

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(feed.to_ical())
