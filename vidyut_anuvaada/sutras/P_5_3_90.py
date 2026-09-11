# Sutra प.5.3.90: कासूगोणीभ्यां ष्टरच्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kAsUgoRIByAM zwarac

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.90"
SUTRA_TEXT = "कासूगोणीभ्यां ष्टरच्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kAsUgoRIByAM zwarac"


class Sutra5390:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.90: अग्निः'),
		('रामः', '', 'प.5.3.90: रामः'),
		('सीता', '', 'प.5.3.90: सीता'),
	]

