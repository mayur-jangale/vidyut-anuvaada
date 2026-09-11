# Sutra प.1.4.84: अनुर्लक्षणे
# (Samjna (technical definitions)) — anurlakzaRe

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.84"
SUTRA_TEXT = "अनुर्लक्षणे"
SUTRA_DESC = "(Samjna (technical definitions)) — anurlakzaRe"


class Sutra1484:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_84
		return apply_1_4_84(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-anu-lakshaRa:अग्निः'),
		('रामः', '', 'not-anu-lakshaRa:रामः'),
		('सीता', '', 'not-anu-lakshaRa:सीता'),
	]

