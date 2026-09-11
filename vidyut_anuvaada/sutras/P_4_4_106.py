# Sutra प.4.4.106: ढश्छन्दसि
# (Sup-sthāna (nominal endings) and kṛt-affixes) — QaSCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.106"
SUTRA_TEXT = "ढश्छन्दसि"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — QaSCandasi"


class Sutra44106:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.106: अग्निः'),
		('रामः', '', 'प.4.4.106: रामः'),
		('सीता', '', 'प.4.4.106: सीता'),
	]

