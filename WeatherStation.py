"""Design and Implement weather monitoring system that notifies multiple display 
devices whenever the weather conditions change that follows the Observer Design 
Pattern. """
from abc import ABC, abstractmethod

class WeatherStation:
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.wind_speed = 0

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.wind_speed)

    def set_measurements(self, temperature, humidity, wind_speed):
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.notify_observers()

class DisplayDevice(ABC):
    @abstractmethod
    def update(self, temperature, humidity, wind_speed):
        pass

class TemperatureDisplay(DisplayDevice):
    def update(self, temperature, humidity, wind_speed):
        print(f"Temperature: {temperature}°C")

class HumidityDisplay(DisplayDevice):
    def update(self, temperature, humidity, wind_speed):
        print(f"Humidity: {humidity}%")

class WindSpeedDisplay(DisplayDevice):
    def update(self, temperature, humidity, wind_speed):
        print(f"Wind Speed: {wind_speed} km/h")

if __name__ == "__main__":
    weather_station = WeatherStation()

    temperature_display = TemperatureDisplay()
    humidity_display = HumidityDisplay()
    wind_speed_display = WindSpeedDisplay()

    weather_station.register_observer(temperature_display)
    weather_station.register_observer(humidity_display)
    weather_station.register_observer(wind_speed_display)

    weather_station.set_measurements(25, 60, 15)
    print()
    weather_station.set_measurements(28, 55, 20)