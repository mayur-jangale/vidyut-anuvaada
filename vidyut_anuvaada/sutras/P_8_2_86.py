# Sutra प.8.2.86: गुरोरनृतोऽनन्त्यस्याप्येकैकस्य प्राचाम्
# (Final transformations (tripāḍī)) — guroranfto'nantyasyApyekEkasya prAcAm

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.86"
SUTRA_TEXT = "गुरोरनृतोऽनन्त्यस्याप्येकैकस्य प्राचाम्"
SUTRA_DESC = "(Final transformations (tripāḍī)) — guroranfto'nantyasyApyekEkasya prAcAm"


class Sutra8286:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.86: अग्निः'),
		('रामः', '', 'प.8.2.86: रामः'),
		('सीता', '', 'प.8.2.86: सीता'),
	]

