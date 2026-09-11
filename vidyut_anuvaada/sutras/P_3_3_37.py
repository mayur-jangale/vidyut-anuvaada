# Sutra प.3.3.37: परिन्योर्नीणोर्द्यूताभ्रेषयोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — parinyornIRordyUtABrezayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.37"
SUTRA_TEXT = "परिन्योर्नीणोर्द्यूताभ्रेषयोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — parinyornIRordyUtABrezayoH"


class Sutra3337:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

