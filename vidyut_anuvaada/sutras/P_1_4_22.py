# Sutra प.1.4.22: द्व्येकयोर्द्विवचनैकवचने
# bahulaṃ śasvat — most occurrences follow the default unless context forces otherwise

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.22"
SUTRA_TEXT = "द्व्येकयोर्द्विवचनैकवचने"
SUTRA_DESC = "bahulaṃ śasvat — most occurrences follow the default unless context forces otherwise"


class Sutra1422:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_22
		return apply_1_4_22(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-dva-eka:अग्निः'),
		('रामः', '', 'not-dva-eka:रामः'),
		('सीता', '', 'not-dva-eka:सीता'),
	]

