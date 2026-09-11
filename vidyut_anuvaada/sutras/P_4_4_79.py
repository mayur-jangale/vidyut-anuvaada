# Sutra प.4.4.79: एकधुराल्लुक् च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — ekaDurAlluk ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.79"
SUTRA_TEXT = "एकधुराल्लुक् च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — ekaDurAlluk ca"


class Sutra4479:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.79: अग्निः'),
		('रामः', '', 'प.4.4.79: रामः'),
		('सीता', '', 'प.4.4.79: सीता'),
	]

