# Sutra प.4.2.50: खलगोरथात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — KalagoraTAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.50"
SUTRA_TEXT = "खलगोरथात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — KalagoraTAt"


class Sutra4250:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.50: अग्निः'),
		('रामः', '', 'प.4.2.50: रामः'),
		('सीता', '', 'प.4.2.50: सीता'),
	]

