from datetime import date, timedelta

class DssCalendar:
    def __init__(self, tekufah_starts_year=False):
        if tekufah_starts_year:
            self.months = {
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
        else:
            self.months = {
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
        self.equinox_day = 22 # could be anywhere between 19-22, because the year starts on tekufah and you can have equinox from 19th-22nd Mar.
        self.equinox_month = 3



    # this method returns the day of Tekufah Nisan, technically not a month, but the first of the year. 
    # if you need first day of the year to be Nisan 1, simply change 'ny.weekday() == 1' to 'ny.weekday() == 2' and comment out the second 'months' variable 
    def parse_new_year(self, year): 
        equinox = date(year,self.equinox_month,self.equinox_day)
        sub = 0
        while sub < 8:
            ny = equinox - timedelta(days=sub)
            if ny.weekday() == 1:
                return ny
            sub += 1

    def parse_date(self, d, creation_bc=3925):
        print(f'Calculating DSS date from: {d} according to creation in {creation_bc} BC.')
        ny = self.parse_new_year(d.year)
        print(f'New year: {ny}')
        payload = {
            'year': d.year+creation_bc,
            'dom': 0,
            'dow': d.strftime('%A')
        }
        if d < ny:
            print('before new years')
            ny = self.parse_new_year(d.year - 1)
            payload['year'] -= 1
        doy = (d - ny).days + 1
        #print('day of year:', doy)
        payload['doy'] = doy
        if doy > 364:
            print('Leap week')
            payload['month'] = 'N/A - Leap Week'
        else:
            for month in months:
                if doy <= int(month):
                    payload['dom'] = doy - payload['dom']
                    for key in months[month]:
                        payload[key] = months[month][key]
                    break
                payload['dom'] = int(month)
        return payload


