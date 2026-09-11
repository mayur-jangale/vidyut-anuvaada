# Sutra प.6.2.166: व्यवायिनोऽन्तरम्
# (Sandhi (euphonic combination)) — vyavAyino'ntaram

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.166"
SUTRA_TEXT = "व्यवायिनोऽन्तरम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — vyavAyino'ntaram"


class Sutra62166:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.166: अग्निः'),
		('रामः', '', 'प.6.2.166: रामः'),
		('सीता', '', 'प.6.2.166: सीता'),
	]

