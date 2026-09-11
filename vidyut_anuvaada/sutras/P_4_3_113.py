# Sutra प.4.3.113: तसिश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tasiSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.113"
SUTRA_TEXT = "तसिश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tasiSca"


class Sutra43113:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.113: अग्निः'),
		('रामः', '', 'प.4.3.113: रामः'),
		('सीता', '', 'प.4.3.113: सीता'),
	]

