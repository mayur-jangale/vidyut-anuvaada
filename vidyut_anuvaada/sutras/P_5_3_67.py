# Sutra प.5.3.67: ईषदसमाप्तौ कल्पब्देश्यदेशीयरः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — IzadasamAptO kalpabdeSyadeSIyaraH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.67"
SUTRA_TEXT = "ईषदसमाप्तौ कल्पब्देश्यदेशीयरः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — IzadasamAptO kalpabdeSyadeSIyaraH"


class Sutra5367:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.67: अग्निः'),
		('रामः', '', 'प.5.3.67: रामः'),
		('सीता', '', 'प.5.3.67: सीता'),
	]

