# Sutra प.1.2.27: ऊकालोऽज्झ्रस्वदीर्घप्लुतः
# (Samjna (technical definitions)) — UkAlo'jJrasvadIrGaplutaH

from P_1_2 import apply_1_2_27

SUTRA_CODE = "प.1.2.27"
SUTRA_TEXT = "ऊकालोऽज्झ्रस्वदीर्घप्लुतः"
SUTRA_DESC = "(Samjna (technical definitions)) — UkAlo'jJrasvadIrGaplutaH"


class Sutra1227:
	def apply(self, word, pos):
		return apply_1_2_27(word, pos)

	EXAMPLES = [
	('अग्निः', '', "ūkāla:{'ह्रस्व': 1, 'दीर्घ': 0, 'प्लुत': 0}"),
		('रामः', '', "ūkāla:{'ह्रस्व': 0, 'दीर्घ': 0, 'प्लुत': 0}"),
		('सीता', '', "ūkāla:{'ह्रस्व': 0, 'दीर्घ': 0, 'प्लुत': 0}"),
	]

