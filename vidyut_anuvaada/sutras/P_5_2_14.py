# Sutra प.5.2.14: आगवीनः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — AgavInaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.14"
SUTRA_TEXT = "आगवीनः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — AgavInaH"


class Sutra5214:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.14: अग्निः'),
		('रामः', '', 'प.5.2.14: रामः'),
		('सीता', '', 'प.5.2.14: सीता'),
	]

