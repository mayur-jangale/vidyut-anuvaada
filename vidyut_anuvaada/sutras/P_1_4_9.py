# Sutra प.1.4.9: षष्ठीयुक्तश्छन्दसि वा
# (Samjna (technical definitions)) — zazWIyuktaSCandasi vA

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.9"
SUTRA_TEXT = "षष्ठीयुक्तश्छन्दसि वा"
SUTRA_DESC = "(Samjna (technical definitions)) — zazWIyuktaSCandasi vA"


class Sutra149:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_9
		return apply_1_4_9(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'no-opt:अग्निः'),
		('रामः', '', 'no-opt:रामः'),
		('सीता', '', 'no-opt:सीता'),
	]

