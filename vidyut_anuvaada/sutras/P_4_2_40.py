# Sutra प.4.2.40: केदाराद्यञ् च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kedArAdyaY ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.40"
SUTRA_TEXT = "केदाराद्यञ् च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kedArAdyaY ca"


class Sutra4240:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.40: अग्निः'),
		('रामः', '', 'प.4.2.40: रामः'),
		('सीता', '', 'प.4.2.40: सीता'),
	]

