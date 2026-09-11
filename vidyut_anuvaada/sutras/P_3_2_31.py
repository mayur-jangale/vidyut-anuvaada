# Sutra प.3.2.31: उदि कूले रुजिवहोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — udi kUle rujivahoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.31"
SUTRA_TEXT = "उदि कूले रुजिवहोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — udi kUle rujivahoH"


class Sutra3231:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

