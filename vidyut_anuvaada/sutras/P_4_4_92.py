# Sutra प.4.4.92: धर्मपथ्यर्थन्यायादनपेते
# (Sup-sthāna (nominal endings) and kṛt-affixes) — DarmapaTyarTanyAyAdanapete

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.92"
SUTRA_TEXT = "धर्मपथ्यर्थन्यायादनपेते"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — DarmapaTyarTanyAyAdanapete"


class Sutra4492:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.92: अग्निः'),
		('रामः', '', 'प.4.4.92: रामः'),
		('सीता', '', 'प.4.4.92: सीता'),
	]

