# Sutra प.4.3.125: द्वन्द्वाद्वुन् वैरमैथुनिकयोः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — dvandvAdvun vEramETunikayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.125"
SUTRA_TEXT = "द्वन्द्वाद्वुन् वैरमैथुनिकयोः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — dvandvAdvun vEramETunikayoH"


class Sutra43125:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.125: अग्निः'),
		('रामः', '', 'प.4.3.125: रामः'),
		('सीता', '', 'प.4.3.125: सीता'),
	]

