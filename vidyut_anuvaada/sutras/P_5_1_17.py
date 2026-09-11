# Sutra प.5.1.17: परिखाया ढञ्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — pariKAyA QaY

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.17"
SUTRA_TEXT = "परिखाया ढञ्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — pariKAyA QaY"


class Sutra5117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.17: अग्निः'),
		('रामः', '', 'प.5.1.17: रामः'),
		('सीता', '', 'प.5.1.17: सीता'),
	]

