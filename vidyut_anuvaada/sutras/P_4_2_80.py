# Sutra प.4.2.80: वुञ्छण्कठजिलशेनिरढञ्ण्ययफक्फिञिञ्ञ्यकक्ठकोऽरीहणकृशाश्वर्श्यकुमुदकाशतृणप्रेक्षाऽश्मसखिसंकाशबलपक्षकर्णसुतंगमप्रगदिन्वराहकुमुदादिभ्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vuYCaRkaWajilaSeniraQaYRyayaPakPiYiYYyakakWako'rIhaRakfSASvarSyakumudakASatfRaprekzA'SmasaKisaMkASabalapakzakarRasutaMgamapragadinvarAhakumudAdiByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.80"
SUTRA_TEXT = "वुञ्छण्कठजिलशेनिरढञ्ण्ययफक्फिञिञ्ञ्यकक्ठकोऽरीहणकृशाश्वर्श्यकुमुदकाशतृणप्रेक्षाऽश्मसखिसंकाशबलपक्षकर्णसुतंगमप्रगदिन्वराहकुमुदादिभ्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vuYCaRkaWajilaSeniraQaYRyayaPakPiYiYYyakakWako'rIhaRakfSASvarSyakumudakASatfRaprekzA'SmasaKisaMkASabalapakzakarRasutaMgamapragadinvarAhakumudAdiByaH"


class Sutra4280:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.80: अग्निः'),
		('रामः', '', 'प.4.2.80: रामः'),
		('सीता', '', 'प.4.2.80: सीता'),
	]

