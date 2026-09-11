# Sutra प.7.2.86: युष्मदस्मदोरनादेशे
# (Taddhita (secondary derivations)) — yuzmadasmadoranAdeSe

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.86"
SUTRA_TEXT = "युष्मदस्मदोरनादेशे"
SUTRA_DESC = "(Taddhita (secondary derivations)) — yuzmadasmadoranAdeSe"


class Sutra7286:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.86: अग्निः'),
		('रामः', '', 'प.7.2.86: रामः'),
		('सीता', '', 'प.7.2.86: सीता'),
	]

