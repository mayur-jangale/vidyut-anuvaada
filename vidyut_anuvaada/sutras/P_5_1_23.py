# Sutra प.5.1.23: वतोरिड्वा
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vatoriqvA

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.23"
SUTRA_TEXT = "वतोरिड्वा"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vatoriqvA"


class Sutra5123:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.23: अग्निः'),
		('रामः', '', 'प.5.1.23: रामः'),
		('सीता', '', 'प.5.1.23: सीता'),
	]

