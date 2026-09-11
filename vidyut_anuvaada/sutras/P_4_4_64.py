# Sutra प.4.4.64: बह्वच्पूर्वपदाट्ठच्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — bahvacpUrvapadAwWac

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.64"
SUTRA_TEXT = "बह्वच्पूर्वपदाट्ठच्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — bahvacpUrvapadAwWac"


class Sutra4464:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.64: अग्निः'),
		('रामः', '', 'प.4.4.64: रामः'),
		('सीता', '', 'प.4.4.64: सीता'),
	]

