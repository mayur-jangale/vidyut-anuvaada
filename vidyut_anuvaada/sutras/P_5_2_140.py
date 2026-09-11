# Sutra प.5.2.140: अहंशुभमोर्युस्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ahaMSuBamoryus

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.140"
SUTRA_TEXT = "अहंशुभमोर्युस्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ahaMSuBamoryus"


class Sutra52140:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.140: अग्निः'),
		('रामः', '', 'प.5.2.140: रामः'),
		('सीता', '', 'प.5.2.140: सीता'),
	]

