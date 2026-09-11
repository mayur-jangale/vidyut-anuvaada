# Sutra प.4.2.81: जनपदे लुप्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — janapade lup

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.81"
SUTRA_TEXT = "जनपदे लुप्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — janapade lup"


class Sutra4281:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.81: अग्निः'),
		('रामः', '', 'प.4.2.81: रामः'),
		('सीता', '', 'प.4.2.81: सीता'),
	]

