# Sutra प.6.2.82: दीर्घकाशतुषभ्राष्ट्रवटं जे
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.82"
SUTRA_TEXT = "दीर्घकाशतुषभ्राष्ट्रवटं जे"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6282:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.82: अग्निः'),
		('रामः', '', 'प.6.2.82: रामः'),
		('सीता', '', 'प.6.2.82: सीता'),
	]

