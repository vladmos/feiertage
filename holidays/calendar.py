"""
iCal generator
"""
from hashlib import md5


class Event(object):
    def __init__(self, summary, date):
        self.summary = summary
        self.date = date

    @property
    def uid(self):
        return md5(self.summary.encode('utf-8') + self.date).hexdigest()


class Calendar(object):
    def __init__(self, summary, prodid):
        self.summary = summary
        self.prodid = prodid
        self.events = []

    def add_event(self, *args, **kwargs):
        self.events.append(Event(*args, **kwargs))

    def to_ical(self):
        lines = []

        lines.append(u'BEGIN:VCALENDAR')
        lines.append(u'CALSCALE:GREGORIAN')
        lines.append(u'PRODID:%s' % self.prodid)
        lines.append(u'VERSION:2.0')
        lines.append(u'X-WR-CALNAME:%s' % self.summary)

        for event in self.events:
            lines.append(u'BEGIN:VEVENT')
            lines.append(u'SUMMARY:%s' % event.summary)
            lines.append(u'UID:%s' % event.uid)
            lines.append(u'DTSTART;VALUE=DATE:%s' % event.date)
            lines.append(u'TRANSP:TRANSPARENT')
            lines.append(u'END:VEVENT')

        lines.append(u'END:VCALENDAR')

        return u'\n'.join(lines)
