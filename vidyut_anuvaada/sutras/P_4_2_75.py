# Sutra प.4.2.75: संकलादिभ्यश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — saMkalAdiByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.75"
SUTRA_TEXT = "संकलादिभ्यश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — saMkalAdiByaSca"


class Sutra4275:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.75: अग्निः'),
		('रामः', '', 'प.4.2.75: रामः'),
		('सीता', '', 'प.4.2.75: सीता'),
	]

