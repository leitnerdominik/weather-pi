
import data_json


class Weather:

    def __init__(self, lcd_settings):
        self.url = 'http://dataservice.accuweather.com'
        self.token = lcd_settings.WEATHER_TOKEN
        self.language = lcd_settings.weather_language
        self.location_url = self.url + '/locations/v1/cities/search?apikey=' + self.token
        self.one_day_forecast_url = self.url + '/forecasts/v1/daily/1day/'

        # Check if today the weather refreshed
        self.weather_refreshed = False

    def get_city_id(self, city_name):
        url = '{}&q={}&language={}'.format(self.location_url, city_name, self.language)
        jsContent = data_json.get_json_from_url(url)
        cityID = jsContent[0]["Key"]

        return cityID

    def get_weather_json_data(self, city_name):
        """Stores the weatherdata in a dictionary and return that"""
        cityID = self.get_city_id(city_name)
        weatherData = {}

        url = '{}{}?apikey={}&language={}'.format(self.one_day_forecast_url, cityID, self.token, self.language)
        jsWeatherData = data_json.get_json_from_url(url)
        # print(jsWeatherData['DailyForecasts'][0]['Temperature'])

        dailyForecastData = jsWeatherData['DailyForecasts'][0]

        # date = dailyForecastData['EpochDate']
        weatherData['minTemp'] = self.convert_fahrenheit_to_celsius(dailyForecastData['Temperature']['Minimum']['Value'])
        weatherData['maxTemp'] = self.convert_fahrenheit_to_celsius(dailyForecastData['Temperature']['Maximum']['Value'])

        weatherData['dayWeatherDescription'] = dailyForecastData['Day']['IconPhrase']

        weatherData['nightWeatherDescription'] = dailyForecastData['Night']['IconPhrase']

        return weatherData

    def get_weather(self, city_name):

        self.weatherData = self.get_weather_json_data(city_name)

        self.city = city_name

        self.min_temp = self.weatherData['minTemp']
        self.max_temp = self.weatherData['maxTemp']

        self.day_description = self.removeSpecialChars(self.weatherData['dayWeatherDescription'])
        self.night_description = self.removeSpecialChars(self.weatherData['nightWeatherDescription'])

    def convert_fahrenheit_to_celsius(self, fahrenheit):
        return str(round((fahrenheit - 32) / 1.8, 1)) + 'C'

    def removeSpecialChars(self, phrase):
        specialChars = [['ö', 'oe'], ['Ö', 'Oe'], ['ä', 'ae'], ['Ä', 'Ae'], ['ü', 'ue'], ['Ü', 'Ue'], ['ß', 'ss']]

        for specialChar, newChar in specialChars:
            if specialChar in phrase:
                phrase = phrase.replace(specialChar, newChar)

        return phrase
