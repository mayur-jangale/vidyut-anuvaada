# Sutra प.3.4.13: ईश्वरे तोसुन्कसुनौ
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ISvare tosunkasunO

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.13"
SUTRA_TEXT = "ईश्वरे तोसुन्कसुनौ"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ISvare tosunkasunO"


class Sutra3413:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

