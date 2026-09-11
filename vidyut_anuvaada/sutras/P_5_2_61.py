# Sutra प.5.2.61: विमुक्तादिभ्योऽण्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vimuktAdiByo'R

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.61"
SUTRA_TEXT = "विमुक्तादिभ्योऽण्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vimuktAdiByo'R"


class Sutra5261:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.61: अग्निः'),
		('रामः', '', 'प.5.2.61: रामः'),
		('सीता', '', 'प.5.2.61: सीता'),
	]

