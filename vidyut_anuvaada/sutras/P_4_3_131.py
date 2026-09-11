# Sutra प.4.3.131: रैवतिकादिभ्यश्छः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — rEvatikAdiByaSCaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.131"
SUTRA_TEXT = "रैवतिकादिभ्यश्छः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — rEvatikAdiByaSCaH"


class Sutra43131:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.131: अग्निः'),
		('रामः', '', 'प.4.3.131: रामः'),
		('सीता', '', 'प.4.3.131: सीता'),
	]

