# Sutra प.4.3.63: वर्गान्ताच्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vargAntAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.63"
SUTRA_TEXT = "वर्गान्ताच्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vargAntAcca"


class Sutra4363:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.63: अग्निः'),
		('रामः', '', 'प.4.3.63: रामः'),
		('सीता', '', 'प.4.3.63: सीता'),
	]

