# Sutra प.3.1.28: गुपूधूपविच्छिपणिपनिभ्य आयः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — gupUDUpavicCipaRipaniBya AyaH

from P_3_1 import apply_3_1_28

SUTRA_CODE = "प.3.1.28"
SUTRA_TEXT = "गुपूधूपविच्छिपणिपनिभ्य आयः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — gupUDUpavicCipaRipaniBya AyaH"


class Sutra3128:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_28(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.28:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.28:root=रामः;pos='),
		('सीता', '', 'प.3.1.28:root=सीता;pos='),
	]

