# Sutra प.1.4.99: लः परस्मैपदम्
# (Samjna (technical definitions)) — laH parasmEpadam

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.99"
SUTRA_TEXT = "लः परस्मैपदम्"
SUTRA_DESC = "(Samjna (technical definitions)) — laH parasmEpadam"


class Sutra1499:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_99
		return apply_1_4_99(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-parasmaipada:अग्निः'),
		('रामः', '', 'not-parasmaipada:रामः'),
		('सीता', '', 'not-parasmaipada:सीता'),
	]

