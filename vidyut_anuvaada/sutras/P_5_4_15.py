# Sutra प.5.4.15: अणिनुणः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — aRinuRaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.15"
SUTRA_TEXT = "अणिनुणः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — aRinuRaH"


class Sutra5415:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.15: अग्निः'),
		('रामः', '', 'प.5.4.15: रामः'),
		('सीता', '', 'प.5.4.15: सीता'),
	]

