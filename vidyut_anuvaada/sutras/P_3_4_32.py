# Sutra प.3.4.32: वर्षप्रमाण ऊलोपश्चास्यान्यतरस्याम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — varzapramARa UlopaScAsyAnyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.32"
SUTRA_TEXT = "वर्षप्रमाण ऊलोपश्चास्यान्यतरस्याम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — varzapramARa UlopaScAsyAnyatarasyAm"


class Sutra3432:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

