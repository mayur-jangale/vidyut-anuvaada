# Sutra प.4.3.149: असंज्ञायां तिलयवाभ्याम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — asaMjYAyAM tilayavAByAm

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.149"
SUTRA_TEXT = "असंज्ञायां तिलयवाभ्याम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — asaMjYAyAM tilayavAByAm"


class Sutra43149:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.149: अग्निः'),
		('रामः', '', 'प.4.3.149: रामः'),
		('सीता', '', 'प.4.3.149: सीता'),
	]

