# Sutra प.5.1.20: असमासे निष्कादिभ्यः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — asamAse nizkAdiByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.20"
SUTRA_TEXT = "असमासे निष्कादिभ्यः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — asamAse nizkAdiByaH"


class Sutra5120:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.20: अग्निः'),
		('रामः', '', 'प.5.1.20: रामः'),
		('सीता', '', 'प.5.1.20: सीता'),
	]

