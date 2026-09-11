# Sutra प.7.4.32: अस्य च्वौ
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.32"
SUTRA_TEXT = "अस्य च्वौ"
SUTRA_DESC = "taddhita — continued"


class Sutra7432:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.32: अग्निः'),
		('रामः', '', 'प.7.4.32: रामः'),
		('सीता', '', 'प.7.4.32: सीता'),
	]

