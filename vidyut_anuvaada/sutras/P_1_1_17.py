# Sutra प.1.1.17: उञः
# uyaḥ — specific suffix rules for उय

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.17"
SUTRA_TEXT = "उञः"
SUTRA_DESC = "uyaḥ — specific suffix rules for उय"


class Sutra1117:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_17
		return apply_1_1_17(word, pos)

	EXAMPLES = [
		('उय', '', 'uya-affix:उय'),
		('अग्नि', '', 'non-uya:अग्नि'),
	]

