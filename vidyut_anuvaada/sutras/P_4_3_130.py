# Sutra प.4.3.130: न दण्डमाणवान्तेवासिषु
# (Sup-sthāna (nominal endings) and kṛt-affixes) — na daRqamARavAntevAsizu

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.130"
SUTRA_TEXT = "न दण्डमाणवान्तेवासिषु"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — na daRqamARavAntevAsizu"


class Sutra43130:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.130: अग्निः'),
		('रामः', '', 'प.4.3.130: रामः'),
		('सीता', '', 'प.4.3.130: सीता'),
	]

