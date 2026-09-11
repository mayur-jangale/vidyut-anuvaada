# Sutra प.4.3.160: गोपयसोर्यत्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — gopayasoryat

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.160"
SUTRA_TEXT = "गोपयसोर्यत्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — gopayasoryat"


class Sutra43160:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.160: अग्निः'),
		('रामः', '', 'प.4.3.160: रामः'),
		('सीता', '', 'प.4.3.160: सीता'),
	]

