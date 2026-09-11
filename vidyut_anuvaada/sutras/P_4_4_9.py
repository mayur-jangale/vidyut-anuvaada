# Sutra प.4.4.9: आकर्षात् ष्ठल्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — AkarzAt zWal

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.9"
SUTRA_TEXT = "आकर्षात् ष्ठल्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — AkarzAt zWal"


class Sutra449:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.9: अग्निः'),
		('रामः', '', 'प.4.4.9: रामः'),
		('सीता', '', 'प.4.4.9: सीता'),
	]

