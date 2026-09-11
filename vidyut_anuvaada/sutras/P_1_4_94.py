# Sutra प.1.4.94: सुः पूजायाम्
# (Samjna (technical definitions)) — suH pUjAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.94"
SUTRA_TEXT = "सुः पूजायाम्"
SUTRA_DESC = "(Samjna (technical definitions)) — suH pUjAyAm"


class Sutra1494:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_94
		return apply_1_4_94(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-su-pUjA:अग्निः'),
		('रामः', '', 'not-su-pUjA:रामः'),
		('सीता', '', 'not-su-pUjA:सीता'),
	]

