from googletrans import Translator
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import pymorphy3

nltk.download('popular')


def translate_text(text: str) -> str:
	"""
	Функция для перевода текста
	:param text: Текст для перевода
	:return: Переведенный с английского на русский язык текст
	"""

	return (
		Translator()
		.translate(
			text = text.strip(),
			dest = 'en',
			src = 'ru'
		)
		.text
	)


def get_word_synonyms(word: str) -> list[str]:
	"""
	Функция для поиска слов-синонимов к исходному слову
	:param word: Исходное слово
	:return: Список слов-синонимов
	"""

	result = []

	for synonym in wordnet.synsets(word):
		for lemma in synonym.lemmas():
			result.append(lemma.name())

	return result[:4]


def get_word_normal_form(word: str) -> str:
	"""
	Функция для получения нормальной формы слова
	:param word: Слово
	:return: Нормальная форма слова
	"""

	return pymorphy3.MorphAnalyzer().parse(word)[0].normal_form
