# Sutra प.5.1.56: सोऽस्यांशवस्नभृतयः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — so'syAMSavasnaBftayaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.56"
SUTRA_TEXT = "सोऽस्यांशवस्नभृतयः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — so'syAMSavasnaBftayaH"


class Sutra5156:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.56: अग्निः'),
		('रामः', '', 'प.5.1.56: रामः'),
		('सीता', '', 'प.5.1.56: सीता'),
	]

