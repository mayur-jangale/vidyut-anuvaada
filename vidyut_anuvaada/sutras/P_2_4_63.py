# Sutra प.2.4.63: यस्कादिभ्यो गोत्रे
# (Samasa (compound formation)) — yaskAdiByo gotre

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.63"
SUTRA_TEXT = "यस्कादिभ्यो गोत्रे"
SUTRA_DESC = "(Samasa (compound formation)) — yaskAdiByo gotre"


class Sutra2463:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

