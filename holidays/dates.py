# coding: utf-8

from datetime import date, timedelta

def easter_day(year, shift):
    day, month = EASTERS[year]
    easter = date(year, month, day)
    the_date = easter + timedelta(shift)
    return the_date.day, the_date.month


def wednesday_before_november_23(year):
    november_23 = date(year, 11, 23)
    shift = november_23.weekday() - 2
    if shift <= 0:
        shift += 7
    wednesday = november_23 - timedelta(shift)
    return wednesday.day, wednesday.month


EASTERS = {
    2014: (20, 4),
    2015: (5, 4),
    2016: (27, 3),
    2017: (16, 4),
    2018: (1, 1),
    2019: (21, 4),
    2020: (12, 4),
}


REGIONS = {
    'BW': u'Baden-Württemberg',
    'BY': u'Freistaat Bayern',
    'BE': u'Berlin',
    'BB': u'Brandenburg',
    'HB': u'Freie Hansestadt Bremen',
    'HH': u'Hamburg',
    'HE': u'Hessen',
    'MV': u'Mecklenburg-Vorpommern',
    'NI': u'Niedersachsen',
    'NW': u'Nordrhein-Westfalen',
    'RP': u'Rheinland-Pfalz',
    'SL': u'Saarland',
    'SN': u'Sachsen',
    'ST': u'Sachsen-Anhalt',
    'SH': u'Schleswig-Holstein',
    'TH': u'Thüringen',
}

HOLIDAYS = {
    u'Neujahrstag': ((1, 1), None),
    u'Heilige Drei Könige': ((6, 1), {'BW', 'BY', 'ST'}),
    u'Karfreitag': (lambda year: easter_day(year, -2), None),
    u'Ostermontag': (lambda year: easter_day(year, 1), None),
    u'Tag der Arbeit': ((1, 5), None),
    u'Christi Himmelfahrt': (lambda year: easter_day(year, 39), None),
    u'Pfingstmontag': (lambda year: easter_day(year, 50), None),
    u'Fronleichnam': (lambda year: easter_day(year, 60), {'BW', 'BY', 'HE', 'NW', 'RP', 'SL'}),
    u'Friedensfest': ((8, 8), {}),
    u'Mariä Himmelfahrt': ((15, 8), {'SL'}),
    u'Tag der Deutschen Einheit': ((3, 10), None),
    u'Reformationstag': ((31, 10), {'BB', 'MW', 'SN', 'ST', 'TH'}),
    u'Allerheiligen': ((1, 11), {'BW', 'BY', 'NW', 'RP', 'SL'}),
    u'Buß- und Bettag': (wednesday_before_november_23, {'SN'}),
    u'Weihnachtstag': ((25, 12), None),
    u'Zweiter Weihnachtsfeiertag': ((26, 12), None),
}
