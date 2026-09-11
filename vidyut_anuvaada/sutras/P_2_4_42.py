# Sutra प.2.4.42: हनो वध लिङि
# (Samasa (compound formation)) — hano vaDa liNi

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.42"
SUTRA_TEXT = "हनो वध लिङि"
SUTRA_DESC = "(Samasa (compound formation)) — hano vaDa liNi"


class Sutra2442:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

