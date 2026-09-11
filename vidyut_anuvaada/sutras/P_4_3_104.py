# Sutra प.4.3.104: कलापिवैशम्पायनान्तेवासिभ्यश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kalApivESampAyanAntevAsiByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.104"
SUTRA_TEXT = "कलापिवैशम्पायनान्तेवासिभ्यश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kalApivESampAyanAntevAsiByaSca"


class Sutra43104:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.104: अग्निः'),
		('रामः', '', 'प.4.3.104: रामः'),
		('सीता', '', 'प.4.3.104: सीता'),
	]

