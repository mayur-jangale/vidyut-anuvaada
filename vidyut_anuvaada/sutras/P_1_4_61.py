# Sutra प.1.4.61: ऊर्यादिच्विडाचश्च
# (Samjna (technical definitions)) — UryAdicviqAcaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.61"
SUTRA_TEXT = "ऊर्यादिच्विडाचश्च"
SUTRA_DESC = "(Samjna (technical definitions)) — UryAdicviqAcaSca"


class Sutra1461:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_61
		return apply_1_4_61(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-UryAdi:अग्निः'),
		('रामः', '', 'not-UryAdi:रामः'),
		('सीता', '', 'not-UryAdi:सीता'),
	]

