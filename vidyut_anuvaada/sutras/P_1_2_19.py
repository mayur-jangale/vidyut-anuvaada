# Sutra प.1.2.19: निष्ठा शीङ्स्विदिमिदिक्ष्विदिधृषः
# (Samjna (technical definitions)) — nizWA SINsvidimidikzvidiDfzaH

from P_1_2 import apply_1_2_19

SUTRA_CODE = "प.1.2.19"
SUTRA_TEXT = "निष्ठा शीङ्स्विदिमिदिक्ष्विदिधृषः"
SUTRA_DESC = "(Samjna (technical definitions)) — nizWA SINsvidimidikzvidiDfzaH"


class Sutra1219:
	def apply(self, word, pos):
		return apply_1_2_19(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-ṣīṅsvidi:अग्निः'),
		('रामः', '', 'non-ṣīṅsvidi:रामः'),
		('सीता', '', 'non-ṣīṅsvidi:सीता'),
	]

