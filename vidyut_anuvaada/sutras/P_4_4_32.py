# Sutra प.4.4.32: उञ्छति
# (Sup-sthāna (nominal endings) and kṛt-affixes) — uYCati

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.32"
SUTRA_TEXT = "उञ्छति"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — uYCati"


class Sutra4432:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.32: अग्निः'),
		('रामः', '', 'प.4.4.32: रामः'),
		('सीता', '', 'प.4.4.32: सीता'),
	]

