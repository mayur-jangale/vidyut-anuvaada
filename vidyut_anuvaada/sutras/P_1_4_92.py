# Sutra प.1.4.92: प्रतिः प्रतिनिधिप्रतिदानयोः
# (Samjna (technical definitions)) — pratiH pratiniDipratidAnayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.92"
SUTRA_TEXT = "प्रतिः प्रतिनिधिप्रतिदानयोः"
SUTRA_DESC = "(Samjna (technical definitions)) — pratiH pratiniDipratidAnayoH"


class Sutra1492:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_92
		return apply_1_4_92(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-prati-substitute:अग्निः'),
		('रामः', '', 'not-prati-substitute:रामः'),
		('सीता', '', 'not-prati-substitute:सीता'),
	]

