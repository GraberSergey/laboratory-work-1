import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import pymorphy3
from functions import *
import itertools
from progressbar import ProgressBar
import time

nltk.download('popular')


class RequestProcessor:
	def __init__(self):
		self.__morph = pymorphy3.MorphAnalyzer()
		self.__request = None

	def process_request(self, request: str):
		"""
		Метод для обработки запроса пользователя

		:param request: Запрос пользователя
		:return: Ответ
		"""

		self.__request = request

		(
			self
			.__tokenize_words()
			.__remove_punctuation()
			.__synonymize_request()
			.__translate_requests()
		)

		return self.__request

	def __tokenize_words(self) -> 'RequestProcessor':
		"""
		Метод для токенизации (получения) слов запроса

		:return: Ссылка на текущий экземпляр класса
		"""

		self.__request = [
			get_word_normal_form(word).lower()
			for word in nltk.word_tokenize(self.__request)
		]

		return self

	def __remove_punctuation(self) -> 'RequestProcessor':
		"""
		Метод для удаления знаков препинания из списка слов запроса

		:return: Ссылка на текущий экземпляр класса
		"""

		self.__request = [
			word for word in self.__request if word.isalnum()
		]

		return self

	def __synonymize_request(self) -> 'RequestProcessor':
		"""
		Функция для подбора подходящего по смыслу запроса
		:return: Ссылка на текущий экземпляр класса
		"""

		requests: list[list[str]] = []
		synonyms: dict[str, list[str]] = {}

		for word in self.__request:
			synonyms[word] = [word] + get_word_synonyms(word)

		self.__synonymized_requests: list[list[str]] = [
			synonymized_request for synonymized_request in itertools.product(*synonyms.values())
		]

		for x in self.__synonymized_requests:
			print(x)

		return self

	def __translate_requests(self) -> 'RequestProcessor':
		"""
		Функция для перевода запроса
		:return: Ссылка на текущий экземпляр класса
		"""

		result: set[str] = set()

		for index, request in enumerate(self.__synonymized_requests):
			request = ' '.join(request)
			request_ru: str = (
				Translator()
				.translate(
					text = request,
					dest = 'ru',
					src = 'en'
				)
				.text
			)

			print('\n'.join([
				'Перевод текста',
				f'  ENG: {request}',
				f'  RU: {request_ru}'
			]))

			result.add(request_ru)

		for request in result:
			print(request)


