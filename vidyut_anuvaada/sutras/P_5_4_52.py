# Sutra प.5.4.52: विभाषा साति कार्त्स्न्ये
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — viBAzA sAti kArtsnye

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.52"
SUTRA_TEXT = "विभाषा साति कार्त्स्न्ये"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — viBAzA sAti kArtsnye"


class Sutra5452:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.52: अग्निः'),
		('रामः', '', 'प.5.4.52: रामः'),
		('सीता', '', 'प.5.4.52: सीता'),
	]

