# Sutra प.5.4.118: अञ्नासिकायाः संज्ञायां नसं चास्थूलात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — aYnAsikAyAH saMjYAyAM nasaM cAsTUlAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.118"
SUTRA_TEXT = "अञ्नासिकायाः संज्ञायां नसं चास्थूलात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — aYnAsikAyAH saMjYAyAM nasaM cAsTUlAt"


class Sutra54118:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.118: अग्निः'),
		('रामः', '', 'प.5.4.118: रामः'),
		('सीता', '', 'प.5.4.118: सीता'),
	]

