# Sutra प.5.4.124: धर्मादनिच् केवलात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — DarmAdanic kevalAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.124"
SUTRA_TEXT = "धर्मादनिच् केवलात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — DarmAdanic kevalAt"


class Sutra54124:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.124: अग्निः'),
		('रामः', '', 'प.5.4.124: रामः'),
		('सीता', '', 'प.5.4.124: सीता'),
	]

