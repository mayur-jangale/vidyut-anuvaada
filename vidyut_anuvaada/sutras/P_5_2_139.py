# Sutra प.5.2.139: तुन्दिवलिवटेर्भः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tundivalivawerBaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.139"
SUTRA_TEXT = "तुन्दिवलिवटेर्भः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tundivalivawerBaH"


class Sutra52139:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.139: अग्निः'),
		('रामः', '', 'प.5.2.139: रामः'),
		('सीता', '', 'प.5.2.139: सीता'),
	]

