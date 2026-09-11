# Sutra प.1.2.4: सार्वधातुकमपित्
# (Samjna (technical definitions)) — sArvaDAtukamapit

from P_1_2 import apply_1_2_4

SUTRA_CODE = "प.1.2.4"
SUTRA_TEXT = "सार्वधातुकमपित्"
SUTRA_DESC = "(Samjna (technical definitions)) — sArvaDAtukamapit"


class Sutra124:
	def apply(self, word, pos):
		return apply_1_2_4(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-sārvadhātuka:अग्निः'),
		('रामः', '', 'non-sārvadhātuka:रामः'),
		('सीता', '', 'non-sārvadhātuka:सीता'),
	]

