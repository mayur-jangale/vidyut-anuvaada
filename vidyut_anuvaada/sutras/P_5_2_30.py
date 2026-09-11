# Sutra प.5.2.30: अवात् कुटारच्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — avAt kuwAracca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.30"
SUTRA_TEXT = "अवात् कुटारच्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — avAt kuwAracca"


class Sutra5230:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.30: अग्निः'),
		('रामः', '', 'प.5.2.30: रामः'),
		('सीता', '', 'प.5.2.30: सीता'),
	]

