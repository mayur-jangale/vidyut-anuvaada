# Sutra प.1.4.107: अस्मद्युत्तमः
# (Samjna (technical definitions)) — asmadyuttamaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.107"
SUTRA_TEXT = "अस्मद्युत्तमः"
SUTRA_DESC = "(Samjna (technical definitions)) — asmadyuttamaH"


class Sutra14107:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_107
		return apply_1_4_107(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-asmad-uttama:अग्निः'),
		('रामः', '', 'not-asmad-uttama:रामः'),
		('सीता', '', 'not-asmad-uttama:सीता'),
	]

