# Sutra प.6.2.83: अन्त्यात् पूर्वं बह्वचः
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.83"
SUTRA_TEXT = "अन्त्यात् पूर्वं बह्वचः"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6283:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.83: अग्निः'),
		('रामः', '', 'प.6.2.83: रामः'),
		('सीता', '', 'प.6.2.83: सीता'),
	]

