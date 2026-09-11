# Sutra प.6.3.113: साढ्यै साढ्वा साढेति निगमे
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.113"
SUTRA_TEXT = "साढ्यै साढ्वा साढेति निगमे"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63113:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.113: अग्निः'),
		('रामः', '', 'प.6.3.113: रामः'),
		('सीता', '', 'प.6.3.113: सीता'),
	]

