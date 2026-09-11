# Sutra प.4.3.166: लुप् च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — lup ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.166"
SUTRA_TEXT = "लुप् च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — lup ca"


class Sutra43166:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.166: अग्निः'),
		('रामः', '', 'प.4.3.166: रामः'),
		('सीता', '', 'प.4.3.166: सीता'),
	]

