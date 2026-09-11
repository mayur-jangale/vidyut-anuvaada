# Sutra प.5.2.35: कर्मणि घटोऽठच्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — karmaRi Gawo'Wac

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.35"
SUTRA_TEXT = "कर्मणि घटोऽठच्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — karmaRi Gawo'Wac"


class Sutra5235:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.35: अग्निः'),
		('रामः', '', 'प.5.2.35: रामः'),
		('सीता', '', 'प.5.2.35: सीता'),
	]

