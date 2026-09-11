# Sutra प.8.4.52: दीर्घादाचार्याणाम्
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.52"
SUTRA_TEXT = "दीर्घादाचार्याणाम्"
SUTRA_DESC = "final transformations — continued"


class Sutra8452:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.52: अग्निः'),
		('रामः', '', 'प.8.4.52: रामः'),
		('सीता', '', 'प.8.4.52: सीता'),
	]

