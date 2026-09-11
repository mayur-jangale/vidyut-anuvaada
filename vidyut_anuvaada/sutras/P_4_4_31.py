# Sutra प.4.4.31: कुसीददशैकादशात् ष्ठन्ष्ठचौ
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kusIdadaSEkAdaSAt zWanzWacO

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.31"
SUTRA_TEXT = "कुसीददशैकादशात् ष्ठन्ष्ठचौ"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kusIdadaSEkAdaSAt zWanzWacO"


class Sutra4431:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.31: अग्निः'),
		('रामः', '', 'प.4.4.31: रामः'),
		('सीता', '', 'प.4.4.31: सीता'),
	]

