# Sutra प.5.1.30: द्वित्रिपूर्वान्निष्कात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvitripUrvAnnizkAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.30"
SUTRA_TEXT = "द्वित्रिपूर्वान्निष्कात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvitripUrvAnnizkAt"


class Sutra5130:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.30: अग्निः'),
		('रामः', '', 'प.5.1.30: रामः'),
		('सीता', '', 'प.5.1.30: सीता'),
	]

