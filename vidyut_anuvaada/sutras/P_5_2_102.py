# Sutra प.5.2.102: तपःसहस्राभ्यां विनीनी
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tapaHsahasrAByAM vinInI

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.102"
SUTRA_TEXT = "तपःसहस्राभ्यां विनीनी"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tapaHsahasrAByAM vinInI"


class Sutra52102:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.102: अग्निः'),
		('रामः', '', 'प.5.2.102: रामः'),
		('सीता', '', 'प.5.2.102: सीता'),
	]

