# Sutra प.7.1.93: अनङ् सौ
# (Taddhita (secondary derivations)) — anaN sO

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.93"
SUTRA_TEXT = "अनङ् सौ"
SUTRA_DESC = "(Taddhita (secondary derivations)) — anaN sO"


class Sutra7193:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.93: अग्निः'),
		('रामः', '', 'प.7.1.93: रामः'),
		('सीता', '', 'प.7.1.93: सीता'),
	]

