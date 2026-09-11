# Sutra प.5.2.85: श्राद्धमनेन भुक्तमिनिठनौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — SrAdDamanena BuktaminiWanO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.85"
SUTRA_TEXT = "श्राद्धमनेन भुक्तमिनिठनौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — SrAdDamanena BuktaminiWanO"


class Sutra5285:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.85: अग्निः'),
		('रामः', '', 'प.5.2.85: रामः'),
		('सीता', '', 'प.5.2.85: सीता'),
	]

