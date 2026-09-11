# Sutra प.7.3.79: ज्ञाजनोर्जा
# (Taddhita (secondary derivations)) — jYAjanorjA

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.79"
SUTRA_TEXT = "ज्ञाजनोर्जा"
SUTRA_DESC = "(Taddhita (secondary derivations)) — jYAjanorjA"


class Sutra7379:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.79: अग्निः'),
		('रामः', '', 'प.7.3.79: रामः'),
		('सीता', '', 'प.7.3.79: सीता'),
	]

