# Sutra प.4.3.155: ञितश्च तत्प्रत्ययात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — YitaSca tatpratyayAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.155"
SUTRA_TEXT = "ञितश्च तत्प्रत्ययात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — YitaSca tatpratyayAt"


class Sutra43155:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.155: अग्निः'),
		('रामः', '', 'प.4.3.155: रामः'),
		('सीता', '', 'प.4.3.155: सीता'),
	]

