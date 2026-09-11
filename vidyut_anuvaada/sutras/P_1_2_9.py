# Sutra प.1.2.9: इको झल्
# (Samjna (technical definitions)) — iko Jal

from P_1_2 import apply_1_2_9

SUTRA_CODE = "प.1.2.9"
SUTRA_TEXT = "इको झल्"
SUTRA_DESC = "(Samjna (technical definitions)) — iko Jal"


class Sutra129:
	def apply(self, word, pos):
		return apply_1_2_9(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'iko-jhal:pairs=none'),
		('रामः', '', 'iko-jhal:pairs=none'),
		('सीता', '', 'iko-jhal:pairs=none'),
	]

