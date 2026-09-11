# Sutra प.4.2.138: गहादिभ्यश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — gahAdiByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.138"
SUTRA_TEXT = "गहादिभ्यश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — gahAdiByaSca"


class Sutra42138:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.138: अग्निः'),
		('रामः', '', 'प.4.2.138: रामः'),
		('सीता', '', 'प.4.2.138: सीता'),
	]

