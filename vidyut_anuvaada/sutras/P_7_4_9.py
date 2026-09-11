# Sutra प.7.4.9: दयतेर्दिगि लिटि
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.9"
SUTRA_TEXT = "दयतेर्दिगि लिटि"
SUTRA_DESC = "taddhita — continued"


class Sutra749:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.9: अग्निः'),
		('रामः', '', 'प.7.4.9: रामः'),
		('सीता', '', 'प.7.4.9: सीता'),
	]

