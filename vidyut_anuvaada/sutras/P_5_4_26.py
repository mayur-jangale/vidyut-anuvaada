# Sutra प.5.4.26: अतिथेर्ञ्यः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — atiTerYyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.26"
SUTRA_TEXT = "अतिथेर्ञ्यः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — atiTerYyaH"


class Sutra5426:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.26: अग्निः'),
		('रामः', '', 'प.5.4.26: रामः'),
		('सीता', '', 'प.5.4.26: सीता'),
	]

