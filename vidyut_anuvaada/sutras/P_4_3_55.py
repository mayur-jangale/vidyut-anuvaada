# Sutra प.4.3.55: शरीरावयवाच्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SarIrAvayavAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.55"
SUTRA_TEXT = "शरीरावयवाच्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SarIrAvayavAcca"


class Sutra4355:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.55: अग्निः'),
		('रामः', '', 'प.4.3.55: रामः'),
		('सीता', '', 'प.4.3.55: सीता'),
	]

