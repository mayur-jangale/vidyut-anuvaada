# Sutra प.4.4.122: रेवतीजगतीहविष्याभ्यः प्रशस्ये
# (Sup-sthāna (nominal endings) and kṛt-affixes) — revatIjagatIhavizyAByaH praSasye

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.122"
SUTRA_TEXT = "रेवतीजगतीहविष्याभ्यः प्रशस्ये"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — revatIjagatIhavizyAByaH praSasye"


class Sutra44122:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.122: अग्निः'),
		('रामः', '', 'प.4.4.122: रामः'),
		('सीता', '', 'प.4.4.122: सीता'),
	]

