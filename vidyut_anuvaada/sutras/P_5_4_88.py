# Sutra प.5.4.88: अह्नोऽह्न एतेभ्यः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ahno'hna eteByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.88"
SUTRA_TEXT = "अह्नोऽह्न एतेभ्यः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ahno'hna eteByaH"


class Sutra5488:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.88: अग्निः'),
		('रामः', '', 'प.5.4.88: रामः'),
		('सीता', '', 'प.5.4.88: सीता'),
	]

