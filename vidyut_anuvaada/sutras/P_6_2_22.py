# Sutra प.6.2.22: पूर्वे भूतपूर्वे
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.22"
SUTRA_TEXT = "पूर्वे भूतपूर्वे"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6222:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.22: अग्निः'),
		('रामः', '', 'प.6.2.22: रामः'),
		('सीता', '', 'प.6.2.22: सीता'),
	]

