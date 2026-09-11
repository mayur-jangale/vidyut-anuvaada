# Sutra प.3.4.63: तूष्णीमि भुवः
# ktin — agent noun suffix (kṛtin)

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.63"
SUTRA_TEXT = "तूष्णीमि भुवः"
SUTRA_DESC = "ktin — agent noun suffix (kṛtin)"


class Sutra3463:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

