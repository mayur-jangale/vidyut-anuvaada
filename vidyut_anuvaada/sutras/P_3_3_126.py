# Sutra प.3.3.126: ईषद्दुःसुषु कृच्छ्राकृच्छ्रार्थेषु खल्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — IzadduHsuzu kfcCrAkfcCrArTezu Kal

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.126"
SUTRA_TEXT = "ईषद्दुःसुषु कृच्छ्राकृच्छ्रार्थेषु खल्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — IzadduHsuzu kfcCrAkfcCrArTezu Kal"


class Sutra33126:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

