import os
import csv


def create_csv(lcd_settings):
    if not os.path.exists(lcd_settings.directory_path):
        os.makedirs(lcd_settings.directory_path)

    if not os.path.exists('{}\\{}'.format(
            lcd_settings.directory_path, lcd_settings.csv_file)):
        output_csv = open(lcd_settings.csv_file, 'w', newline='')
        output_csv.close()
