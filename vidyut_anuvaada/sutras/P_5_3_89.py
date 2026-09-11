# Sutra प.5.3.89: कुत्वा डुपच्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kutvA qupac

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.89"
SUTRA_TEXT = "कुत्वा डुपच्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kutvA qupac"


class Sutra5389:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.89: अग्निः'),
		('रामः', '', 'प.5.3.89: रामः'),
		('सीता', '', 'प.5.3.89: सीता'),
	]

