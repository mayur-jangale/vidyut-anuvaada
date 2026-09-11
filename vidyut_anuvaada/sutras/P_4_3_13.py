# Sutra प.4.3.13: विभाषा रोगातपयोः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — viBAzA rogAtapayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.13"
SUTRA_TEXT = "विभाषा रोगातपयोः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — viBAzA rogAtapayoH"


class Sutra4313:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.13: अग्निः'),
		('रामः', '', 'प.4.3.13: रामः'),
		('सीता', '', 'प.4.3.13: सीता'),
	]

