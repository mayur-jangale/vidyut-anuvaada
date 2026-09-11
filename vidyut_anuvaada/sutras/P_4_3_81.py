# Sutra प.4.3.81: हेतुमनुष्येभ्योऽन्यतरस्यां रूप्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — hetumanuzyeByo'nyatarasyAM rUpyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.81"
SUTRA_TEXT = "हेतुमनुष्येभ्योऽन्यतरस्यां रूप्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — hetumanuzyeByo'nyatarasyAM rUpyaH"


class Sutra4381:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.81: अग्निः'),
		('रामः', '', 'प.4.3.81: रामः'),
		('सीता', '', 'प.4.3.81: सीता'),
	]

