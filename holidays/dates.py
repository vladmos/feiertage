# coding: utf-8
from __future__ import unicode_literals, absolute_import, print_function

from datetime import date, timedelta


EASTERS = {
    2016: (27, 3),
    2017: (16, 4),
    2018: (1, 4),
    2019: (21, 4),
    2020: (12, 4),
}

FIRST_ADVENTS = {
    2016: (27, 11),
    2017: (3, 12),
    2018: (2, 12),
    2019: (1, 12),
    2020: (29, 11),
}


def easter_day(shift):
    def inner(year):
        day, month = EASTERS[year]
        easter = date(year, month, day)
        the_date = easter + timedelta(shift)
        return the_date.day, the_date.month
    return inner


def second_wednesday_before_the_first_advent(year):
    first_advent_day, first_advent_month = FIRST_ADVENTS[year]
    first_advent = date(year, first_advent_month, first_advent_day)
    # First advent is always on Sunday
    wednesday = first_advent - timedelta(11)
    return wednesday.day, wednesday.month


# Assuming that there are no gaps in EASTERS
MAXIMUM_KNOWN_YEAR = max(EASTERS.iterkeys())

REGIONS = {
    'BW': 'Baden-Württemberg',
    'BY': 'Freistaat Bayern',
    'BY-AU': 'Freistaat Bayern: Augsburg',
    'BY-MU': 'Freistaat Bayern: München',
    'BE': 'Berlin',
    'BB': 'Brandenburg',
    'HB': 'Freie Hansestadt Bremen',
    'HH': 'Hamburg',
    'HE': 'Hessen',
    'MV': 'Mecklenburg-Vorpommern',
    'NI': 'Niedersachsen',
    'NW': 'Nordrhein-Westfalen',
    'RP': 'Rheinland-Pfalz',
    'SL': 'Saarland',
    'SN': 'Sachsen',
    'ST': 'Sachsen-Anhalt',
    'SH': 'Schleswig-Holstein',
    'TH': 'Thüringen',
}

HOLIDAYS = {
    'Neujahrstag': ((1, 1), None),
    'Heilige Drei Könige': ((6, 1), {'BW', 'BY', 'BY-AU', 'BY-MU', 'ST'}),
    'Karfreitag': (easter_day(-2), None),
    'Ostermontag': (easter_day(1), None),
    'Tag der Arbeit': ((1, 5), None),
    'Christi Himmelfahrt': (easter_day(39), None),
    'Pfingstmontag': (easter_day(50), None),
    'Fronleichnam': (easter_day(60), {'BW', 'BY', 'BY-AU', 'BY-MU', 'HE', 'NW', 'RP', 'SL'}),
    'Friedensfest': ((8, 8), {'BY-AU'}),
    'Mariä Himmelfahrt': ((15, 8), {'BY-AU', 'BY-MU', 'SL'}),
    'Tag der Deutschen Einheit': ((3, 10), None),
    'Reformationstag': ((31, 10), {'BB', 'MW', 'SN', 'ST', 'TH'}),
    'Allerheiligen': ((1, 11), {'BW', 'BY', 'BY-AU', 'BY-MU', 'NW', 'RP', 'SL'}),
    'Buß- und Bettag': (second_wednesday_before_the_first_advent, {'SN'}),
    'Weihnachtstag': ((25, 12), None),
    'Zweiter Weihnachtsfeiertag': ((26, 12), None),
}

GLOBAL_EXCEPTIONS = {
    'Reformationstag': [2017],
}