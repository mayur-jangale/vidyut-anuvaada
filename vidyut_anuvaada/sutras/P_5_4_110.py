# Sutra प.5.4.110: नदीपौर्णमास्याग्रहायणीभ्यः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — nadIpOrRamAsyAgrahAyaRIByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.110"
SUTRA_TEXT = "नदीपौर्णमास्याग्रहायणीभ्यः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — nadIpOrRamAsyAgrahAyaRIByaH"


class Sutra54110:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.110: अग्निः'),
		('रामः', '', 'प.5.4.110: रामः'),
		('सीता', '', 'प.5.4.110: सीता'),
	]

