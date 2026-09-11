# Sutra प.5.4.108: अनश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — anaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.108"
SUTRA_TEXT = "अनश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — anaSca"


class Sutra54108:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.108: अग्निः'),
		('रामः', '', 'प.5.4.108: रामः'),
		('सीता', '', 'प.5.4.108: सीता'),
	]

