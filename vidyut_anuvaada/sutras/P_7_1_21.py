# Sutra प.7.1.21: अष्टाभ्य औश्
# (Taddhita (secondary derivations)) — azwABya OS

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.21"
SUTRA_TEXT = "अष्टाभ्य औश्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — azwABya OS"


class Sutra7121:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.21: अग्निः'),
		('रामः', '', 'प.7.1.21: रामः'),
		('सीता', '', 'प.7.1.21: सीता'),
	]

