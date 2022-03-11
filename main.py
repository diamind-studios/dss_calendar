from dsscalendar import DssCalendar
from datetime import date, timedelta
from pprint import pprint

# variables in calculation
# equinox could be 19th-21st




# Different dates of creation (BC)
age_coefficient = [
    {'date': 3925, 'source': ['Ken Johnson']},
    #{'date': [3960,3959], 'source': 'common'}, code needs updated so it can handle date intervals to deal with uncertainty
    {'date': 3942, 'source': ['Eusebius','Jerome']},
    {'date': 3761, 'source': ['Jose ben Halafta: Seder Olam Rabbah']},
    {'date': 4339, 'source': ['Seder Olam Zutta']},
    {'date': 4997, 'source': ['Kepler'],'location':'https://www.science20.com/science_20/kepler_young_earth_creationist-134613'},
    #{'date': 3998, 'source': ['Isaac Newton'],'location':'Chronology of Ancient Kingdoms: Amended'}, can't really confirm this one
    {'date': 5500, 'source': ['Septuagint']}
]

dsscal = DssCalendar()

# Apr 6, 32 A.D. - Daniel date (ch 9)
test_date = date(2005,3,17)


dss_date = dsscal.parse_date(test_date)

print('Payload:')
pprint(dss_date)