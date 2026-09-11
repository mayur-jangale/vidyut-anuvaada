# Sutra प.8.2.8: न ङिसम्बुद्ध्योः
# saṃhitāyāṃ padāntasya — final element in saṃhitā

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.8"
SUTRA_TEXT = "न ङिसम्बुद्ध्योः"
SUTRA_DESC = "saṃhitāyāṃ padāntasya — final element in saṃhitā"


class Sutra828:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.8: अग्निः'),
		('रामः', '', 'प.8.2.8: रामः'),
		('सीता', '', 'प.8.2.8: सीता'),
	]

