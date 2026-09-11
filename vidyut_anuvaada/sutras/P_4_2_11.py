# Sutra प.4.2.11: पाण्डुकम्बलादिनिः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — pARqukambalAdiniH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.11"
SUTRA_TEXT = "पाण्डुकम्बलादिनिः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — pARqukambalAdiniH"


class Sutra4211:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.11: अग्निः'),
		('रामः', '', 'प.4.2.11: रामः'),
		('सीता', '', 'प.4.2.11: सीता'),
	]

