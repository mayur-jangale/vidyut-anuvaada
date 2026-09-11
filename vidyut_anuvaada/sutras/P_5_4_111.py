# Sutra प.5.4.111: झयः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — JayaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.111"
SUTRA_TEXT = "झयः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — JayaH"


class Sutra54111:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.111: अग्निः'),
		('रामः', '', 'प.5.4.111: रामः'),
		('सीता', '', 'प.5.4.111: सीता'),
	]

