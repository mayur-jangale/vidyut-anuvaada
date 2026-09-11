# Sutra प.1.1.13: शे
# Se — the suffix सी is used in specific contexts

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.13"
SUTRA_TEXT = "शे"
SUTRA_DESC = "Se — the suffix सी is used in specific contexts"


class Sutra1113:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_13
		return apply_1_1_13(word, pos)

	EXAMPLES = [
		('सी', '', 'śe-affix:सी'),
		('अग्नि', '', 'no-śe:अग्नि'),
	]

