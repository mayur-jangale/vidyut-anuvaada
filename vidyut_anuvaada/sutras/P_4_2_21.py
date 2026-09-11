# Sutra प.4.2.21: सास्मिन् पौर्णमासीति संज्ञायाम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — sAsmin pOrRamAsIti saMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.21"
SUTRA_TEXT = "सास्मिन् पौर्णमासीति संज्ञायाम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — sAsmin pOrRamAsIti saMjYAyAm"


class Sutra4221:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.21: अग्निः'),
		('रामः', '', 'प.4.2.21: रामः'),
		('सीता', '', 'प.4.2.21: सीता'),
	]

