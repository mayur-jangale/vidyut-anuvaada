# Sutra प.7.1.89: पुंसोऽसुङ्
# (Taddhita (secondary derivations)) — puMso'suN

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.89"
SUTRA_TEXT = "पुंसोऽसुङ्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — puMso'suN"


class Sutra7189:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.89: अग्निः'),
		('रामः', '', 'प.7.1.89: रामः'),
		('सीता', '', 'प.7.1.89: सीता'),
	]

