# Sutra प.1.2.45: अर्थवदधातुरप्रत्ययः प्रातिपदिकम्
# (Samjna (technical definitions)) — arTavadaDAturapratyayaH prAtipadikam

from P_1_2 import apply_1_2_45

SUTRA_CODE = "प.1.2.45"
SUTRA_TEXT = "अर्थवदधातुरप्रत्ययः प्रातिपदिकम्"
SUTRA_DESC = "(Samjna (technical definitions)) — arTavadaDAturapratyayaH prAtipadikam"


class Sutra1245:
	def apply(self, word, pos):
		return apply_1_2_45(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-prātipadika:अग्निः'),
		('रामः', '', 'non-prātipadika:रामः'),
		('सीता', '', 'non-prātipadika:सीता'),
	]

