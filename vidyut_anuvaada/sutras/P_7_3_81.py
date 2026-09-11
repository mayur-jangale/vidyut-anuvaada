# Sutra प.7.3.81: मीनातेर्निगमे
# (Taddhita (secondary derivations)) — mInAternigame

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.81"
SUTRA_TEXT = "मीनातेर्निगमे"
SUTRA_DESC = "(Taddhita (secondary derivations)) — mInAternigame"


class Sutra7381:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.81: अग्निः'),
		('रामः', '', 'प.7.3.81: रामः'),
		('सीता', '', 'प.7.3.81: सीता'),
	]

