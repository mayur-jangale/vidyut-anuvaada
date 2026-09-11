# Sutra प.1.1.20: दाधा घ्वदाप्
# dāghvadāp — roots of the form dāgh, vād, etc. follow special patterns

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.20"
SUTRA_TEXT = "दाधा घ्वदाप्"
SUTRA_DESC = "dāghvadāp — roots of the form dāgh, vād, etc. follow special patterns"


class Sutra1120:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_20
		return apply_1_1_20(word, pos)

	EXAMPLES = [
		('देवता', '', 'dāgh-derivative:देवता'),
		('अग्नि', '', 'non-dāgh:अग्नि'),
	]

