# Sutra प.5.1.84: अवयसि ठंश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — avayasi WaMSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.84"
SUTRA_TEXT = "अवयसि ठंश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — avayasi WaMSca"


class Sutra5184:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.84: अग्निः'),
		('रामः', '', 'प.5.1.84: रामः'),
		('सीता', '', 'प.5.1.84: सीता'),
	]

