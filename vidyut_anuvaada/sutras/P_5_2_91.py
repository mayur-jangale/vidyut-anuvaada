# Sutra प.5.2.91: साक्षाद्द्रष्टरि संज्ञायाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — sAkzAddrazwari saMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.91"
SUTRA_TEXT = "साक्षाद्द्रष्टरि संज्ञायाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — sAkzAddrazwari saMjYAyAm"


class Sutra5291:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.91: अग्निः'),
		('रामः', '', 'प.5.2.91: रामः'),
		('सीता', '', 'प.5.2.91: सीता'),
	]

