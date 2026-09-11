# Sutra प.3.2.129: ताच्छील्यवयोवचनशक्तिषु चानश्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — tAcCIlyavayovacanaSaktizu cAnaS

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.129"
SUTRA_TEXT = "ताच्छील्यवयोवचनशक्तिषु चानश्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — tAcCIlyavayovacanaSaktizu cAnaS"


class Sutra32129:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

