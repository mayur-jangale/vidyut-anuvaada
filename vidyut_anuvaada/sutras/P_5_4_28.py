# Sutra प.5.4.28: अवेः कः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — aveH kaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.28"
SUTRA_TEXT = "अवेः कः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — aveH kaH"


class Sutra5428:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.28: अग्निः'),
		('रामः', '', 'प.5.4.28: रामः'),
		('सीता', '', 'प.5.4.28: सीता'),
	]

