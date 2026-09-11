# Sutra प.5.1.90: षष्टिकाः षष्टिरात्रेण पच्यन्ते
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — zazwikAH zazwirAtreRa pacyante

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.90"
SUTRA_TEXT = "षष्टिकाः षष्टिरात्रेण पच्यन्ते"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — zazwikAH zazwirAtreRa pacyante"


class Sutra5190:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.90: अग्निः'),
		('रामः', '', 'प.5.1.90: रामः'),
		('सीता', '', 'प.5.1.90: सीता'),
	]

