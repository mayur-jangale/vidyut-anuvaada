# Sutra प.5.2.27: विनञ्भ्यां नानाञौ नसह
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vinaYByAM nAnAYO nasaha

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.27"
SUTRA_TEXT = "विनञ्भ्यां नानाञौ नसह"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vinaYByAM nAnAYO nasaha"


class Sutra5227:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.27: अग्निः'),
		('रामः', '', 'प.5.2.27: रामः'),
		('सीता', '', 'प.5.2.27: सीता'),
	]

