"""DCS reader: parser, pada_form, compact, gold."""

from mayur import dcs, gold

SAMPLE = """## text: Rāmāyaṇa
## text_id: 143
## chapter: Rām, Bā, 1
## chapter_id: 1067

# text = tapaḥsvādhyāyanirataṃ tapasvī vāgvidāṃ varam
# sent_id = 1
# sent_counter = 1
# sent_subcounter = 1
1-3\ttapaḥsvādhyāyanirataṃ\t_\t_\t_\t_\t_\t_\t_\t_
1\ttapas\ttapas\tNOUN\t_\tCase=Cpd\t_\t_\t_\tLemmaId=1|Unsandhied=tapas|WordSem=5
2\tsvādhyāya\tsvādhyāya\tNOUN\t_\tCase=Cpd\t_\t_\t_\tLemmaId=2|Unsandhied=svādhyāya
3\tniratam\tniram\tVERB\t_\tCase=Acc|Gender=Masc|Number=Sing|VerbForm=Part\t_\t_\t_\tUnsandhied=niratam|WordSem=89598
4\tvālmīkir\tvālmīki\tNOUN\t_\tCase=Nom|Gender=Masc|Number=Sing\t_\t_\t_\tUnsandhied=vālmīkiḥ

# text = kaś ca
# sent_counter = 2
# sent_subcounter = 1
1\tkaś\tka\tPRON\t_\tCase=Nom|Gender=Masc|Number=Sing\t_\t_\t_\tUnsandhied=kaḥ
"""


def test_parse_sentences():
    sents = list(dcs.parse_sentences(SAMPLE.splitlines()))
    assert len(sents) == 2
    first = sents[0]
    assert first["text"] == "तपःस्वाध्यायनिरतं तपस्वी वाग्विदां वरम्"
    assert (first["sent_counter"], first["sent_subcounter"], first["chapter_id"]) == (1, 1, "1067")
    assert [t["form"] for t in first["tokens"]] == ["तपस्", "स्वाध्याय", "निरतम्", "वाल्मीकिस्"]
    assert [t["compound_member"] for t in first["tokens"]] == [True, True, False, False]
    part = first["tokens"][2]
    assert part["lemma"] == "निरम्" and part["upos"] == "VERB" and part["word_sem"] == "89598"
    assert part["feats"] == {"Case": "Acc", "Gender": "Masc", "Number": "Sing", "VerbForm": "Part"}
    assert first["tokens"][0]["feats"] == {}
    assert sents[1]["tokens"][0]["form"] == "कस्"


def test_pada_form():
    assert dcs.pada_form("रामः", "राम") == "रामस्"
    assert dcs.pada_form("पुनः", "पुनर्") == "पुनर्"
    assert dcs.pada_form("गीः", "गिर्") == "गीर्"  # the stem's own र् (8.2.76 lengthens the vowel)
    assert dcs.pada_form("गिरः", "गिर्") == "गिरस्"  # the ending's स्, though the lemma ends in र्
    assert dcs.pada_form("चेरुः", "चर्") == "चेरुस्" and dcs.pada_form("चत्वारः", "चतुर्") == "चत्वारस्"
    assert dcs.pada_form("कविः", "कवि") == "कविस्"
    assert dcs.pada_form("वाल्मीकिः", "वाल्मीकि") == "वाल्मीकिस्"
    assert dcs.pada_form("पितरः", "पितृ") == "पितरस्"
    assert dcs.pada_form("पितुः", "पितृ", {"Case": "Gen", "Number": "Sing"}) == "पितुर्"
    assert dcs.pada_form("कुर्युः", "कृ", {"Tense": "Pres", "Number": "Plur"}) == "कुर्युस्"
    assert dcs._repair_vocative("रावणैः", "रावण", {"Case": "Voc", "Number": "Sing"}) == "रावण"
    assert dcs._repair_vocative("रावणैः", "रावण", {"Case": "Ins", "Number": "Plur"}) == "रावणैः"
    assert dcs.pada_form("पितः", "पितृ", {"Case": "Voc", "Number": "Sing"}) == "पितर्"
    assert dcs.pada_form("निरतं", "निरम्") == "निरतम्"
    assert dcs.pada_form("च", "च") == "च"
    assert dcs.pada_form("गीः", "गिर्") == "गीर्"


def test_compact():
    assert dcs.compact("को न्व् अस्मिन्") == "को न्वस्मिन्"
    assert dcs.compact("कश् च") == "कश्च"
    assert dcs.compact("वाल्मीकिर् मुनिपुंगवम्") == "वाल्मीकिर्मुनिपुंगवम्"
    assert dcs.compact("नारदं परिपप्रच्छ") == "नारदं परिपप्रच्छ"
    assert dcs.compact("रामः सीता") == "रामः सीता"
    assert dcs.compact("एकः") == "एकः"


def test_gold_first_verse():
    assert len(gold.load()["verses"]) == 79
    assert gold.verse_text(1) == "तपःस्वाध्यायनिरतं तपस्वी वाग्विदां वरम् । नारदं परिपप्रच्छ वाल्मीकिर्मुनिपुंगवम् ॥"
    v = gold.verse(1)
    assert v["id"] == "रामायण १.१.१" and len(v["lines"]) == 2
    word = v["lines"][0]["words"][2]
    assert word["form"] == "निरतम्" and word["lemma"] == "निरम्" and not word["compound_member"]
    assert gold.load()["license"] == "CC BY 4.0"
