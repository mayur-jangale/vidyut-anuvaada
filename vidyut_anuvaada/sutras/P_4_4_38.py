# Sutra प.4.4.38: आक्रन्दाट्ठञ्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — AkrandAwWaYca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.38"
SUTRA_TEXT = "आक्रन्दाट्ठञ्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — AkrandAwWaYca"


class Sutra4438:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.38: अग्निः'),
		('रामः', '', 'प.4.4.38: रामः'),
		('सीता', '', 'प.4.4.38: सीता'),
	]

