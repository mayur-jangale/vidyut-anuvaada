# Sutra प.4.4.89: संज्ञायां धेनुष्या
# (Sup-sthāna (nominal endings) and kṛt-affixes) — saMjYAyAM DenuzyA

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.89"
SUTRA_TEXT = "संज्ञायां धेनुष्या"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — saMjYAyAM DenuzyA"


class Sutra4489:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.89: अग्निः'),
		('रामः', '', 'प.4.4.89: रामः'),
		('सीता', '', 'प.4.4.89: सीता'),
	]

