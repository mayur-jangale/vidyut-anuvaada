# Sutra प.7.3.73: लुग्वा दुहदिहलिहगुहामात्मनेपदे दन्त्ये
# (Taddhita (secondary derivations)) — lugvA duhadihalihaguhAmAtmanepade dantye

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.73"
SUTRA_TEXT = "लुग्वा दुहदिहलिहगुहामात्मनेपदे दन्त्ये"
SUTRA_DESC = "(Taddhita (secondary derivations)) — lugvA duhadihalihaguhAmAtmanepade dantye"


class Sutra7373:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.73: अग्निः'),
		('रामः', '', 'प.7.3.73: रामः'),
		('सीता', '', 'प.7.3.73: सीता'),
	]

