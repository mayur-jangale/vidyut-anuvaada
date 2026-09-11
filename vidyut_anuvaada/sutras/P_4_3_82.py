# Sutra प.4.3.82: मयट् च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — mayaw ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.82"
SUTRA_TEXT = "मयट् च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — mayaw ca"


class Sutra4382:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.82: अग्निः'),
		('रामः', '', 'प.4.3.82: रामः'),
		('सीता', '', 'प.4.3.82: सीता'),
	]

