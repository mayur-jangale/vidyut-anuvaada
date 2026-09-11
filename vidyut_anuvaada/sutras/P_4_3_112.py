# Sutra प.4.3.112: तेनैकदिक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tenEkadik

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.112"
SUTRA_TEXT = "तेनैकदिक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tenEkadik"


class Sutra43112:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.112: अग्निः'),
		('रामः', '', 'प.4.3.112: रामः'),
		('सीता', '', 'प.4.3.112: सीता'),
	]

