# Sutra प.5.1.60: पञ्चद्दशतौ वर्गे वा
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — paYcaddaSatO varge vA

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.60"
SUTRA_TEXT = "पञ्चद्दशतौ वर्गे वा"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — paYcaddaSatO varge vA"


class Sutra5160:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.60: अग्निः'),
		('रामः', '', 'प.5.1.60: रामः'),
		('सीता', '', 'प.5.1.60: सीता'),
	]

