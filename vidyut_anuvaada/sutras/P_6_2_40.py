# Sutra प.6.2.40: उष्ट्रः सादिवाम्योः
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.40"
SUTRA_TEXT = "उष्ट्रः सादिवाम्योः"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6240:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.40: अग्निः'),
		('रामः', '', 'प.6.2.40: रामः'),
		('सीता', '', 'प.6.2.40: सीता'),
	]

