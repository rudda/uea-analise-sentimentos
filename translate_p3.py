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


def write(data, dataset_full):
	i =0; # create an index
	target = "en-US" # target that will be translated
	#emoji pattern
	emoji_pattern = re.compile("["
			u"\U0001F600-\U0001F64F"  # emoticons
			u"\U0001F300-\U0001F5FF"  # symbols & pictographs
			u"\U0001F680-\U0001F6FF"  # transport & map symbols
			u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
							   "]+", flags=re.UNICODE)
	#aux= []
	#canITranslate = False

	#latestId = '419306143'

	for line in data:
		try:
			#increment index - just for fun :)
			i  = i + 1
			# parse to json format
			data_json = json.loads(str(line))
			#aux = data_json
			#remove emojis from review
			#review_str = emoji_pattern.sub(r'', str(data_json['reviewBody']))
			#remove emojis from title
			#title_str = emoji_pattern.sub(r'', str(data_json['title']))

			dataset_full.write(json.dumps(data_json) + "\n")
			print(i)


			# if( data_json['reviewId'] == latestId):
			# 	canITranslate = True
			# 	print('I can translate now!!')

			# if( data_json['reviewId'] != latestId and canITranslate == False):
			# 	print('looking for')

		except KeyError:
			print("there is a key error")
			#data_error.write(json.dumps(aux) + "\n")



def load():

	#dataset = open('data/dataset-v2.dat', 'r', encoding='utf-8')
	data_enUS     = open('data/dataset-enUS.json', 'r', encoding='utf-8')
	data_enUS_2   = open('data/dataset-enUS-p2.json', 'r', encoding='utf-8')
	data_enUS_p1  = open('data/dataset-enUS-p3.json', 'r', encoding='utf-8')
	data_enUS_p2  = open('data/dataset-enUS-p4.json', 'r', encoding='utf-8')
	data_enUS_p3  = open('data/dataset-enUS-p5.json', 'r', encoding='utf-8')
	data_enUS_p4  = open('data/dataset-enUS-p5.json', 'r', encoding='utf-8')
	data_enUS_p5  = open('data/dataset-enUS-p5.json', 'r', encoding='utf-8')
	data_enUS_p6  = open('data/dataset-enUS-p5.json', 'r', encoding='utf-8')

	dataset_full = open('data/dataset-full.json', 'a', encoding='utf-8')

	write(data_enUS, dataset_full)
	write(data_enUS_2, dataset_full)
	write(data_enUS_p1, dataset_full)
	write(data_enUS_p2, dataset_full)
	write(data_enUS_p3, dataset_full)
	write(data_enUS_p4, dataset_full)
	write(data_enUS_p5, dataset_full)
	write(data_enUS_p6, dataset_full)

	#close files streams
	data_enUS.close()
	data_enUS_2.close()
	data_enUS_p1.close()
	data_enUS_p2.close()
	data_enUS_p3.close()
	data_enUS_p4.close()
	data_enUS_p5.close()
	data_enUS_p6.close()

	print('finish!!')



load()

