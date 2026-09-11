# Sutra प.5.1.112: समापनात् सपूर्वपदात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — samApanAt sapUrvapadAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.112"
SUTRA_TEXT = "समापनात् सपूर्वपदात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — samApanAt sapUrvapadAt"


class Sutra51112:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.112: अग्निः'),
		('रामः', '', 'प.5.1.112: रामः'),
		('सीता', '', 'प.5.1.112: सीता'),
	]

