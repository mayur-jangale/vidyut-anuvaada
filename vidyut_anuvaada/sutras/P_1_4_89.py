# Sutra प.1.4.89: आङ् मर्यादावचने
# (Samjna (technical definitions)) — AN maryAdAvacane

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.89"
SUTRA_TEXT = "आङ् मर्यादावचने"
SUTRA_DESC = "(Samjna (technical definitions)) — AN maryAdAvacane"


class Sutra1489:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_89
		return apply_1_4_89(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-AN-maryAdA:अग्निः'),
		('रामः', '', 'not-AN-maryAdA:रामः'),
		('सीता', '', 'not-AN-maryAdA:सीता'),
	]

