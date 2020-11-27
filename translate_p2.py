"""Translates text into the target language.

Target must be an ISO 639-1 language code.
See https://g.co/cloud/translate/v2/translate-reference#supported_languages
"""
from google.cloud import translate_v2 as translate
import json
import re



def googleTranslator(text, target):

	# The text to translate
	#text = ["oi", "tudo bom?"]
	# The target language
	target = "en"
	# Text can also be a sequence of strings, in which case this method
	# will return a sequence of results for each text.
	translate_client = translate.Client()
	result = translate_client.translate(text, target_language=target)
	return result
	# print(u"Text: {}".format(result["input"]))
	# print("Translation:", result["translatedText"])

def load():

	dataset = open('data/dataset-v2.dat', 'r', encoding='utf-8')
	data_enUS_p2 = open('data/dataset-restante.json', 'a', encoding='utf-8')


	data_error = open('data/dataset-error.json', 'a', encoding='utf-8')

	i =0; # create an index
	target = "en-US" # target that will be translated
	#emoji pattern
	emoji_pattern = re.compile("["
			u"\U0001F600-\U0001F64F"  # emoticons
			u"\U0001F300-\U0001F5FF"  # symbols & pictographs
			u"\U0001F680-\U0001F6FF"  # transport & map symbols
			u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
							   "]+", flags=re.UNICODE)
	aux= []
	canITranslate = False

	latestId = '467387303'
	j=0
	for line in dataset:
		try:
			#increment index - just for fun :)
			i  = i + 1
			# parse to json format
			data_json = json.loads(str(line))
			aux = data_json
			#remove emojis from review
			review_str = emoji_pattern.sub(r'', str(data_json['reviewBody']))
			#remove emojis from title
			title_str = emoji_pattern.sub(r'', str(data_json['title']))

			if(canITranslate):

				#translatting
				#review_str = googleTranslator(review_str, target)
				#title_str = googleTranslator(title_str, target)
				#assingement
				#data_json['title'] = title_str['translatedText']
				#data_json['reviewBody'] = review_str['translatedText']

				if( i > 40000 and i <= 70000):
					#write
					data_enUS_p2.write(json.dumps(data_json) + "\n")
					j= j + 1
					print('p2',i,j)

			if( data_json['reviewId'] == latestId):
				canITranslate = True
				print('I can translate now!!')

			if( data_json['reviewId'] != latestId and canITranslate == False):
				print('looking for')

		except KeyError:
			print("there is a key error")
			data_error.write(json.dumps(aux) + "\n")


	#close files streams
	data_enUS.close()
	dataset.close()
	data_error.close()
	print('data translate finish!!')



load()

