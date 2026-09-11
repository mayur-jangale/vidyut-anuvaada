# Sutra प.6.2.132: पुत्रः पुंभ्यः
# (Sandhi (euphonic combination)) — putraH puMByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.132"
SUTRA_TEXT = "पुत्रः पुंभ्यः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — putraH puMByaH"


class Sutra62132:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.132: अग्निः'),
		('रामः', '', 'प.6.2.132: रामः'),
		('सीता', '', 'प.6.2.132: सीता'),
	]

