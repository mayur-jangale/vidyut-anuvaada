# Sutra प.6.2.111: उत्तरपदादिः
# (Sandhi (euphonic combination)) — uttarapadAdiH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.111"
SUTRA_TEXT = "उत्तरपदादिः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — uttarapadAdiH"


class Sutra62111:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.111: अग्निः'),
		('रामः', '', 'प.6.2.111: रामः'),
		('सीता', '', 'प.6.2.111: सीता'),
	]

