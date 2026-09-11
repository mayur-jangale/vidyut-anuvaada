# Sutra प.4.3.51: व्याहरति मृगः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vyAharati mfgaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.51"
SUTRA_TEXT = "व्याहरति मृगः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vyAharati mfgaH"


class Sutra4351:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.51: अग्निः'),
		('रामः', '', 'प.4.3.51: रामः'),
		('सीता', '', 'प.4.3.51: सीता'),
	]

