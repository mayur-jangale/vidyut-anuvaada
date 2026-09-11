# Sutra प.5.4.54: तदधीनवचने
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadaDInavacane

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.54"
SUTRA_TEXT = "तदधीनवचने"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadaDInavacane"


class Sutra5454:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.54: अग्निः'),
		('रामः', '', 'प.5.4.54: रामः'),
		('सीता', '', 'प.5.4.54: सीता'),
	]

