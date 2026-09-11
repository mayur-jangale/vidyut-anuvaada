# Sutra प.1.2.36: विभाषा छन्दसि
# (Samjna (technical definitions)) — viBAzA Candasi

from P_1_2 import apply_1_2_36

SUTRA_CODE = "प.1.2.36"
SUTRA_TEXT = "विभाषा छन्दसि"
SUTRA_DESC = "(Samjna (technical definitions)) — viBAzA Candasi"


class Sutra1236:
	def apply(self, word, pos):
		return apply_1_2_36(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-chandasi:अग्निः'),
		('रामः', '', 'non-chandasi:रामः'),
		('सीता', '', 'non-chandasi:सीता'),
	]

