# Sutra प.3.1.68: कर्तरि शप्
# ṭeḥ śeṣaḥ — after the vikaraṇa ट्, the remaining portion is treated specially

from P_3_1 import apply_3_1_68

SUTRA_CODE = "प.3.1.68"
SUTRA_TEXT = "कर्तरि शप्"
SUTRA_DESC = "ṭeḥ śeṣaḥ — after the vikaraṇa ट्, the remaining portion is treated specially"


class Sutra3168:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_68(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.68:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.68:root=रामः;pos='),
		('सीता', '', 'प.3.1.68:root=सीता;pos='),
	]

