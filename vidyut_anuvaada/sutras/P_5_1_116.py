# Sutra प.5.1.116: तत्र तस्येव
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tatra tasyeva

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.116"
SUTRA_TEXT = "तत्र तस्येव"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tatra tasyeva"


class Sutra51116:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.116: अग्निः'),
		('रामः', '', 'प.5.1.116: रामः'),
		('सीता', '', 'प.5.1.116: सीता'),
	]

