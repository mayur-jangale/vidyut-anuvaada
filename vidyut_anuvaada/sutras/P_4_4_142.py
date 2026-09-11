# Sutra प.4.4.142: सर्वदेवात् तातिल्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — sarvadevAt tAtil

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.142"
SUTRA_TEXT = "सर्वदेवात् तातिल्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — sarvadevAt tAtil"


class Sutra44142:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.142: अग्निः'),
		('रामः', '', 'प.4.4.142: रामः'),
		('सीता', '', 'प.4.4.142: सीता'),
	]

