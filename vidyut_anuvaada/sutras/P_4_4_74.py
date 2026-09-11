# Sutra प.4.4.74: आवसथात् ष्ठल्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — AvasaTAt zWal

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.74"
SUTRA_TEXT = "आवसथात् ष्ठल्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — AvasaTAt zWal"


class Sutra4474:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.74: अग्निः'),
		('रामः', '', 'प.4.4.74: रामः'),
		('सीता', '', 'प.4.4.74: सीता'),
	]

