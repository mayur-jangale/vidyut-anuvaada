# Sutra प.4.3.109: छगलिनो ढिनुक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — Cagalino Qinuk

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.109"
SUTRA_TEXT = "छगलिनो ढिनुक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — Cagalino Qinuk"


class Sutra43109:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.109: अग्निः'),
		('रामः', '', 'प.4.3.109: रामः'),
		('सीता', '', 'प.4.3.109: सीता'),
	]

