# Sutra प.5.4.3: स्थूलादिभ्यः प्रकारवचने कन्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — sTUlAdiByaH prakAravacane kan

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.3"
SUTRA_TEXT = "स्थूलादिभ्यः प्रकारवचने कन्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — sTUlAdiByaH prakAravacane kan"


class Sutra543:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.3: अग्निः'),
		('रामः', '', 'प.5.4.3: रामः'),
		('सीता', '', 'प.5.4.3: सीता'),
	]

