# Sutra प.5.4.35: वाचो व्याहृतार्थायाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vAco vyAhftArTAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.35"
SUTRA_TEXT = "वाचो व्याहृतार्थायाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vAco vyAhftArTAyAm"


class Sutra5435:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.35: अग्निः'),
		('रामः', '', 'प.5.4.35: रामः'),
		('सीता', '', 'प.5.4.35: सीता'),
	]

