# Sutra प.1.2.63: तिष्यपुनर्वस्वोर्नक्षत्रद्वन्द्वे बहुवचनस्य द्विवचनं नित्यम्
# (Samjna (technical definitions)) — tizyapunarvasvornakzatradvandve bahuvacanasya dvivacanaM nityam

from P_1_2 import apply_1_2_63

SUTRA_CODE = "प.1.2.63"
SUTRA_TEXT = "तिष्यपुनर्वस्वोर्नक्षत्रद्वन्द्वे बहुवचनस्य द्विवचनं नित्यम्"
SUTRA_DESC = "(Samjna (technical definitions)) — tizyapunarvasvornakzatradvandve bahuvacanasya dvivacanaM nityam"


class Sutra1263:
	def apply(self, word, pos):
		return apply_1_2_63(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-dvandva:अग्निः'),
		('रामः', '', 'non-dvandva:रामः'),
		('सीता', '', 'non-dvandva:सीता'),
	]

