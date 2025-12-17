import urllib.parse

def get_path_query_params(url):
	parsed_url = urllib.parse.urlparse(str(url))
	path_query_params = parsed_url.path + '?' + parsed_url.query
	return path_query_params