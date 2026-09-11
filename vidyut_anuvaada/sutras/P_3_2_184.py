# Sutra प.3.2.184: अर्तिलूधूसूखनसहचर इत्रः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — artilUDUsUKanasahacara itraH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.184"
SUTRA_TEXT = "अर्तिलूधूसूखनसहचर इत्रः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — artilUDUsUKanasahacara itraH"


class Sutra32184:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

