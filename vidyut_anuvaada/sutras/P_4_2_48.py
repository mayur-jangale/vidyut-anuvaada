# Sutra प.4.2.48: केशाश्वाभ्यां यञ्छावन्यतरस्याम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — keSASvAByAM yaYCAvanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.48"
SUTRA_TEXT = "केशाश्वाभ्यां यञ्छावन्यतरस्याम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — keSASvAByAM yaYCAvanyatarasyAm"


class Sutra4248:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.48: अग्निः'),
		('रामः', '', 'प.4.2.48: रामः'),
		('सीता', '', 'प.4.2.48: सीता'),
	]

