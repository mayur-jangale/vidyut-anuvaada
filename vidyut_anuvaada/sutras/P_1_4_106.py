# Sutra प.1.4.106: प्रहासे च मन्योपपदे मन्यतेरुत्तम एकवच्च
# (Samjna (technical definitions)) — prahAse ca manyopapade manyateruttama ekavacca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.106"
SUTRA_TEXT = "प्रहासे च मन्योपपदे मन्यतेरुत्तम एकवच्च"
SUTRA_DESC = "(Samjna (technical definitions)) — prahAse ca manyopapade manyateruttama ekavacca"


class Sutra14106:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_106
		return apply_1_4_106(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-uttama-manyA:अग्निः'),
		('रामः', '', 'not-uttama-manyA:रामः'),
		('सीता', '', 'not-uttama-manyA:सीता'),
	]

