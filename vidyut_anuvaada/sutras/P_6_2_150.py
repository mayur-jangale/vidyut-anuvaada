# Sutra प.6.2.150: अनो भावकर्मवचनः
# (Sandhi (euphonic combination)) — ano BAvakarmavacanaH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.150"
SUTRA_TEXT = "अनो भावकर्मवचनः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — ano BAvakarmavacanaH"


class Sutra62150:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.150: अग्निः'),
		('रामः', '', 'प.6.2.150: रामः'),
		('सीता', '', 'प.6.2.150: सीता'),
	]

