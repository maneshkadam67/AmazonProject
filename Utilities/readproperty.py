import configparser
config=configparser.RawConfigParser()
config.read(".\\Configuration\config.ini")
class ReadConfig:
    @staticmethod
    def getURL():
        url=config.get('common-info','baseURL')
        return url
    @staticmethod
    def getUserName():
        username=config.get('common-info','userName')
        return username
    @staticmethod
    def getPassword():
        password=config.get('common-info','password')
        return password
    @staticmethod
    def getProductName():
        productName=config.get('common-info','productSearch')
        return productName
