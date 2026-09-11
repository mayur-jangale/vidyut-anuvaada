# Sutra प.8.3.11: स्वतवान् पायौ
# aṅgasya — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.11"
SUTRA_TEXT = "स्वतवान् पायौ"
SUTRA_DESC = "aṅgasya — repeated"


class Sutra8311:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.11: अग्निः'),
		('रामः', '', 'प.8.3.11: रामः'),
		('सीता', '', 'प.8.3.11: सीता'),
	]

