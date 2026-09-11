# Sutra प.4.3.114: उरसो यच्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — uraso yacca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.114"
SUTRA_TEXT = "उरसो यच्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — uraso yacca"


class Sutra43114:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.114: अग्निः'),
		('रामः', '', 'प.4.3.114: रामः'),
		('सीता', '', 'प.4.3.114: सीता'),
	]

