# Sutra प.1.1.18: ऊँ
# Ū~ — specific treatment of ऊ

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.18"
SUTRA_TEXT = "ऊँ"
SUTRA_DESC = "Ū~ — specific treatment of ऊ"


class Sutra1118:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_18
		return apply_1_1_18(word, pos)

	EXAMPLES = [
		('ऊ', '', 'ū-long:ऊ'),
		('अग्नि', '', 'non-ū:अग्नि'),
	]

