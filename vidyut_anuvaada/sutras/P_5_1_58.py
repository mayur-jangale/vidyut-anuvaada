# Sutra प.5.1.58: संख्यायाः संज्ञासंघसूत्राध्ययनेषु
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMKyAyAH saMjYAsaMGasUtrADyayanezu

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.58"
SUTRA_TEXT = "संख्यायाः संज्ञासंघसूत्राध्ययनेषु"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMKyAyAH saMjYAsaMGasUtrADyayanezu"


class Sutra5158:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.58: अग्निः'),
		('रामः', '', 'प.5.1.58: रामः'),
		('सीता', '', 'प.5.1.58: सीता'),
	]

