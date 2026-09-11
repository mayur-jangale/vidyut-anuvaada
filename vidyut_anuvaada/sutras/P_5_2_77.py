# Sutra प.5.2.77: तावतिथं ग्रहणमिति लुग्वा
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tAvatiTaM grahaRamiti lugvA

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.77"
SUTRA_TEXT = "तावतिथं ग्रहणमिति लुग्वा"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tAvatiTaM grahaRamiti lugvA"


class Sutra5277:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.77: अग्निः'),
		('रामः', '', 'प.5.2.77: रामः'),
		('सीता', '', 'प.5.2.77: सीता'),
	]

