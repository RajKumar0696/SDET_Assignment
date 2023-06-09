import configparser

file = open("Configuration/config.ini","r")
config = configparser.RawConfigParser(allow_no_value=True)
config.read_file(file)

class ReadProperties:
    @staticmethod
    def get_broken_image_url():
        url = config.get('common_info', 'broken_image_url')
        return url