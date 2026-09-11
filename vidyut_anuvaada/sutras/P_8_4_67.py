# Sutra प.8.4.67: नोदात्तस्वरितोदयमगार्ग्यकाश्यपगालवानाम्
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.67"
SUTRA_TEXT = "नोदात्तस्वरितोदयमगार्ग्यकाश्यपगालवानाम्"
SUTRA_DESC = "final transformations — continued"


class Sutra8467:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.67: अग्निः'),
		('रामः', '', 'प.8.4.67: रामः'),
		('सीता', '', 'प.8.4.67: सीता'),
	]

