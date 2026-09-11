# Sutra प.7.2.19: धृषिशसी वैयात्ये
# (Taddhita (secondary derivations)) — DfziSasI vEyAtye

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.19"
SUTRA_TEXT = "धृषिशसी वैयात्ये"
SUTRA_DESC = "(Taddhita (secondary derivations)) — DfziSasI vEyAtye"


class Sutra7219:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.19: अग्निः'),
		('रामः', '', 'प.7.2.19: रामः'),
		('सीता', '', 'प.7.2.19: सीता'),
	]

