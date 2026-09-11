# Sutra प.5.2.60: अध्यायानुवाकयोर्लुक्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — aDyAyAnuvAkayorluk

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.60"
SUTRA_TEXT = "अध्यायानुवाकयोर्लुक्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — aDyAyAnuvAkayorluk"


class Sutra5260:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.60: अग्निः'),
		('रामः', '', 'प.5.2.60: रामः'),
		('सीता', '', 'प.5.2.60: सीता'),
	]

