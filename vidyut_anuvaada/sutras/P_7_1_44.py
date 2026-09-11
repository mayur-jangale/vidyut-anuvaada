# Sutra प.7.1.44: तस्य तात्
# (Taddhita (secondary derivations)) — tasya tAt

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.44"
SUTRA_TEXT = "तस्य तात्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — tasya tAt"


class Sutra7144:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.44: अग्निः'),
		('रामः', '', 'प.7.1.44: रामः'),
		('सीता', '', 'प.7.1.44: सीता'),
	]

