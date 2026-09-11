# Sutra प.1.4.71: तिरोऽन्तर्द्धौ
# śeṣaḥ — remaining rules apply by default

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.71"
SUTRA_TEXT = "तिरोऽन्तर्द्धौ"
SUTRA_DESC = "śeṣaḥ — remaining rules apply by default"


class Sutra1471:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_71
		return apply_1_4_71(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-tiras:अग्निः'),
		('रामः', '', 'not-tiras:रामः'),
		('सीता', '', 'not-tiras:सीता'),
	]

