# Sutra प.4.3.64: अशब्दे यत्खावन्यतरस्याम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — aSabde yatKAvanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.64"
SUTRA_TEXT = "अशब्दे यत्खावन्यतरस्याम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — aSabde yatKAvanyatarasyAm"


class Sutra4364:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.64: अग्निः'),
		('रामः', '', 'प.4.3.64: रामः'),
		('सीता', '', 'प.4.3.64: सीता'),
	]

