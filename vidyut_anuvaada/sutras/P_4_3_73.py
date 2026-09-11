# Sutra प.4.3.73: अणृगयनादिभ्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — aRfgayanAdiByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.73"
SUTRA_TEXT = "अणृगयनादिभ्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — aRfgayanAdiByaH"


class Sutra4373:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.73: अग्निः'),
		('रामः', '', 'प.4.3.73: रामः'),
		('सीता', '', 'प.4.3.73: सीता'),
	]

