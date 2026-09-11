# Sutra प.6.2.152: सप्तम्याः पुण्यम्
# (Sandhi (euphonic combination)) — saptamyAH puRyam

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.152"
SUTRA_TEXT = "सप्तम्याः पुण्यम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — saptamyAH puRyam"


class Sutra62152:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.152: अग्निः'),
		('रामः', '', 'प.6.2.152: रामः'),
		('सीता', '', 'प.6.2.152: सीता'),
	]

