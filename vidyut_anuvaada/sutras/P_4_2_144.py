# Sutra प.4.2.144: विभाषाऽमनुष्ये
# (Sup-sthāna (nominal endings) and kṛt-affixes) — viBAzA'manuzye

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.144"
SUTRA_TEXT = "विभाषाऽमनुष्ये"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — viBAzA'manuzye"


class Sutra42144:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.144: अग्निः'),
		('रामः', '', 'प.4.2.144: रामः'),
		('सीता', '', 'प.4.2.144: सीता'),
	]

