# Sutra प.6.2.174: ह्रस्वान्तेऽन्त्यात् पूर्वम्
# (Sandhi (euphonic combination)) — hrasvAnte'ntyAt pUrvam

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.174"
SUTRA_TEXT = "ह्रस्वान्तेऽन्त्यात् पूर्वम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — hrasvAnte'ntyAt pUrvam"


class Sutra62174:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.174: अग्निः'),
		('रामः', '', 'प.6.2.174: रामः'),
		('सीता', '', 'प.6.2.174: सीता'),
	]

