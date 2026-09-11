# Sutra प.3.4.46: कषादिषु यथाविध्यनुप्रयोगः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kazAdizu yaTAviDyanuprayogaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.46"
SUTRA_TEXT = "कषादिषु यथाविध्यनुप्रयोगः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kazAdizu yaTAviDyanuprayogaH"


class Sutra3446:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

