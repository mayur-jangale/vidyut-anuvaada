# Sutra प.4.3.111: कर्मन्दकृशाश्वादिनिः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — karmandakfSASvAdiniH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.111"
SUTRA_TEXT = "कर्मन्दकृशाश्वादिनिः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — karmandakfSASvAdiniH"


class Sutra43111:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.111: अग्निः'),
		('रामः', '', 'प.4.3.111: रामः'),
		('सीता', '', 'प.4.3.111: सीता'),
	]

