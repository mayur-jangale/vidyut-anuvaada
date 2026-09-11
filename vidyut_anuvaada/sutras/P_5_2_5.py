# Sutra प.5.2.5: सर्वचर्मणः कृतः खखञौ
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.5"
SUTRA_TEXT = "सर्वचर्मणः कृतः खखञौ"
SUTRA_DESC = "taddhita — continued"


class Sutra525:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.5: अग्निः'),
		('रामः', '', 'प.5.2.5: रामः'),
		('सीता', '', 'प.5.2.5: सीता'),
	]

