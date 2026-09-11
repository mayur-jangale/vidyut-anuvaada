# Sutra प.5.4.59: संख्यायाश्च गुणान्तायाः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMKyAyASca guRAntAyAH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.59"
SUTRA_TEXT = "संख्यायाश्च गुणान्तायाः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMKyAyASca guRAntAyAH"


class Sutra5459:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.59: अग्निः'),
		('रामः', '', 'प.5.4.59: रामः'),
		('सीता', '', 'प.5.4.59: सीता'),
	]

