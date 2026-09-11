# Sutra प.7.2.73: यमरमनमातां सक् च
# (Taddhita (secondary derivations)) — yamaramanamAtAM sak ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.73"
SUTRA_TEXT = "यमरमनमातां सक् च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — yamaramanamAtAM sak ca"


class Sutra7273:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.73: अग्निः'),
		('रामः', '', 'प.7.2.73: रामः'),
		('सीता', '', 'प.7.2.73: सीता'),
	]

