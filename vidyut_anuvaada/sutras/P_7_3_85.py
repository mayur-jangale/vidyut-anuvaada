# Sutra प.7.3.85: जाग्रोऽविचिण्णल्ङित्सु
# (Taddhita (secondary derivations)) — jAgro'viciRRalNitsu

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.85"
SUTRA_TEXT = "जाग्रोऽविचिण्णल्ङित्सु"
SUTRA_DESC = "(Taddhita (secondary derivations)) — jAgro'viciRRalNitsu"


class Sutra7385:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.85: अग्निः'),
		('रामः', '', 'प.7.3.85: रामः'),
		('सीता', '', 'प.7.3.85: सीता'),
	]

