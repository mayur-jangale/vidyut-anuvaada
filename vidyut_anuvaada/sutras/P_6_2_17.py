# Sutra प.6.2.17: स्वं स्वामिनि
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.17"
SUTRA_TEXT = "स्वं स्वामिनि"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6217:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.17: अग्निः'),
		('रामः', '', 'प.6.2.17: रामः'),
		('सीता', '', 'प.6.2.17: सीता'),
	]

