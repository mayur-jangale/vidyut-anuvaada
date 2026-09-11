# Sutra प.5.3.80: प्राचामुपादेरडज्वुचौ च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — prAcAmupAderaqajvucO ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.80"
SUTRA_TEXT = "प्राचामुपादेरडज्वुचौ च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — prAcAmupAderaqajvucO ca"


class Sutra5380:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.80: अग्निः'),
		('रामः', '', 'प.5.3.80: रामः'),
		('सीता', '', 'प.5.3.80: सीता'),
	]

