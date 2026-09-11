# Sutra प.1.4.3: यू स्त्र्याख्यौ नदी
# (Samjna (technical definitions)) — yU stryAKyO nadI

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.3"
SUTRA_TEXT = "यू स्त्र्याख्यौ नदी"
SUTRA_DESC = "(Samjna (technical definitions)) — yU stryAKyO nadI"


class Sutra143:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_3
		return apply_1_4_3(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-nadI:अग्निः'),
		('रामः', '', 'not-nadI:रामः'),
		('सीता', '', 'not-nadI:सीता'),
	]

