# Sutra प.4.4.123: असुरस्य स्वम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — asurasya svam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.123"
SUTRA_TEXT = "असुरस्य स्वम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — asurasya svam"


class Sutra44123:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.123: अग्निः'),
		('रामः', '', 'प.4.4.123: रामः'),
		('सीता', '', 'प.4.4.123: सीता'),
	]

