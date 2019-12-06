from time import sleep

from weather import Weather
from lcd_display import LCD_display
from settings import Settings
import schedule


def main():
    lcd_settings = Settings()
    weather = Weather(lcd_settings)
    lcd = LCD_display(lcd_settings)

    weather.get_weather(lcd_settings.weather_city)
    lcd.lcd_update(weather)
    while True:
        schedule.check_tasks(weather, lcd_settings, lcd)
        sleep(0.2)


if __name__ == '__main__':
    main()
