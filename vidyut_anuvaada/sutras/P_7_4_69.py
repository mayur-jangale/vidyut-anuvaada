# Sutra प.7.4.69: दीर्घ इणः किति
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.69"
SUTRA_TEXT = "दीर्घ इणः किति"
SUTRA_DESC = "taddhita — continued"


class Sutra7469:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.69: अग्निः'),
		('रामः', '', 'प.7.4.69: रामः'),
		('सीता', '', 'प.7.4.69: सीता'),
	]

