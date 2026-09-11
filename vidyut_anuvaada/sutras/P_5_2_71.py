# Sutra प.5.2.71: ब्राह्मणकोष्णिके संज्ञायाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — brAhmaRakozRike saMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.71"
SUTRA_TEXT = "ब्राह्मणकोष्णिके संज्ञायाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — brAhmaRakozRike saMjYAyAm"


class Sutra5271:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.71: अग्निः'),
		('रामः', '', 'प.5.2.71: रामः'),
		('सीता', '', 'प.5.2.71: सीता'),
	]

