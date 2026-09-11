# Sutra प.4.4.40: प्रतिकण्ठार्थललामं च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — pratikaRWArTalalAmaM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.40"
SUTRA_TEXT = "प्रतिकण्ठार्थललामं च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — pratikaRWArTalalAmaM ca"


class Sutra4440:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.40: अग्निः'),
		('रामः', '', 'प.4.4.40: रामः'),
		('सीता', '', 'प.4.4.40: सीता'),
	]

