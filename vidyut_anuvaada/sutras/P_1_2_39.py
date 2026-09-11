# Sutra प.1.2.39: स्वरितात् संहितायामनुदात्तानाम्
# (Samjna (technical definitions)) — svaritAt saMhitAyAmanudAttAnAm

from P_1_2 import apply_1_2_39

SUTRA_CODE = "प.1.2.39"
SUTRA_TEXT = "स्वरितात् संहितायामनुदात्तानाम्"
SUTRA_DESC = "(Samjna (technical definitions)) — svaritAt saMhitAyAmanudAttAnAm"


class Sutra1239:
	def apply(self, word, pos):
		return apply_1_2_39(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-saṃhitā:अग्निः'),
		('रामः', '', 'non-saṃhitā:रामः'),
		('सीता', '', 'non-saṃhitā:सीता'),
	]

