# Sutra प.8.3.76: स्फुरतिस्फुलत्योर्निर्निविभ्यः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.76"
SUTRA_TEXT = "स्फुरतिस्फुलत्योर्निर्निविभ्यः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8376:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.76: अग्निः'),
		('रामः', '', 'प.8.3.76: रामः'),
		('सीता', '', 'प.8.3.76: सीता'),
	]

