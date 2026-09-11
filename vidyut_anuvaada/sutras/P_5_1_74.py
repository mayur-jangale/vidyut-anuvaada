# Sutra प.5.1.74: योजनं गच्छति
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — yojanaM gacCati

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.74"
SUTRA_TEXT = "योजनं गच्छति"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — yojanaM gacCati"


class Sutra5174:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.74: अग्निः'),
		('रामः', '', 'प.5.1.74: रामः'),
		('सीता', '', 'प.5.1.74: सीता'),
	]

