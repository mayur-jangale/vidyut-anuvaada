"""vidyut-anuvaada -- Sanskrit-to-English translation engine using Panini's Ashtadhyayi."""

__version__ = "0.1.0"

from vidyut_anuvaada.sutras.pipeline import (
	SanskritPipeline,
	TranslationResult,
)
from vidyut_anuvaada.sutras.tokenizer import SanskritTokenizer
from vidyut_anuvaada.sutras.lemmatizer import SanskritLemmatizer
from vidyut_anuvaada.sutras.sutra_engines import SutraEngine

from vidyut_anuvaada.sutras import dictionary

from vidyut_anuvaada.sutras.pipeline import translate


def tokenize(text):
	"""Tokenize Devanagari Sanskrit text into word tokens."""
	tokenizer = SanskritTokenizer()
	return tokenizer.tokenize(text)


def lemmatize(word, pos=""):
	"""Return (lemma, features_dict) for a Sanskrit word."""
	lem = SanskritLemmatizer()
	return lem.lemmatize(word, pos)


__all__ = [
	"__version__",
	# classes
	"SanskritPipeline",
	"SanskritTokenizer",
	"SanskritLemmatizer",
	"SutraEngine",
	"TranslationResult",
	# convenience functions
	"translate",
	"tokenize",
	"lemmatize",
	# dictionary module
	"dictionary",
]
