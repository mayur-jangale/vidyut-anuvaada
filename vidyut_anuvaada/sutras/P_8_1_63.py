# Sutra प.8.1.63: चादिलोपे विभाषा
# ṅamo lopaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.63"
SUTRA_TEXT = "चादिलोपे विभाषा"
SUTRA_DESC = "ṅamo lopaḥ — repeated"


class Sutra8163:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.63: अग्निः'),
		('रामः', '', 'प.8.1.63: रामः'),
		('सीता', '', 'प.8.1.63: सीता'),
	]

