"""
iCal generator
"""
from __future__ import unicode_literals, absolute_import, print_function

from hashlib import md5


class Event(object):
    def __init__(self, summary, year, month, day):
        self.summary = summary
        self.date = '%04d%02d%02d' % (year, month, day)

    @property
    def uid(self):
        return md5((self.summary + self.date).encode('utf-8')).hexdigest()


class Calendar(object):
    def __init__(self, summary, prodid):
        self.summary = summary
        self.prodid = prodid
        self.events = []

    def add_event(self, *args, **kwargs):
        self.events.append(Event(*args, **kwargs))

    def to_ical(self):
        lines = []

        lines.append('BEGIN:VCALENDAR')
        lines.append('CALSCALE:GREGORIAN')
        lines.append('PRODID:%s' % self.prodid)
        lines.append('VERSION:2.0')
        lines.append('X-WR-CALNAME:%s' % self.summary)

        for event in sorted(self.events, key=lambda e: e.date):
            lines.append('BEGIN:VEVENT')
            lines.append('SUMMARY:%s' % event.summary)
            lines.append('UID:%s' % event.uid)
            lines.append('DTSTART;VALUE=DATE:%s' % event.date)
            lines.append('TRANSP:TRANSPARENT')
            lines.append('END:VEVENT')

        lines.append('END:VCALENDAR')

        return '\n'.join(lines)
