# Sutra प.1.2.56: प्रधानप्रत्ययार्थवचनमर्थस्यान्यप्रमाणत्वात्
# (Samjna (technical definitions)) — praDAnapratyayArTavacanamarTasyAnyapramARatvAt

from P_1_2 import apply_1_2_56

SUTRA_CODE = "प.1.2.56"
SUTRA_TEXT = "प्रधानप्रत्ययार्थवचनमर्थस्यान्यप्रमाणत्वात्"
SUTRA_DESC = "(Samjna (technical definitions)) — praDAnapratyayArTavacanamarTasyAnyapramARatvAt"


class Sutra1256:
	def apply(self, word, pos):
		return apply_1_2_56(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'pradhāna-pratyaya:अग्निः;artha-vacana'),
		('रामः', '', 'pradhāna-pratyaya:रामः;artha-vacana'),
		('सीता', '', 'pradhāna-pratyaya:सीता;artha-vacana'),
	]

