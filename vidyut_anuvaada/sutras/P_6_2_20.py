# Sutra प.6.2.20: वा भुवनम्
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.20"
SUTRA_TEXT = "वा भुवनम्"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6220:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.20: अग्निः'),
		('रामः', '', 'प.6.2.20: रामः'),
		('सीता', '', 'प.6.2.20: सीता'),
	]

