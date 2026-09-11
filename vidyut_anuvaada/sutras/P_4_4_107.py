# Sutra प.4.4.107: समानतीर्थे वासी
# (Sup-sthāna (nominal endings) and kṛt-affixes) — samAnatIrTe vAsI

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.107"
SUTRA_TEXT = "समानतीर्थे वासी"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — samAnatIrTe vAsI"


class Sutra44107:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.107: अग्निः'),
		('रामः', '', 'प.4.4.107: रामः'),
		('सीता', '', 'प.4.4.107: सीता'),
	]

