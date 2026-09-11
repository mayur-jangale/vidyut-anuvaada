# Sutra प.1.2.55: योगप्रमाणे च तदभावेऽदर्शनं स्यात्
# (Samjna (technical definitions)) — yogapramARe ca tadaBAve'darSanaM syAt

from P_1_2 import apply_1_2_55

SUTRA_CODE = "प.1.2.55"
SUTRA_TEXT = "योगप्रमाणे च तदभावेऽदर्शनं स्यात्"
SUTRA_DESC = "(Samjna (technical definitions)) — yogapramARe ca tadaBAve'darSanaM syAt"


class Sutra1255:
	def apply(self, word, pos):
		return apply_1_2_55(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'yoga-pramāṇa:अग्निः;absence=non-occurrence'),
		('रामः', '', 'yoga-pramāṇa:रामः;absence=non-occurrence'),
		('सीता', '', 'yoga-pramāṇa:सीता;absence=non-occurrence'),
	]

