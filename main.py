import RequestProcessor
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import pymorphy3
from googletrans import Translator
from functions import *


def main():
	request_processor: RequestProcessor = RequestProcessor.RequestProcessor()
	request: str = 'Быстро дойти до библиотеки'
	translated_request: str = (
		Translator()
		.translate(
			text = request.strip(),
			dest = 'en',
			src = 'ru'
		)
		.text
	)

	print(request_processor.process_request(translated_request))


if __name__ == '__main__':
	main()
