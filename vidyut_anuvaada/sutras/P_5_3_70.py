# Sutra प.5.3.70: प्रागिवात्कः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — prAgivAtkaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.70"
SUTRA_TEXT = "प्रागिवात्कः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — prAgivAtkaH"


class Sutra5370:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.70: अग्निः'),
		('रामः', '', 'प.5.3.70: रामः'),
		('सीता', '', 'प.5.3.70: सीता'),
	]

