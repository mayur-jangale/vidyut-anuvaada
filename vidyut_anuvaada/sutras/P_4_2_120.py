# Sutra प.4.2.120: वृद्धात् प्राचाम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vfdDAt prAcAm

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.120"
SUTRA_TEXT = "वृद्धात् प्राचाम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vfdDAt prAcAm"


class Sutra42120:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.120: अग्निः'),
		('रामः', '', 'प.4.2.120: रामः'),
		('सीता', '', 'प.4.2.120: सीता'),
	]

