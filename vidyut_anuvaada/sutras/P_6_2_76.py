# Sutra प.6.2.76: शिल्पिनि चाकृञः
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.76"
SUTRA_TEXT = "शिल्पिनि चाकृञः"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6276:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.76: अग्निः'),
		('रामः', '', 'प.6.2.76: रामः'),
		('सीता', '', 'प.6.2.76: सीता'),
	]

