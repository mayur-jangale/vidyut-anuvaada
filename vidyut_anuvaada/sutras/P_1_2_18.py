# Sutra प.1.2.18: न क्त्वा सेट्
# (Samjna (technical definitions)) — na ktvA sew

from P_1_2 import apply_1_2_18

SUTRA_CODE = "प.1.2.18"
SUTRA_TEXT = "न क्त्वा सेट्"
SUTRA_DESC = "(Samjna (technical definitions)) — na ktvA sew"


class Sutra1218:
	def apply(self, word, pos):
		return apply_1_2_18(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-seṭ:अग्निः'),
		('रामः', '', 'non-seṭ:रामः'),
		('सीता', '', 'non-seṭ:सीता'),
	]

