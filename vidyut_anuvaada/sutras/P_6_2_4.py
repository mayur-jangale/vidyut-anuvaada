# Sutra प.6.2.4: गाधलवणयोः प्रमाणे
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.4"
SUTRA_TEXT = "गाधलवणयोः प्रमाणे"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra624:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.4: अग्निः'),
		('रामः', '', 'प.6.2.4: रामः'),
		('सीता', '', 'प.6.2.4: सीता'),
	]

