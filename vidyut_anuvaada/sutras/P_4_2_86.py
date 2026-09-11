# Sutra प.4.2.86: मध्वादिभ्यश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — maDvAdiByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.86"
SUTRA_TEXT = "मध्वादिभ्यश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — maDvAdiByaSca"


class Sutra4286:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.86: अग्निः'),
		('रामः', '', 'प.4.2.86: रामः'),
		('सीता', '', 'प.4.2.86: सीता'),
	]

