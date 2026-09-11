# Sutra प.5.3.11: इदमो हः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — idamo haH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.11"
SUTRA_TEXT = "इदमो हः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — idamo haH"


class Sutra5311:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.11: अग्निः'),
		('रामः', '', 'प.5.3.11: रामः'),
		('सीता', '', 'प.5.3.11: सीता'),
	]

