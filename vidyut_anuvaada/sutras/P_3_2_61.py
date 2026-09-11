# Sutra प.3.2.61: सत्सूद्विषद्रुहदुहयुजविदभिदच्छिदजिनीराजामुपसर्गेऽपि क्विप्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — satsUdvizadruhaduhayujavidaBidacCidajinIrAjAmupasarge'pi kvip

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.61"
SUTRA_TEXT = "सत्सूद्विषद्रुहदुहयुजविदभिदच्छिदजिनीराजामुपसर्गेऽपि क्विप्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — satsUdvizadruhaduhayujavidaBidacCidajinIrAjAmupasarge'pi kvip"


class Sutra3261:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

