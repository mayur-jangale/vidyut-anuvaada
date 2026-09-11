# Sutra प.4.3.106: शौनकादिभ्यश्छन्दसि
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SOnakAdiByaSCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.106"
SUTRA_TEXT = "शौनकादिभ्यश्छन्दसि"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SOnakAdiByaSCandasi"


class Sutra43106:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.106: अग्निः'),
		('रामः', '', 'प.4.3.106: रामः'),
		('सीता', '', 'प.4.3.106: सीता'),
	]

