# Sutra प.5.4.7: अषडक्षाशितङ्ग्वलंकर्मालम्पुरुषाध्युत्तरपदात् खः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — azaqakzASitaNgvalaMkarmAlampuruzADyuttarapadAt KaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.7"
SUTRA_TEXT = "अषडक्षाशितङ्ग्वलंकर्मालम्पुरुषाध्युत्तरपदात् खः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — azaqakzASitaNgvalaMkarmAlampuruzADyuttarapadAt KaH"


class Sutra547:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.7: अग्निः'),
		('रामः', '', 'प.5.4.7: रामः'),
		('सीता', '', 'प.5.4.7: सीता'),
	]

