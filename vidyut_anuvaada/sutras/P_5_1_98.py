# Sutra प.5.1.98: तेन यथाकथाचहस्ताभ्यां णयतौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tena yaTAkaTAcahastAByAM RayatO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.98"
SUTRA_TEXT = "तेन यथाकथाचहस्ताभ्यां णयतौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tena yaTAkaTAcahastAByAM RayatO"


class Sutra5198:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.98: अग्निः'),
		('रामः', '', 'प.5.1.98: रामः'),
		('सीता', '', 'प.5.1.98: सीता'),
	]

