# Sutra प.1.4.95: अतिरतिक्रमणे च
# (Samjna (technical definitions)) — atiratikramaRe ca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.95"
SUTRA_TEXT = "अतिरतिक्रमणे च"
SUTRA_DESC = "(Samjna (technical definitions)) — atiratikramaRe ca"


class Sutra1495:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_95
		return apply_1_4_95(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-ati-atikramaRa:अग्निः'),
		('रामः', '', 'not-ati-atikramaRa:रामः'),
		('सीता', '', 'not-ati-atikramaRa:सीता'),
	]

