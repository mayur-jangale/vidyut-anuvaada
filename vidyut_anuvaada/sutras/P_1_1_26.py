# Sutra प.1.1.26: क्तक्तवतू निष्ठा
# (Samjna (technical definitions)) — ktaktavatU nizWA

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.26"
SUTRA_TEXT = "क्तक्तवतू निष्ठा"
SUTRA_DESC = "(Samjna (technical definitions)) — ktaktavatU nizWA"


class Sutra1126:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_26
		return apply_1_1_26(word, pos)

	EXAMPLES = [
		('गत', '', 'non-niṣṭhā:गत'),
		('गतवत्', '', 'non-niṣṭhā:गतवत्'),
		('पचति', '', 'non-niṣṭhā:पचति'),
	]

