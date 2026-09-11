# Sutra प.6.2.163: संख्यायाः स्तनः
# (Sandhi (euphonic combination)) — saMKyAyAH stanaH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.163"
SUTRA_TEXT = "संख्यायाः स्तनः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — saMKyAyAH stanaH"


class Sutra62163:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.163: अग्निः'),
		('रामः', '', 'प.6.2.163: रामः'),
		('सीता', '', 'प.6.2.163: सीता'),
	]

