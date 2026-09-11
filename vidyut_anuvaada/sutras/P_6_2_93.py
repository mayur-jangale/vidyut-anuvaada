# Sutra प.6.2.93: सर्वं गुणकार्त्स्न्ये
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.93"
SUTRA_TEXT = "सर्वं गुणकार्त्स्न्ये"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6293:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.93: अग्निः'),
		('रामः', '', 'प.6.2.93: रामः'),
		('सीता', '', 'प.6.2.93: सीता'),
	]

