import configparser

config=configparser.RawConfigParser()
config.read("../configuration/config.ini")

class Readconfig:
    @staticmethod
    def url():
        url=config.get('Qa details','url')
        return url

    @staticmethod
    def username():
        username = config.get('Qa details', 'username')
        return username

    @staticmethod
    def password():
        password = config.get('Qa details', 'password')
        return password