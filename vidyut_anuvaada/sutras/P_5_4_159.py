# Sutra प.5.4.159: नाडीतन्त्र्योः स्वाङ्गे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — nAqItantryoH svANge

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.159"
SUTRA_TEXT = "नाडीतन्त्र्योः स्वाङ्गे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — nAqItantryoH svANge"


class Sutra54159:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.159: अग्निः'),
		('रामः', '', 'प.5.4.159: रामः'),
		('सीता', '', 'प.5.4.159: सीता'),
	]

