# Sutra प.5.2.59: मतौ छः सूक्तसाम्नोः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — matO CaH sUktasAmnoH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.59"
SUTRA_TEXT = "मतौ छः सूक्तसाम्नोः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — matO CaH sUktasAmnoH"


class Sutra5259:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.59: अग्निः'),
		('रामः', '', 'प.5.2.59: रामः'),
		('सीता', '', 'प.5.2.59: सीता'),
	]

