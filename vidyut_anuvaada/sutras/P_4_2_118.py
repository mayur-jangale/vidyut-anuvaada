# Sutra प.4.2.118: विभाषोशीनरेषु
# (Sup-sthāna (nominal endings) and kṛt-affixes) — viBAzoSInarezu

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.118"
SUTRA_TEXT = "विभाषोशीनरेषु"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — viBAzoSInarezu"


class Sutra42118:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.118: अग्निः'),
		('रामः', '', 'प.4.2.118: रामः'),
		('सीता', '', 'प.4.2.118: सीता'),
	]

