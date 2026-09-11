# Sutra प.4.4.34: शब्ददर्दुरं करोति
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SabdadarduraM karoti

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.34"
SUTRA_TEXT = "शब्ददर्दुरं करोति"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SabdadarduraM karoti"


class Sutra4434:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.34: अग्निः'),
		('रामः', '', 'प.4.4.34: रामः'),
		('सीता', '', 'प.4.4.34: सीता'),
	]

