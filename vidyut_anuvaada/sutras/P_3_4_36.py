# Sutra प.3.4.36: समूलाकृतजीवेषु हन्कृञ्ग्रहः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — samUlAkftajIvezu hankfYgrahaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.36"
SUTRA_TEXT = "समूलाकृतजीवेषु हन्कृञ्ग्रहः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — samUlAkftajIvezu hankfYgrahaH"


class Sutra3436:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

