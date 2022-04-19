class ZakupStana:
    mesto_zakljucenja = ""
    datum_zakljucenja = ""
    zakupodavac = ""
    grad_zakupodavca = ""
    ulica_zakupodavca = ""
    jmbg_zakupodavca = '1123456789999'
    licna_karta_zakupodavca = '111111111'
    zakupac = ""
    grad_zakupca = ""
    ulica_zakupca = ""
    jmbg_zakupca = '1123456789999'
    licna_karta_zakupca = '111111111'
    grad_stana = ""
    ulica_stana = ""
    broj_stana = 0
    sprat_stana = 0
    broj_soba = 0
    broj_kuhinja = 0
    broj_kupatila = 0
    broj_terasa = 0
    povrsina_stana = 0
    datum_izdavanja = ""
    datum_izlaska = ""
    zakupnina = 0

    def __init__(self, block):
        self.mesto_zakljucenja = block.mesto_zakljucenja
        self.datum_zakljucenja = block.datum_zakljucenja
        self.zakupodavac = block.zakupodavac
        self.grad_zakupodavca = block.grad_zakupodavca
        self.ulica_zakupodavca = block.ulica_zakupodavca
        self.jmbg_zakupodavca = block.jmbg_zakupodavca
        self.licna_karta_zakupodavca = block.licna_karta_zakupodavca
        self.zakupac = block.zakupac
        self.grad_zakupca = block.grad_zakupca
        self.ulica_zakupca = block.ulica_zakupca
        self.jmbg_zakupca = block.jmbg_zakupca
        self.licna_karta_zakupca = block.licna_karta_zakupca
        self.grad_stana = block.grad_stana
        self.ulica_stana = block.ulica_stana
        self.broj_stana = block.broj_stana
        self.sprat_stana = block.sprat_stana
        self.broj_soba = block.broj_soba
        self.broj_kuhinja = block.broj_kuhinja
        self.broj_kupatila = block.broj_kupatila
        self.broj_terasa = block.broj_terasa
        self.povrsina_stana = block.povrsina_stana
        self.datum_izdavanja = block.datum_izdavanja
        self.datum_izlaska = block.datum_izlaska
        self.zakupnina = block.zakupnina

    def getJSON(self):
        return {
            "mesto_zakljucenja": self.mesto_zakljucenja,
            "datum_zakljucenja": self.datum_zakljucenja,
            "zakupodavac": self.zakupodavac,
            "grad_zakupodavca": self.grad_zakupodavca,
            "ulica_zakupodavca": self.ulica_zakupodavca,
            "jmbg_zakupodavca": self.jmbg_zakupodavca,
            "licna_karta_zakupodavca": self.licna_karta_zakupodavca,
            "zakupac": self.zakupac,
            "grad_zakupca": self.grad_zakupca,
            "ulica_zakupca": self.ulica_zakupca,
            "jmbg_zakupca": self.jmbg_zakupca,
            "licna_karta_zakupca": self.licna_karta_zakupca,
            "grad_stana": self.grad_stana,
            "ulica_stana": self.ulica_stana,
            "broj_stana": self.broj_stana,
            "sprat_stana": self.sprat_stana,
            "broj_soba": self.broj_soba,
            "broj_kuhinja": self.broj_kuhinja,
            "broj_kupatila": self.broj_kupatila,
            "broj_terasa": self.broj_terasa,
            "povrsina_stana": self.povrsina_stana,
            "datum_izdavanja": self.datum_izdavanja,
            "datum_izlaska": self.datum_izlaska,
            "zakupnina": self.zakupnina,
        }
