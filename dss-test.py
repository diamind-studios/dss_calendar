from datetime import date, timedelta
from pprint import pprint

# variables in calculation
# equinox could be 19th-21st

test_date = date(32,4,6) # Apr 6, 32 A.D. - Daniel date (ch 9)
test_date = date(2005,3,17)


# Different dates of creation (BC)
age_coefficient = [
    #{'date': [3960,3959], 'source': 'common'}, code needs updated so it can handle date intervals to deal with uncertainty
    {'date': 3925, 'source': ['Ken Johnson']},
    {'date': 3942, 'source': ['Eusebius','Jerome']},
    {'date': 3761, 'source': ['Jose ben Halafta: Seder Olam Rabbah']},
    {'date': 4339, 'source': ['Seder Olam Zutta']},
    {'date': 4997, 'source': ['Kepler'],'location':'https://www.science20.com/science_20/kepler_young_earth_creationist-134613'},
    #{'date': 3998, 'source': ['Isaac Newton'],'location':'Chronology of Ancient Kingdoms: Amended'}, can't really confirm this one
    {'date': 5500, 'source': ['Septuagint']}
]

months = {
    '30': {'type': 'Month', 'heb_name': 'NISAN', 'dss_name': 'ABIB'},
    '60': {'type': 'Month', 'heb_name': 'IYAR', 'dss_name': 'ZIF'},
    '90': {'type': 'Month', 'heb_name': 'SIVAN', 'dss_name': 'SIVAN'},
    '91': {'type': 'Equinox', 'heb_name': '', 'dss_name': 'Tekufah Tammuz'},
    '121': {'type': 'Month', 'heb_name': 'TAMMUZ', 'dss_name': 'TAMMUZ'},
    '151': {'type': 'Month', 'heb_name': 'AV', 'dss_name': 'AV'},
    '181': {'type': 'Month', 'heb_name': 'ELUL', 'dss_name': 'ELUL'},
    '182': {'type': 'Equinox', 'heb_name': '', 'dss_name': 'Tekufah Tishrei'},
    '212': {'type': 'Month', 'heb_name': 'TISHREI', 'dss_name': 'TISHREI'},
    '242': {'type': 'Month', 'heb_name': 'HESHVAN', 'dss_name': 'BUL'},
    '272': {'type': 'Month', 'heb_name': 'KISLEV', 'dss_name': 'KISLEV'},
    '273': {'type': 'Equinox', 'heb_name': '', 'dss_name': 'Tekufah Tevet'},
    '303': {'type': 'Month', 'heb_name': 'TEVET', 'dss_name': 'TEVET'},
    '333': {'type': 'Month', 'heb_name': 'SHEVAT', 'dss_name': 'SHEVAT'},
    '363': {'type': 'Month', 'heb_name': 'ADAR', 'dss_name': 'ADAR'},
    '364': {'type': 'Equinox', 'heb_name': '', 'dss_name': 'Tekufah Nisan'}
}
months = {
    '1': {'type': 'Equinox', 'heb_name': '', 'dss_name': 'Tekufah Nisan'},
    '31': {'type': 'Month', 'heb_name': 'NISAN', 'dss_name': 'ABIB'},
    '61': {'type': 'Month', 'heb_name': 'IYAR', 'dss_name': 'ZIF'},
    '91': {'type': 'Month', 'heb_name': 'SIVAN', 'dss_name': 'SIVAN'},
    '92': {'type': 'Equinox', 'heb_name': '', 'dss_name': 'Tekufah Tammuz'},
    '122': {'type': 'Month', 'heb_name': 'TAMMUZ', 'dss_name': 'TAMMUZ'},
    '152': {'type': 'Month', 'heb_name': 'AV', 'dss_name': 'AV'},
    '182': {'type': 'Month', 'heb_name': 'ELUL', 'dss_name': 'ELUL'},
    '183': {'type': 'Equinox', 'heb_name': '', 'dss_name': 'Tekufah Tishrei'},
    '213': {'type': 'Month', 'heb_name': 'TISHREI', 'dss_name': 'TISHREI'},
    '243': {'type': 'Month', 'heb_name': 'HESHVAN', 'dss_name': 'BUL'},
    '273': {'type': 'Month', 'heb_name': 'KISLEV', 'dss_name': 'KISLEV'},
    '274': {'type': 'Equinox', 'heb_name': '', 'dss_name': 'Tekufah Tevet'},
    '304': {'type': 'Month', 'heb_name': 'TEVET', 'dss_name': 'TEVET'},
    '334': {'type': 'Month', 'heb_name': 'SHEVAT', 'dss_name': 'SHEVAT'},
    '364': {'type': 'Month', 'heb_name': 'ADAR', 'dss_name': 'ADAR'}
}

eq_d = 22 # could be anywhere between 19-22, because the year starts on tekufah and you can have equinox from 19th-22nd
eq_m = 3


# this function returns the day of Tekufah Nisan, technically not a month, but the first of the year. 
# if you need first day of the year to be Nisan 1, simply change 'ny.weekday() == 1' to 'ny.weekday() == 2' and comment out the second 'months' variable 
def parse_new_year(year): 
    equinox = date(year,eq_m,eq_d)
    sub = 0
    while sub < 8:
        ny = equinox - timedelta(days=sub)
        if ny.weekday() == 1:
            return ny
        sub += 1

def parse_date(d,age=1):
    print(f'Calculating DSS date from: {d}')
    ny = parse_new_year(d.year)
    print(f'New year: {ny}')
    payload = {
        'year': d.year+age_coefficient[age]['date'],
        'dom': 0,
        'dow': d.strftime('%A')
    }
    if d < ny:
        print('before new years')
        ny = parse_new_year(d.year - 1)
        payload['year'] -= 1
    doy = (d - ny).days + 1
    #print('day of year:', doy)
    payload['doy'] = doy
    if doy > 364:
        print('Leap week')
    else:
        for month in months:
            if doy <= int(month):
                print('falls on:',months[month]['dss_name'])
                payload['dom'] = doy - payload['dom']
                for key in months[month]:
                    payload[key] = months[month][key]
                break
            payload['dom'] = int(month)
    print('payload:\n')
    pprint(payload)
    #return payload


parse_date(test_date)


