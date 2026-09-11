# Sutra प.5.2.17: अभ्यमित्राच्छ च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — aByamitrAcCa ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.17"
SUTRA_TEXT = "अभ्यमित्राच्छ च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — aByamitrAcCa ca"


class Sutra5217:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.17: अग्निः'),
		('रामः', '', 'प.5.2.17: रामः'),
		('सीता', '', 'प.5.2.17: सीता'),
	]

