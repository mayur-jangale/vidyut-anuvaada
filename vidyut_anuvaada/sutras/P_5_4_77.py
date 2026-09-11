# Sutra प.5.4.77: अचतुरविचतुरसुचतुरस्त्रीपुंसधेन्वनडुहर्क्सामवाङ्मनसाक्षिभ्रुवदारगवोर्वष्ठीवपदष्ठीवनक्तंदिवरात्रिंदिवाहर्दिवसरजसनिःश्रेयसपुरुषायुषद्व्यायुषत्र्यायुषर्ग्यजुषजातोक्षमहोक्षवृद्धोक्षोपशुनगोष्ठश्वाः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — acaturavicaturasucaturastrIpuMsaDenvanaquharksAmavANmanasAkziBruvadAragavorvazWIvapadazWIvanaktaMdivarAtriMdivAhardivasarajasaniHSreyasapuruzAyuzadvyAyuzatryAyuzargyajuzajAtokzamahokzavfdDokzopaSunagozWaSvAH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.77"
SUTRA_TEXT = "अचतुरविचतुरसुचतुरस्त्रीपुंसधेन्वनडुहर्क्सामवाङ्मनसाक्षिभ्रुवदारगवोर्वष्ठीवपदष्ठीवनक्तंदिवरात्रिंदिवाहर्दिवसरजसनिःश्रेयसपुरुषायुषद्व्यायुषत्र्यायुषर्ग्यजुषजातोक्षमहोक्षवृद्धोक्षोपशुनगोष्ठश्वाः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — acaturavicaturasucaturastrIpuMsaDenvanaquharksAmavANmanasAkziBruvadAragavorvazWIvapadazWIvanaktaMdivarAtriMdivAhardivasarajasaniHSreyasapuruzAyuzadvyAyuzatryAyuzargyajuzajAtokzamahokzavfdDokzopaSunagozWaSvAH"


class Sutra5477:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.77: अग्निः'),
		('रामः', '', 'प.5.4.77: रामः'),
		('सीता', '', 'प.5.4.77: सीता'),
	]

