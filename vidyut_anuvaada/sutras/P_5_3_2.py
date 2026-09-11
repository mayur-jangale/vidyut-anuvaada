# Sutra प.5.3.2: किंसर्वनामबहुभ्योऽद्व्यादिभ्यः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kiMsarvanAmabahuByo'dvyAdiByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.2"
SUTRA_TEXT = "किंसर्वनामबहुभ्योऽद्व्यादिभ्यः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kiMsarvanAmabahuByo'dvyAdiByaH"


class Sutra532:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.2: अग्निः'),
		('रामः', '', 'प.5.3.2: रामः'),
		('सीता', '', 'प.5.3.2: सीता'),
	]

