"""Testing methods for the Weather class."""
import unittest
import weather


class TestTodayMethods(unittest.TestCase):
    """docstring for TestTodaysWeather."""

    def setUp(self):
        """Setup for the tests."""
        try:
            self.weather_keys = ['reference_time', 'sunset_time',
                                 'sunrise_time', 'clouds', 'rain',
                                 'snow', 'wind', 'humidity', 'pressure',
                                 'temperature', 'status', 'detailed_status',
                                 'weather_code', 'weather_icon_name',
                                 'visibility_distance', 'dewpoint',
                                 'humidex', 'heat_index']
            self.weather = weather.Weather()
        except Exception as e:
            raise
        finally:
            pass

    def test_today_is_dict(self):
        """'today' is a dictionary."""
        try:
            self.assertTrue(isinstance(self.weather.today, dict))
        except Exception as e:
            raise
        finally:
            pass

    def test_today_has_keys(self):
        """'today' has appropriate keys."""
        try:
            self.assertEqual(self.weather_keys,
                             list(self.weather.today.keys()))
        except Exception as e:
            raise
        finally:
            pass

    def test_reference_time(self):
        """reference_time is an int."""
        try:
            self.assertTrue(int(self.weather.today['reference_time']))
        except Exception as e:
            raise
        finally:
            pass

    def test_sunset_time(self):
        """sunset_time is an int or none."""
        try:
            self.assertTrue(isinstance(self.weather.today['sunset_time'], int)
                            or isinstance(self.weather.today['sunset_time'],
                                          type(None)))
        except Exception as e:
            raise
        finally:
            pass

    def test_sunrise_time(self):
        """sunrise_time is an int or none."""
        try:
            self.assertTrue(isinstance(self.weather.today['sunrise_time'], int)
                            or isinstance(self.weather.today['sunrise_time'],
                                          type(None)))
        except Exception as e:
            raise
        finally:
            pass

    def test_clouds(self):
        """'clouds' is an int."""
        try:
            self.assertTrue(int(self.weather.today['clouds']))
        except Exception as e:
            raise
        finally:
            pass

    def test_rain(self):
        """'rain' is a dictionary."""
        try:
            self.assertTrue(isinstance(self.weather.today['rain'], dict))
        except Exception as e:
            raise
        finally:
            pass

    def test_snow(self):
        """'snow' is a dictionary."""
        try:
            self.assertTrue(isinstance(self.weather.today['snow'], dict))
        except Exception as e:
            raise
        finally:
            pass

    def test_wind(self):
        """'wind' is a dictionary."""
        try:
            self.assertTrue(isinstance(self.weather.today['wind'], dict))
        except Exception as e:
            raise
        finally:
            pass

    def test_humidity(self):
        """'humidity' is an int."""
        try:
            self.assertTrue(int(self.weather.today['humidity']))
        except Exception as e:
            raise
        finally:
            pass

    def test_pressure(self):
        """'pressure' is a dictionary."""
        try:
            self.assertTrue(isinstance(self.weather.today['pressure'], dict))
        except Exception as e:
            raise
        finally:
            pass

    def test_temperature(self):
        """'temperature' is a dictionary."""
        try:
            self.assertTrue(isinstance(self.weather.today['temperature'],
                                       dict))
        except Exception as e:
            raise
        finally:
            pass

    def test_status(self):
        """'status' is a string."""
        try:
            self.assertTrue(isinstance(self.weather.today['status'], str))
        except Exception as e:
            raise
        finally:
            pass

    def test_detailed_status(self):
        """detailed_status is a string."""
        try:
            self.assertTrue(isinstance(self.weather.today['detailed_status'],
                                       str))
        except Exception as e:
            raise
        finally:
            pass

    def test_weather_code(self):
        """weather_code is an int."""
        try:
            self.assertTrue(int(self.weather.today['weather_code']))
        except Exception as e:
            raise
        finally:
            pass

    def test_weather_icon_name(self):
        """weather_icon_name is a string."""
        try:
            self.assertTrue(isinstance(self.weather.today['weather_icon_name'],
                                       str))
        except Exception as e:
            raise
        finally:
            pass

    def test_dewpoint(self):
        """'dewpoint' is a float or None."""
        try:
            self.assertTrue(isinstance(self.weather.today['dewpoint'], float)
                            or isinstance(self.weather.today['dewpoint'],
                                          type(None)))
        except Exception as e:
            raise
        finally:
            pass

    def test_humidex(self):
        """'humidex' is a float or None."""
        try:
            self.assertTrue(isinstance(self.weather.today['humidex'], float)
                            or isinstance(self.weather.today['humidex'],
                                          type(None)))
        except Exception as e:
            raise
        finally:
            pass

    def test_heat_index(self):
        """'heat_index' is a float or None."""
        try:
            self.assertTrue(isinstance(self.weather.today['heat_index'], float)
                            or isinstance(self.weather.today['heat_index'],
                                          type(None)))
        except Exception as e:
            raise
        finally:
            pass


class TestForecastMethods(unittest.TestCase):
    """docstring for TestForecast."""

    def setUp(self):
        """Setup for the tests."""
        try:
            self.weather_keys = ['reference_time', 'sunset_time',
                                 'sunrise_time', 'clouds', 'rain',
                                 'snow', 'wind', 'humidity', 'pressure',
                                 'temperature', 'status', 'detailed_status',
                                 'weather_code', 'weather_icon_name',
                                 'visibility_distance', 'dewpoint',
                                 'humidex', 'heat_index']
            self.weather = weather.Weather()
        except Exception as e:
            raise
        finally:
            pass

    def test_forecasts(self):
        """'forecasts' is a dictionary of dictionaries."""
        try:
            self.assertTrue(isinstance(self.weather.forecasts, list))
            for __forecast in self.weather.forecasts:
                with self.subTest(__forecast=__forecast):
                    self.assertTrue(isinstance(__forecast, dict))
                    self.assertEqual(self.weather_keys,
                                     list(__forecast.keys()))
        except Exception as e:
            raise
        finally:
            pass


if __name__ == '__main__':
    unittest.main()