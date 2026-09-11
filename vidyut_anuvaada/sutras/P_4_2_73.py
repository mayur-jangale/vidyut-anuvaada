# Sutra प.4.2.73: बह्वचः कूपेषु
# (Sup-sthāna (nominal endings) and kṛt-affixes) — bahvacaH kUpezu

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.73"
SUTRA_TEXT = "बह्वचः कूपेषु"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — bahvacaH kUpezu"


class Sutra4273:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.73: अग्निः'),
		('रामः', '', 'प.4.2.73: रामः'),
		('सीता', '', 'प.4.2.73: सीता'),
	]

