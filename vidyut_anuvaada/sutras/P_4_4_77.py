# Sutra प.4.4.77: धुरो यड्ढकौ
# (Sup-sthāna (nominal endings) and kṛt-affixes) — Duro yaqQakO

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.77"
SUTRA_TEXT = "धुरो यड्ढकौ"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — Duro yaqQakO"


class Sutra4477:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.77: अग्निः'),
		('रामः', '', 'प.4.4.77: रामः'),
		('सीता', '', 'प.4.4.77: सीता'),
	]

