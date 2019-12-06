from time import sleep

from lcddriver import lcd
import temp


class LCD_display:

    def __init__(self, lcd_settings):
        self.lcd = lcd()

        self.lcd_init(lcd_settings)

    def lcd_init(self, lcd_settings):
        """Show's a start message"""
        # phrase has to be a list
        init_text = ['Starting...', 'lcd-display!'.rjust(14)]
        init_time = 1  # How long in seconds the init text will be shown
        for display_row, phrase in enumerate(init_text, start=1):
            self.lcd.lcd_display_string(phrase, display_row)
        sleep(init_time)
        self.lcd.lcd_clear()

    def lcd_update(self, weather):
        """Update's/show's the text on the LCD-Display"""

        temparature = temp.getTemp()
        humidity = temp.getHumidity()

        self.lcd.lcd_clear()
        self.lcd.lcd_display_string('{}: {}...{}'.format(weather.city ,weather.min_temp, weather.max_temp), 1)
        self.lcd.lcd_display_string('Tag {}'.format(weather.day_description[:16]), 2)
        self.lcd.lcd_display_string('Nac {}'.format(weather.night_description[:16]), 3)
        self.lcd.lcd_display_string('{} {}'.format(temparature, humidity), 4)
