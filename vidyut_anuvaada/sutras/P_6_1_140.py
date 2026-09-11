# Sutra प.6.1.140: किरतौ लवने
# sandhi-sūtra प.6.1.140

from P_6_1 import apply_6_1_140

SUTRA_CODE = "प.6.1.140"
SUTRA_TEXT = "किरतौ लवने"
SUTRA_DESC = "sandhi-sūtra प.6.1.140"


class Sutra61140:
	def apply(self, word, pos):
		return apply_6_1_140(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.140:no-visarga;अग्निः'),
		('रामः', '', '6.1.140:no-visarga;रामः'),
		('सीता', '', '6.1.140:no-visarga;सीता'),
	]
