# Sutra प.8.1.30: निपातैर्यद्यदिहन्तकुविन्नेच्चेच्चण्कच्चिद्यत्रयुक्तम्
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.30"
SUTRA_TEXT = "निपातैर्यद्यदिहन्तकुविन्नेच्चेच्चण्कच्चिद्यत्रयुक्तम्"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8130:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.30: अग्निः'),
		('रामः', '', 'प.8.1.30: रामः'),
		('सीता', '', 'प.8.1.30: सीता'),
	]

