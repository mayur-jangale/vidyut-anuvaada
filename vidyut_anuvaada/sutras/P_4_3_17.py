# Sutra प.4.3.17: प्रावृष एण्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — prAvfza eRyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.17"
SUTRA_TEXT = "प्रावृष एण्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — prAvfza eRyaH"


class Sutra4317:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.17: अग्निः'),
		('रामः', '', 'प.4.3.17: रामः'),
		('सीता', '', 'प.4.3.17: सीता'),
	]

