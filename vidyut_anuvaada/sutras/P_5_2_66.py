# Sutra प.5.2.66: स्वाङ्गेभ्यः प्रसिते
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — svANgeByaH prasite

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.66"
SUTRA_TEXT = "स्वाङ्गेभ्यः प्रसिते"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — svANgeByaH prasite"


class Sutra5266:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.66: अग्निः'),
		('रामः', '', 'प.5.2.66: रामः'),
		('सीता', '', 'प.5.2.66: सीता'),
	]

