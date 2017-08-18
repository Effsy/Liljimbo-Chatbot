# testing ground for new feature - sending generic templates on facebook developer platform
'''
from wit import Wit
from gnewsclient import gnewsclient

wit_access_token = "HASFWGKV2HBFHTI6MXYSGI7HLZHVC7XN"
client = Wit(access_token = wit_access_token)

def wit_response(message_text):
	resp = client.message(message_text)
	categories = {'newstype': None, 'location': None}


	entities = list(resp['entities'])
	for entity in entities:
		categories[entity] = resp['entities'][entity][0]['value']

	return categories

def get_news_elements(categories):
	news_client = gnewsclient()
	news_client.query = ''

	if categories['newstype'] != None:
		news_client.query += categories['newstype'] + ' '
	if categories['location'] != None:
		news_client.query += categories['location']

	news_items = news_client.get_news()

	elements = []

	for item in news_items:
		element = {
			'title': item['title'],
			'buttons':[
				{
					'title': 'Read more..',
					'type':'web_url',
					'url': item['link']
				}
			],
			'image_url': item['img']
		}
		elements.append(element)

	return elements

print(get_news_elements(wit_response("I want sports news from Taiwan")))
'''