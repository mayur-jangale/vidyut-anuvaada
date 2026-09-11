# Sutra प.4.3.145: गोश्च पुरीषे
# (Sup-sthāna (nominal endings) and kṛt-affixes) — goSca purIze

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.145"
SUTRA_TEXT = "गोश्च पुरीषे"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — goSca purIze"


class Sutra43145:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.145: अग्निः'),
		('रामः', '', 'प.4.3.145: रामः'),
		('सीता', '', 'प.4.3.145: सीता'),
	]

