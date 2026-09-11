# Sutra प.5.2.33: इनच्पिटच्चिकचि च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — inacpiwaccikaci ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.33"
SUTRA_TEXT = "इनच्पिटच्चिकचि च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — inacpiwaccikaci ca"


class Sutra5233:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.33: अग्निः'),
		('रामः', '', 'प.5.2.33: रामः'),
		('सीता', '', 'प.5.2.33: सीता'),
	]

