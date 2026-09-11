# Sutra प.3.2.142: संपृचानुरुधाङ्यमाङ्यसपरिसृसंसृजपरिदेविसंज्वरपरिक्षिपपरिरटपरिवदपरिदहपरिमुहदुषद्विषद्रुहदुहयुजाक्रीडविविचत्यजरजभजातिचरापचरामुषाभ्याहनश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — saMpfcAnuruDANyamANyasaparisfsaMsfjaparidevisaMjvaraparikzipaparirawaparivadaparidahaparimuhaduzadvizadruhaduhayujAkrIqavivicatyajarajaBajAticarApacarAmuzAByAhanaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.142"
SUTRA_TEXT = "संपृचानुरुधाङ्यमाङ्यसपरिसृसंसृजपरिदेविसंज्वरपरिक्षिपपरिरटपरिवदपरिदहपरिमुहदुषद्विषद्रुहदुहयुजाक्रीडविविचत्यजरजभजातिचरापचरामुषाभ्याहनश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — saMpfcAnuruDANyamANyasaparisfsaMsfjaparidevisaMjvaraparikzipaparirawaparivadaparidahaparimuhaduzadvizadruhaduhayujAkrIqavivicatyajarajaBajAticarApacarAmuzAByAhanaSca"


class Sutra32142:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

