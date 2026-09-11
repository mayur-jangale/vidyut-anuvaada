# Sutra प.1.4.21: बहुषु बहुवचनम्
# (Samjna (technical definitions)) — bahuzu bahuvacanam

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.21"
SUTRA_TEXT = "बहुषु बहुवचनम्"
SUTRA_DESC = "(Samjna (technical definitions)) — bahuzu bahuvacanam"


class Sutra1421:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_21
		return apply_1_4_21(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-bahuvacana:अग्निः'),
		('रामः', '', 'not-bahuvacana:रामः'),
		('सीता', '', 'not-bahuvacana:सीता'),
	]

