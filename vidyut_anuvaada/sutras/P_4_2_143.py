# Sutra प.4.2.143: पर्वताच्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — parvatAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.143"
SUTRA_TEXT = "पर्वताच्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — parvatAcca"


class Sutra42143:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.143: अग्निः'),
		('रामः', '', 'प.4.2.143: रामः'),
		('सीता', '', 'प.4.2.143: सीता'),
	]

