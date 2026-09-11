# Sutra प.4.2.59: तदधीते तद्वेद
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tadaDIte tadveda

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.59"
SUTRA_TEXT = "तदधीते तद्वेद"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tadaDIte tadveda"


class Sutra4259:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.59: अग्निः'),
		('रामः', '', 'प.4.2.59: रामः'),
		('सीता', '', 'प.4.2.59: सीता'),
	]

