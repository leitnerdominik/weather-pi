from Adafruit_DHT import read_retry


def getDHT11Data():
    """return humidity and temperature from DHT11"""
    humidity, temperature = read_retry(11, 4);

    return humidity, temperature



def getTemp():
    temp = getDHT11Data()[1]
    return "Temp:{0:0.1f}ßC".format(temp)

def getHumidity():
    humidity = getDHT11Data()[0]
    return "LF:{0:0.1f}%".format(humidity)
