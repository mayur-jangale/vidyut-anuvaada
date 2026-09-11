# Sutra प.4.3.38: कृतलब्धक्रीतकुशलाः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kftalabDakrItakuSalAH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.38"
SUTRA_TEXT = "कृतलब्धक्रीतकुशलाः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kftalabDakrItakuSalAH"


class Sutra4338:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.38: अग्निः'),
		('रामः', '', 'प.4.3.38: रामः'),
		('सीता', '', 'प.4.3.38: सीता'),
	]

