# Sutra प.3.2.182: दाम्नीशसयुयुजस्तुतुदसिसिचमिहपतदशनहः करणे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — dAmnISasayuyujastutudasisicamihapatadaSanahaH karaRe

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.182"
SUTRA_TEXT = "दाम्नीशसयुयुजस्तुतुदसिसिचमिहपतदशनहः करणे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — dAmnISasayuyujastutudasisicamihapatadaSanahaH karaRe"


class Sutra32182:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

