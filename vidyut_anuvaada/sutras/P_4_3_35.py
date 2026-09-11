# Sutra प.4.3.35: स्थानान्तगोशालखरशालाच्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — sTAnAntagoSAlaKaraSAlAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.35"
SUTRA_TEXT = "स्थानान्तगोशालखरशालाच्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — sTAnAntagoSAlaKaraSAlAcca"


class Sutra4335:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.35: अग्निः'),
		('रामः', '', 'प.4.3.35: रामः'),
		('सीता', '', 'प.4.3.35: सीता'),
	]

