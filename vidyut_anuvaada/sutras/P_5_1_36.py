# Sutra प.5.1.36: द्वित्रिपूर्वादण् च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvitripUrvAdaR ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.36"
SUTRA_TEXT = "द्वित्रिपूर्वादण् च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvitripUrvAdaR ca"


class Sutra5136:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.36: अग्निः'),
		('रामः', '', 'प.5.1.36: रामः'),
		('सीता', '', 'प.5.1.36: सीता'),
	]

