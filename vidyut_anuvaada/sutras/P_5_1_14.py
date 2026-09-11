# Sutra प.5.1.14: ऋषभोपानहोर्ञ्यः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — fzaBopAnahorYyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.14"
SUTRA_TEXT = "ऋषभोपानहोर्ञ्यः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — fzaBopAnahorYyaH"


class Sutra5114:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.14: अग्निः'),
		('रामः', '', 'प.5.1.14: रामः'),
		('सीता', '', 'प.5.1.14: सीता'),
	]

