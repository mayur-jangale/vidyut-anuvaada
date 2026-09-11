# Sutra प.1.2.57: कालोपसर्जने च तुल्यम्
# (Samjna (technical definitions)) — kAlopasarjane ca tulyam

from P_1_2 import apply_1_2_57

SUTRA_CODE = "प.1.2.57"
SUTRA_TEXT = "कालोपसर्जने च तुल्यम्"
SUTRA_DESC = "(Samjna (technical definitions)) — kAlopasarjane ca tulyam"


class Sutra1257:
	def apply(self, word, pos):
		return apply_1_2_57(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-kāla:अग्निः'),
		('रामः', '', 'non-kāla:रामः'),
		('सीता', '', 'non-kāla:सीता'),
	]

