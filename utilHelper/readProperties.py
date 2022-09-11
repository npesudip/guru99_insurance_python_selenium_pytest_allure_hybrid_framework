import configparser

config = configparser.RawConfigParser()
config.read(r"..\Configurations\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        # test_url = config.get('common info', 'baseURL')
        test_url = "https://demo.guru99.com/insurance/v1/index.php"
        return test_url

