# Sutra प.7.3.24: प्राचां नगरान्ते
# (Taddhita (secondary derivations)) — prAcAM nagarAnte

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.24"
SUTRA_TEXT = "प्राचां नगरान्ते"
SUTRA_DESC = "(Taddhita (secondary derivations)) — prAcAM nagarAnte"


class Sutra7324:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.24: अग्निः'),
		('रामः', '', 'प.7.3.24: रामः'),
		('सीता', '', 'प.7.3.24: सीता'),
	]

