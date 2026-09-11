# Sutra प.4.3.150: द्व्यचश्छन्दसि
# (Sup-sthāna (nominal endings) and kṛt-affixes) — dvyacaSCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.150"
SUTRA_TEXT = "द्व्यचश्छन्दसि"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — dvyacaSCandasi"


class Sutra43150:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.150: अग्निः'),
		('रामः', '', 'प.4.3.150: रामः'),
		('सीता', '', 'प.4.3.150: सीता'),
	]

