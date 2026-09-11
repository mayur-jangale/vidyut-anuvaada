# Sutra प.1.4.7: शेषो घ्यसखि
# (Samjna (technical definitions)) — Sezo GyasaKi

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.7"
SUTRA_TEXT = "शेषो घ्यसखि"
SUTRA_DESC = "(Samjna (technical definitions)) — Sezo GyasaKi"


class Sutra147:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_7
		return apply_1_4_7(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-genitive:अग्निः'),
		('रामः', '', 'not-genitive:रामः'),
		('सीता', '', 'not-genitive:सीता'),
	]

