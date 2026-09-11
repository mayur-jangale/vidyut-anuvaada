# Sutra प.4.4.129: मधोर्ञ च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — maDorYa ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.129"
SUTRA_TEXT = "मधोर्ञ च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — maDorYa ca"


class Sutra44129:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.129: अग्निः'),
		('रामः', '', 'प.4.4.129: रामः'),
		('सीता', '', 'प.4.4.129: सीता'),
	]

