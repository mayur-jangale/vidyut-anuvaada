# Sutra प.3.2.25: हरतेर्दृतिनाथयोः पशौ
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — haraterdftinATayoH paSO

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.25"
SUTRA_TEXT = "हरतेर्दृतिनाथयोः पशौ"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — haraterdftinATayoH paSO"


class Sutra3225:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

