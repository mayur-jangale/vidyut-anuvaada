# Sutra प.5.1.110: विशाखाषाढादण् मन्थदण्डयोः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — viSAKAzAQAdaR manTadaRqayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.110"
SUTRA_TEXT = "विशाखाषाढादण् मन्थदण्डयोः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — viSAKAzAQAdaR manTadaRqayoH"


class Sutra51110:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.110: अग्निः'),
		('रामः', '', 'प.5.1.110: रामः'),
		('सीता', '', 'प.5.1.110: सीता'),
	]

