# Sutra प.5.3.72: कस्य च दः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kasya ca daH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.72"
SUTRA_TEXT = "कस्य च दः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kasya ca daH"


class Sutra5372:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.72: अग्निः'),
		('रामः', '', 'प.5.3.72: रामः'),
		('सीता', '', 'प.5.3.72: सीता'),
	]

