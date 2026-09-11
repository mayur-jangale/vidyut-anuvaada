# Sutra प.5.2.28: वेः शालच्छङ्कटचौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — veH SAlacCaNkawacO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.28"
SUTRA_TEXT = "वेः शालच्छङ्कटचौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — veH SAlacCaNkawacO"


class Sutra5228:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.28: अग्निः'),
		('रामः', '', 'प.5.2.28: रामः'),
		('सीता', '', 'प.5.2.28: सीता'),
	]

