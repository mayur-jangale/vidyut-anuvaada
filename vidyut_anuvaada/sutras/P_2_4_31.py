# Sutra प.2.4.31: अर्धर्चाः पुंसि च
# (Samasa (compound formation)) — arDarcAH puMsi ca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.31"
SUTRA_TEXT = "अर्धर्चाः पुंसि च"
SUTRA_DESC = "(Samasa (compound formation)) — arDarcAH puMsi ca"


class Sutra2431:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

