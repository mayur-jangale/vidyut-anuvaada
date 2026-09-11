# Sutra प.1.4.93: अधिपरी अनर्थकौ
# (Samjna (technical definitions)) — aDiparI anarTakO

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.93"
SUTRA_TEXT = "अधिपरी अनर्थकौ"
SUTRA_DESC = "(Samjna (technical definitions)) — aDiparI anarTakO"


class Sutra1493:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_93
		return apply_1_4_93(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-adhi-parI:अग्निः'),
		('रामः', '', 'not-adhi-parI:रामः'),
		('सीता', '', 'not-adhi-parI:सीता'),
	]

