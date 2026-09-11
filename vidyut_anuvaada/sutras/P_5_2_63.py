# Sutra प.5.2.63: तत्र कुशलः पथः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tatra kuSalaH paTaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.63"
SUTRA_TEXT = "तत्र कुशलः पथः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tatra kuSalaH paTaH"


class Sutra5263:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.63: अग्निः'),
		('रामः', '', 'प.5.2.63: रामः'),
		('सीता', '', 'प.5.2.63: सीता'),
	]

