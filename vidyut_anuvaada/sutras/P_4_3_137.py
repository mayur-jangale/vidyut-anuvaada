# Sutra प.4.3.137: कोपधाच्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kopaDAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.137"
SUTRA_TEXT = "कोपधाच्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kopaDAcca"


class Sutra43137:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.137: अग्निः'),
		('रामः', '', 'प.4.3.137: रामः'),
		('सीता', '', 'प.4.3.137: सीता'),
	]

