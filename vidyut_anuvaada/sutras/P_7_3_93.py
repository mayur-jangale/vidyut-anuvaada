# Sutra प.7.3.93: ब्रुव ईट्
# (Taddhita (secondary derivations)) — bruva Iw

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.93"
SUTRA_TEXT = "ब्रुव ईट्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — bruva Iw"


class Sutra7393:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.93: अग्निः'),
		('रामः', '', 'प.7.3.93: रामः'),
		('सीता', '', 'प.7.3.93: सीता'),
	]

