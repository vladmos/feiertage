from datetime import date, timedelta


EASTERS = {
    2016: (3, 27),
    2017: (4, 16),
    2018: (4, 1),
    2019: (4, 21),
    2020: (4, 12),
    2021: (4, 4),
    2022: (4, 17),
    2023: (4, 9),
    2024: (3, 31),
    2025: (4, 20),
    2026: (4, 5),
    2027: (4, 28),
    2028: (4, 16),
    2029: (4, 1),
    2030: (4, 21),
    2031: (4, 13),
    2032: (3, 28),
    2033: (4, 17),
    2034: (4, 9),
    2035: (3, 25),
}

FIRST_ADVENTS = {
    2016: (11, 27),
    2017: (12, 3),
    2018: (12, 2),
    2019: (12, 1),
    2020: (11, 29),
    2021: (11, 28),
    2022: (11, 27),
    2023: (12, 3),
    2024: (12, 1),
    2025: (11, 30),
    2026: (11, 29),
    2027: (11, 28),
    2028: (12, 3),
    2029: (12, 2),
    2030: (12, 1),
    2031: (11, 30),
    2032: (11, 28),
    2033: (11, 27),
    2034: (12, 3),
    2035: (12, 2),
}


def easter_day(shift):
    def inner(year):
        easter = date(year, *EASTERS[year])
        the_date = easter + timedelta(shift)
        return the_date.month, the_date.day
    return inner


def second_wednesday_before_the_first_advent(year):
    first_advent = date(year, *FIRST_ADVENTS[year])
    # First advent is always on Sunday
    wednesday = first_advent - timedelta(11)
    return wednesday.month, wednesday.day


# Assuming that there are no gaps in EASTERS
MAXIMUM_KNOWN_YEAR = max(EASTERS.keys())

REGIONS = {
    'BW': 'Baden-Württemberg',
    'BY': 'Freistaat Bayern',
    'BY-AGB': 'Freistaat Bayern: Augsburg',
    'BY-MUC': 'Freistaat Bayern: München',
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

ALIASES = {
    'BY-MU': 'BY-MUC',
    'BY-AU': 'BY-AGB'
}

HOLIDAYS = {
    'Neujahrstag': ((1, 1), None),
    'Heilige Drei Könige': ((1, 6), {'BW', 'BY', 'BY-AGB', 'BY-MUC', 'ST'}),
    'Internationaler Frauentag': ((3, 8), {'BE', 'MV', }),
    'Karfreitag': (easter_day(-2), None),
    'Ostermontag': (easter_day(1), None),
    'Tag der Arbeit': ((5, 1), None),
    'Christi Himmelfahrt': (easter_day(39), None),
    'Pfingstmontag': (easter_day(50), None),
    'Fronleichnam': (easter_day(60), {'BW', 'BY', 'BY-AGB', 'BY-MUC', 'HE', 'NW', 'RP', 'SL'}),
    'Friedensfest': ((8, 8), {'BY-AGB'}),
    'Mariä Himmelfahrt': ((8, 15), {'BY-AGB', 'BY-MUC', 'SL'}),
    'Weltkindertag': ((9, 20), {'TH'}),
    'Tag der Deutschen Einheit': ((10, 3), None),
    'Reformationstag': ((10, 31), {'BB', 'HB', 'HH', 'MW', 'NI', 'SN', 'ST', 'SH', 'TH'}),
    'Allerheiligen': ((11, 1), {'BW', 'BY', 'BY-AGB', 'BY-MUC', 'NW', 'RP', 'SL'}),
    'Buß- und Bettag': (second_wednesday_before_the_first_advent, {'SN'}),
    'Weihnachtstag': ((12, 25), None),
    'Zweiter Weihnachtsfeiertag': ((12, 26), None),
}

GLOBAL_EXCEPTIONS = {
    'Reformationstag': [2017],
}
