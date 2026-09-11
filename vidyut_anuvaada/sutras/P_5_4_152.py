# Sutra प.5.4.152: इनः स्त्रियाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — inaH striyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.152"
SUTRA_TEXT = "इनः स्त्रियाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — inaH striyAm"


class Sutra54152:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.152: अग्निः'),
		('रामः', '', 'प.5.4.152: रामः'),
		('सीता', '', 'प.5.4.152: सीता'),
	]

