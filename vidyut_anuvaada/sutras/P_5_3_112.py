# Sutra प.5.3.112: पूगाञ्ञ्योऽग्रामणीपूर्वात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — pUgAYYyo'grAmaRIpUrvAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.112"
SUTRA_TEXT = "पूगाञ्ञ्योऽग्रामणीपूर्वात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — pUgAYYyo'grAmaRIpUrvAt"


class Sutra53112:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.112: अग्निः'),
		('रामः', '', 'प.5.3.112: रामः'),
		('सीता', '', 'प.5.3.112: सीता'),
	]

