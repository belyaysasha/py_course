import xml.etree.ElementTree as ET

class TemperatureConverter:

    """

    Класс для конвертации температуры.

    """

    @staticmethod
    def convert_celsius_to_fahrenheit(temperature_in_celsius):

        """

        Конвертирует температуру из Цельсия в Фаренгейт.
        celsius: Температура в градусах Цельсия
        :return: Температура в градусах Фаренгейта, округленная до одного знака после запятой

        """

        temperature_in_fahrenheit = (9/5) * temperature_in_celsius + 32
        return round(temperature_in_fahrenheit, 1)  # Округляем до одного знака после запятой


class ForecastXmlParser:

    """

    Класс для парсинга данных из forecast.xml.

    """
    
    def __init__(self, xml_file):

        """

        Инициализирует парсер с указанным XML файлом.
        xml_file: Путь к XML файлу

        """

        self.xml_file = xml_file


    def parse(self):

        """

        Парсит XML файл и выводит прогноз погоды.
        Формат вывода: weekday - temperature in celsius - temperature in fahrenheit

        """

        # Загружаем и парсим XML файл

        tree = ET.parse(self.xml_file)
        root = tree.getroot()

        # Проходим по всем элементам "day" в XML

        for child in root.findall('child'):
            day = child.get('day')  # Получаем день недели
            temp_celsius = float(child.find('temperature').text)  # Получаем температуру в Цельсиях

            # Конвертируем температуру в Фаренгейты
            temp_fahrenheit = TemperatureConverter.convert_celsius_to_fahrenheit(temp_celsius)     

            # Печатаем результат в нужном формате
            print(f"{day} - {temp_celsius}°C - {temp_fahrenheit}°F")



# Пример использования

if __name__ == "__main__":

    # Укажите путь к вашему XML файлу здесь

    xml_file_path = 'forecast.xml'

    
    # Создаем экземпляр парсера и вызываем метод parse

    parser = ForecastXmlParser(xml_file_path)
    parser.parse()
