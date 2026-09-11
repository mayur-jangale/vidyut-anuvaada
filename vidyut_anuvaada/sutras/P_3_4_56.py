# Sutra प.3.4.56: विशिपतिपदिस्कन्दां व्याप्यमानासेव्यमानयोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — viSipatipadiskandAM vyApyamAnAsevyamAnayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.56"
SUTRA_TEXT = "विशिपतिपदिस्कन्दां व्याप्यमानासेव्यमानयोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — viSipatipadiskandAM vyApyamAnAsevyamAnayoH"


class Sutra3456:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

