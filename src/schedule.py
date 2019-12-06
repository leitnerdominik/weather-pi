#!python3

from time import sleep
from datetime import datetime

def check_tasks(weather, lcd_settings, lcd_display):
    """runs a task at a specific time"""
    current_time = datetime.now()
    if current_time.strftime("%S") == '00':
        lcd_display.lcd_update(weather)
        sleep(60)
    elif current_time.strftime("%H:%M") == '07:15' and not weather.weather_refreshed:
        weather.get_weather(lcd_settings.weather_city)
        weather.weather_refreshed = True
    if current_time.strftime("%H:%M") == '02:00':
        weather.weather_refreshed = False
