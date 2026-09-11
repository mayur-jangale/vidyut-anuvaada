# Sutra प.5.3.111: प्रत्नपूर्वविश्वेमात्थाल् छन्दसि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — pratnapUrvaviSvemAtTAl Candasi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.111"
SUTRA_TEXT = "प्रत्नपूर्वविश्वेमात्थाल् छन्दसि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — pratnapUrvaviSvemAtTAl Candasi"


class Sutra53111:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.111: अग्निः'),
		('रामः', '', 'प.5.3.111: रामः'),
		('सीता', '', 'प.5.3.111: सीता'),
	]

