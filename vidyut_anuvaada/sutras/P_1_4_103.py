# Sutra प.1.4.103: सुपः
# (Samjna (technical definitions)) — supaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.103"
SUTRA_TEXT = "सुपः"
SUTRA_DESC = "(Samjna (technical definitions)) — supaH"


class Sutra14103:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_103
		return apply_1_4_103(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-sup:अग्निः'),
		('रामः', '', 'not-sup:रामः'),
		('सीता', '', 'not-sup:सीता'),
	]

