# Sutra प.4.2.100: रंकोरमनुष्येऽण् च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — raMkoramanuzye'R ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.100"
SUTRA_TEXT = "रंकोरमनुष्येऽण् च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — raMkoramanuzye'R ca"


class Sutra42100:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.100: अग्निः'),
		('रामः', '', 'प.4.2.100: रामः'),
		('सीता', '', 'प.4.2.100: सीता'),
	]

