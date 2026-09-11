# Sutra प.4.4.63: कर्माध्ययने वृत्तम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — karmADyayane vfttam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.63"
SUTRA_TEXT = "कर्माध्ययने वृत्तम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — karmADyayane vfttam"


class Sutra4463:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.63: अग्निः'),
		('रामः', '', 'प.4.4.63: रामः'),
		('सीता', '', 'प.4.4.63: सीता'),
	]

