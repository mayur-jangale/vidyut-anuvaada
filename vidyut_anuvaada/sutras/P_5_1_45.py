# Sutra प.5.1.45: तस्य वापः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tasya vApaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.45"
SUTRA_TEXT = "तस्य वापः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tasya vApaH"


class Sutra5145:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.45: अग्निः'),
		('रामः', '', 'प.5.1.45: रामः'),
		('सीता', '', 'प.5.1.45: सीता'),
	]

