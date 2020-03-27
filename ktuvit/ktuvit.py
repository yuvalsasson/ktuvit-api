import requests
import json

class ApiError(Exception):
	pass

class KtuvitApi(object):
	"""
	Implementing Ktuvit API. For further information see: https://www.ktuvit.me/ApiDocumentation.aspx. 
	"""
	def __init__(self, protocol="http", domain="api.screwzira.com"):
		super(KtuvitApi, self).__init__()
		self._session = requests.session()
		self.protocol = protocol
		self.domain = domain

	def do_json_api(self, path, params):
		"""
			Call the given endpoint (path)
			:param str path: the endpoint to reach
			:param dict params: Dictionary of parameters to send the endpoint
		"""
		response = self.do_api(path, params)
		# there is a bug in the api: The response is json of json. Therefore we need to decode it twice.
		result = json.loads(response.content)

		# result may be encoded second time
		try:
			result = json.loads(result)
		except json.JSONDecodeError:
			pass

		if result["IsSuccess"] == False or result['ErrorMessage'] is not None:
			raise ApiError(result["ErrorMessage"])
		return result

	def do_api(self, path, params):
		url = f"{self.protocol}://{self.domain}/{path}"
		headers = {
			"Content-Type" : "application/json"

		}
		query={
			"request":params
		}
		data = json.dumps(query)
		return requests.post(url, headers=headers, data=data)

		
	def find_film(self, search_type, phrase, version="1.0"):
		"""
		Possible search types: FilmName, Subtitle, ImdbID
		"""
		return self.do_json_api("FindFilm", {"SearchType" : search_type, "SearchPhrase" : phrase, "Version" : "1.0"})

	def find_series(self, search_type, phrase, season, episode, version='1.0'):
		"""
		Possible search types: FilmName, Subtitle, ImdbID
		"""
		return self.do_json_api("FindSeries", {
			"SearchType":search_type,
			'SearchPhrase':phrase,
			'Season':str(season),
			'Episode':str(episode),
			'Version':version
			})

	def get_subtitle(self, subtitle_id, font_size=None, hex_color=None):
		#TODO: Add support for exceptions 
		params = {
			"subtitleID" : subtitle_id # Documentation is wrong, param name starts with lowercase 's'
		}
		if font_size is not None:
			params["FontSize"] = int(font_size)
		
		if hex_color is not None:
			params["HexColor"] = str(hex_color)
		
		return self.do_api("Download", params).content