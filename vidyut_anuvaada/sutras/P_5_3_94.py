# Sutra प.5.3.94: एकाच्च प्राचाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ekAcca prAcAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.94"
SUTRA_TEXT = "एकाच्च प्राचाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ekAcca prAcAm"


class Sutra5394:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.94: अग्निः'),
		('रामः', '', 'प.5.3.94: रामः'),
		('सीता', '', 'प.5.3.94: सीता'),
	]

