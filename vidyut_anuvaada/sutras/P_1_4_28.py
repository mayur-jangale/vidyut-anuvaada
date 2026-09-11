# Sutra प.1.4.28: अन्तर्द्धौ येनादर्शनमिच्छति
# (Samjna (technical definitions)) — antardDO yenAdarSanamicCati

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.28"
SUTRA_TEXT = "अन्तर्द्धौ येनादर्शनमिच्छति"
SUTRA_DESC = "(Samjna (technical definitions)) — antardDO yenAdarSanamicCati"


class Sutra1428:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_28
		return apply_1_4_28(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-antarddhi-apadana:अग्निः'),
		('रामः', '', 'not-antarddhi-apadana:रामः'),
		('सीता', '', 'not-antarddhi-apadana:सीता'),
	]

