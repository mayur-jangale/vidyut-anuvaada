# Sutra प.4.4.42: प्रतिपथमेति ठंश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — pratipaTameti WaMSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.42"
SUTRA_TEXT = "प्रतिपथमेति ठंश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — pratipaTameti WaMSca"


class Sutra4442:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.42: अग्निः'),
		('रामः', '', 'प.4.4.42: रामः'),
		('सीता', '', 'प.4.4.42: सीता'),
	]

