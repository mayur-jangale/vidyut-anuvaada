# Sutra प.3.4.4: यथाविध्यनुप्रयोगः पूर्वस्मिन्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — yaTAviDyanuprayogaH pUrvasmin

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.4"
SUTRA_TEXT = "यथाविध्यनुप्रयोगः पूर्वस्मिन्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — yaTAviDyanuprayogaH pUrvasmin"


class Sutra344:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

