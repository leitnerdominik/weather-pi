
class Settings:

    def __init__(self):
        """Stores all the settings"""
        # Weather settings
        self.WEATHER_TOKEN = 'AEelEAvZsbohTPic5CXFS2hXaL1QUatV'
        self.weather_language = 'de-de'
        self.weather_city = 'Brixen'

        # data settings
        self.directory_path = 'weather_data'
        self.csv_file = 'weatherdata.csv'
