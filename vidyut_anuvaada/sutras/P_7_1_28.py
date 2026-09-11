# Sutra प.7.1.28: ङे प्रथमयोरम्
# (Taddhita (secondary derivations)) — Ne praTamayoram

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.28"
SUTRA_TEXT = "ङे प्रथमयोरम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Ne praTamayoram"


class Sutra7128:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.28: अग्निः'),
		('रामः', '', 'प.7.1.28: रामः'),
		('सीता', '', 'प.7.1.28: सीता'),
	]

