# Sutra प.5.4.60: समयाच्च यापनायाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — samayAcca yApanAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.60"
SUTRA_TEXT = "समयाच्च यापनायाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — samayAcca yApanAyAm"


class Sutra5460:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.60: अग्निः'),
		('रामः', '', 'प.5.4.60: रामः'),
		('सीता', '', 'प.5.4.60: सीता'),
	]

