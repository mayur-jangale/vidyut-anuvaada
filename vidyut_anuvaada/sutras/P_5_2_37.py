# Sutra प.5.2.37: प्रमाणे द्वयसज्दघ्नञ्मात्रचः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — pramARe dvayasajdaGnaYmAtracaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.37"
SUTRA_TEXT = "प्रमाणे द्वयसज्दघ्नञ्मात्रचः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — pramARe dvayasajdaGnaYmAtracaH"


class Sutra5237:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.37: अग्निः'),
		('रामः', '', 'प.5.2.37: रामः'),
		('सीता', '', 'प.5.2.37: सीता'),
	]

