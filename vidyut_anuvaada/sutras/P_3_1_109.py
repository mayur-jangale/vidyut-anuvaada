# Sutra प.3.1.109: एतिस्तुशास्वृदृजुषः क्यप्
# ṅitvasya — repeated pattern

from P_3_1 import apply_3_1_109

SUTRA_CODE = "प.3.1.109"
SUTRA_TEXT = "एतिस्तुशास्वृदृजुषः क्यप्"
SUTRA_DESC = "ṅitvasya — repeated pattern"


class Sutra31109:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_109(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.109:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.109:root=रामः;pos='),
		('सीता', '', 'प.3.1.109:root=सीता;pos='),
	]

