# Sutra प.5.1.114: आकालिकडाद्यन्तवचने
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — AkAlikaqAdyantavacane

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.114"
SUTRA_TEXT = "आकालिकडाद्यन्तवचने"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — AkAlikaqAdyantavacane"


class Sutra51114:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.114: अग्निः'),
		('रामः', '', 'प.5.1.114: रामः'),
		('सीता', '', 'प.5.1.114: सीता'),
	]

