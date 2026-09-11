# Sutra प.4.4.67: श्राणामांसौदनाट्टिठन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SrARAmAMsOdanAwwiWan

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.67"
SUTRA_TEXT = "श्राणामांसौदनाट्टिठन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SrARAmAMsOdanAwwiWan"


class Sutra4467:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.67: अग्निः'),
		('रामः', '', 'प.4.4.67: रामः'),
		('सीता', '', 'प.4.4.67: सीता'),
	]

