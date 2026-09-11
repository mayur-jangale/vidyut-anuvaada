# Sutra प.8.3.41: इदुदुपधस्य चाप्रत्ययस्य
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.41"
SUTRA_TEXT = "इदुदुपधस्य चाप्रत्ययस्य"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8341:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.41: अग्निः'),
		('रामः', '', 'प.8.3.41: रामः'),
		('सीता', '', 'प.8.3.41: सीता'),
	]

