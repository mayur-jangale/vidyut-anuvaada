# Sutra प.4.2.95: कत्र्यादिभ्यो ढकञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — katryAdiByo QakaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.95"
SUTRA_TEXT = "कत्र्यादिभ्यो ढकञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — katryAdiByo QakaY"


class Sutra4295:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.95: अग्निः'),
		('रामः', '', 'प.4.2.95: रामः'),
		('सीता', '', 'प.4.2.95: सीता'),
	]

