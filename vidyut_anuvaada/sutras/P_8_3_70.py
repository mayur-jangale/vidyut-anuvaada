# Sutra प.8.3.70: परिनिविभ्यः सेवसितसयसिवुसहसुट्स्तुस्वञ्जाम्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.70"
SUTRA_TEXT = "परिनिविभ्यः सेवसितसयसिवुसहसुट्स्तुस्वञ्जाम्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8370:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.70: अग्निः'),
		('रामः', '', 'प.8.3.70: रामः'),
		('सीता', '', 'प.8.3.70: सीता'),
	]

