# Sutra प.1.4.60: गतिश्च
# (Samjna (technical definitions)) — gatiSca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.60"
SUTRA_TEXT = "गतिश्च"
SUTRA_DESC = "(Samjna (technical definitions)) — gatiSca"


class Sutra1460:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_60
		return apply_1_4_60(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-gati-upasarga:अग्निः'),
		('रामः', '', 'not-gati-upasarga:रामः'),
		('सीता', '', 'not-gati-upasarga:सीता'),
	]

