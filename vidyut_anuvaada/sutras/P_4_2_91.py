# Sutra प.4.2.91: नडादीनां कुक् च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — naqAdInAM kuk ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.91"
SUTRA_TEXT = "नडादीनां कुक् च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — naqAdInAM kuk ca"


class Sutra4291:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.91: अग्निः'),
		('रामः', '', 'प.4.2.91: रामः'),
		('सीता', '', 'प.4.2.91: सीता'),
	]

