from flask import Flask

class Configurations:
	SERVER_URL = None
	ACCESS_TOKEN = None


sdk = Flask('fyleplatformsdk')
sdk.config.from_object(Configurations)
