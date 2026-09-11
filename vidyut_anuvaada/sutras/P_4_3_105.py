# Sutra प.4.3.105: पुराणप्रोक्तेषु ब्राह्मणकल्पेषु
# (Sup-sthāna (nominal endings) and kṛt-affixes) — purARaproktezu brAhmaRakalpezu

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.105"
SUTRA_TEXT = "पुराणप्रोक्तेषु ब्राह्मणकल्पेषु"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — purARaproktezu brAhmaRakalpezu"


class Sutra43105:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.105: अग्निः'),
		('रामः', '', 'प.4.3.105: रामः'),
		('सीता', '', 'प.4.3.105: सीता'),
	]

