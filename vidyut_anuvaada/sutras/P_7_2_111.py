# Sutra प.7.2.111: इदोऽय् पुंसि
# (Taddhita (secondary derivations)) — ido'y puMsi

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.111"
SUTRA_TEXT = "इदोऽय् पुंसि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ido'y puMsi"


class Sutra72111:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.111: अग्निः'),
		('रामः', '', 'प.7.2.111: रामः'),
		('सीता', '', 'प.7.2.111: सीता'),
	]

