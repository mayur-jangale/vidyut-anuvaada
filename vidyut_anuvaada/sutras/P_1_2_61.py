# Sutra प.1.2.61: छन्दसि पुनर्वस्वोरेकवचनम्
# (Samjna (technical definitions)) — Candasi punarvasvorekavacanam

from P_1_2 import apply_1_2_61

SUTRA_CODE = "प.1.2.61"
SUTRA_TEXT = "छन्दसि पुनर्वस्वोरेकवचनम्"
SUTRA_DESC = "(Samjna (technical definitions)) — Candasi punarvasvorekavacanam"


class Sutra1261:
	def apply(self, word, pos):
		return apply_1_2_61(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-chandasi:अग्निः'),
		('रामः', '', 'non-chandasi:रामः'),
		('सीता', '', 'non-chandasi:सीता'),
	]

