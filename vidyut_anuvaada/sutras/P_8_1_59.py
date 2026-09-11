# Sutra प.8.1.59: चवायोगे प्रथमा
# ṅamo lopaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.59"
SUTRA_TEXT = "चवायोगे प्रथमा"
SUTRA_DESC = "ṅamo lopaḥ — repeated"


class Sutra8159:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.59: अग्निः'),
		('रामः', '', 'प.8.1.59: रामः'),
		('सीता', '', 'प.8.1.59: सीता'),
	]

