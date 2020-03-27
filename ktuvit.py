import requests

class KtuvitApi(object):
	"""docstring for KtuvitApi"""
	def __init__(self, protocol="http", domain="api.screwzira.com"):
		super(KtuvitApi, self).__init__()
		self._session = requests.session()
		self.protocol = protocol
		self.domain = domain

	def api_call(url, params):

	def find_film(search_type, pharse, version="1.0"):
