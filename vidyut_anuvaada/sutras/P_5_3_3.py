# Sutra प.5.3.3: इदम इश्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — idama iS

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.3"
SUTRA_TEXT = "इदम इश्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — idama iS"


class Sutra533:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.3: अग्निः'),
		('रामः', '', 'प.5.3.3: रामः'),
		('सीता', '', 'प.5.3.3: सीता'),
	]

