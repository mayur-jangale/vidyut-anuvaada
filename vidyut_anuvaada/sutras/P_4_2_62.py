# Sutra प.4.2.62: अनुब्राह्मणादिनिः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — anubrAhmaRAdiniH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.62"
SUTRA_TEXT = "अनुब्राह्मणादिनिः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — anubrAhmaRAdiniH"


class Sutra4262:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.62: अग्निः'),
		('रामः', '', 'प.4.2.62: रामः'),
		('सीता', '', 'प.4.2.62: सीता'),
	]

