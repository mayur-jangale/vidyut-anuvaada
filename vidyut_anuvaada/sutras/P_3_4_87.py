# Sutra प.3.4.87: सेर्ह्यपिच्च
# āśīrliṅ — benedictive endings

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.87"
SUTRA_TEXT = "सेर्ह्यपिच्च"
SUTRA_DESC = "āśīrliṅ — benedictive endings"


class Sutra3487:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

