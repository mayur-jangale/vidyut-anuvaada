# Sutra प.6.2.94: संज्ञायां गिरिनिकाययोः
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.94"
SUTRA_TEXT = "संज्ञायां गिरिनिकाययोः"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6294:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.94: अग्निः'),
		('रामः', '', 'प.6.2.94: रामः'),
		('सीता', '', 'प.6.2.94: सीता'),
	]

