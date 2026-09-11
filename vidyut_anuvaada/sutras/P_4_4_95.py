# Sutra प.4.4.95: हृदयस्य प्रियः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — hfdayasya priyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.95"
SUTRA_TEXT = "हृदयस्य प्रियः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — hfdayasya priyaH"


class Sutra4495:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.95: अग्निः'),
		('रामः', '', 'प.4.4.95: रामः'),
		('सीता', '', 'प.4.4.95: सीता'),
	]

