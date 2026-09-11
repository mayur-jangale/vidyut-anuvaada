# Sutra प.4.2.36: पितृव्यमातुलमातामहपितामहाः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — pitfvyamAtulamAtAmahapitAmahAH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.36"
SUTRA_TEXT = "पितृव्यमातुलमातामहपितामहाः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — pitfvyamAtulamAtAmahapitAmahAH"


class Sutra4236:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.36: अग्निः'),
		('रामः', '', 'प.4.2.36: रामः'),
		('सीता', '', 'प.4.2.36: सीता'),
	]

