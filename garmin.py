

from garminconnect import (
    Garmin,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
    GarminConnectAuthenticationError,
)

import configparser

config = configparser.ConfigParser()
config.read('config.ini')



api = Garmin(config['Garmin']['username'], config['Garmin']['password'])

api.login()
print(api.get_full_name())

