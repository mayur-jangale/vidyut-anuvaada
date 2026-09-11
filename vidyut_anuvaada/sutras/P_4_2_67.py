# Sutra प.4.2.67: तदस्मिन्नस्तीति देशे तन्नाम्नि
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tadasminnastIti deSe tannAmni

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.67"
SUTRA_TEXT = "तदस्मिन्नस्तीति देशे तन्नाम्नि"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tadasminnastIti deSe tannAmni"


class Sutra4267:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.67: अग्निः'),
		('रामः', '', 'प.4.2.67: रामः'),
		('सीता', '', 'प.4.2.67: सीता'),
	]

