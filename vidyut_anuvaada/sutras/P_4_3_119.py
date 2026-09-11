# Sutra प.4.3.119: क्षुद्राभ्रमरवटरपादपादञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kzudrABramaravawarapAdapAdaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.119"
SUTRA_TEXT = "क्षुद्राभ्रमरवटरपादपादञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kzudrABramaravawarapAdapAdaY"


class Sutra43119:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.119: अग्निः'),
		('रामः', '', 'प.4.3.119: रामः'),
		('सीता', '', 'प.4.3.119: सीता'),
	]

