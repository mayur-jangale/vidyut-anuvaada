# Sutra प.1.1.59: द्विर्वचनेऽचि
# (Samjna (technical definitions)) — dvirvacane'ci

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.59"
SUTRA_TEXT = "द्विर्वचनेऽचि"
SUTRA_DESC = "(Samjna (technical definitions)) — dvirvacane'ci"


class Sutra1159:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_59
		return apply_1_1_59(word, pos)

	EXAMPLES = [
		('द्विर्वचने', '', "प.1.1.59:dvirvacane'ci;input=द्विर्वचने"),
		('अग्नि', '', "प.1.1.59:dvirvacane'ci;input=अग्नि"),
	]

