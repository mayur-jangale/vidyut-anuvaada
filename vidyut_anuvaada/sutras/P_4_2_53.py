# Sutra प.4.2.53: राजन्यादिभ्यो वुञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — rAjanyAdiByo vuY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.53"
SUTRA_TEXT = "राजन्यादिभ्यो वुञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — rAjanyAdiByo vuY"


class Sutra4253:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.53: अग्निः'),
		('रामः', '', 'प.4.2.53: रामः'),
		('सीता', '', 'प.4.2.53: सीता'),
	]

