class StudentskoUverenje:
  ime = ""
  datum_rodjenja = ""
  mesto_rodjenja = ""
  drzava_rodjenja = ""
  upisana_godina_studija = ""
  upisana_godina_studija_broj = 0
  tip_studiranja = ""
  tip_studija = ""
  mesto_ustanove = ""
  usmerenje = ""
  trajanje = 0
  broj_semestara = 0
  ovlasceno_lice = ""

  def __init__(self, block):
    self.ime = block.ime
    self.datum_rodjenja = block.datum_rodjenja
    self.mesto_rodjenja = block.mesto_rodjenja
    self.drzava_rodjenja = block.drzava_rodjenja
    self.upisana_godina_studija = block.upisana_godina_studija
    self.upisana_godina_studija_broj = block.upisana_godina_studija_broj
    self.tip_studiranja = block.tip_studiranja
    self.tip_studija = block.tip_studija
    self.mesto_ustanove = block.mesto_ustanove
    self.usmerenje = block.usmerenje
    self.trajanje = block.trajanje
    self.broj_semestara = block.broj_semestara
    self.ovlasceno_lice = block.ovlasceno_lice

  def getJSON(self):
    return {
      "ime": self.ime,
      "datum_rodjenja": self.datum_rodjenja,
      "mesto_rodjenja": self.mesto_rodjenja,
      "drzava_rodjenja": self.drzava_rodjenja,
      "upisana_godina_studija": self.upisana_godina_studija,
      "upisana_godina_studija_broj": self.upisana_godina_studija_broj,
      "tip_studija": self.tip_studija,
      "tip_studiranja": self.tip_studiranja,
      "mesto_ustanove": self.mesto_ustanove,
      "usmerenje": self.usmerenje,
      "trajanje": self.trajanje,
      "broj_semestara": self.broj_semestara,
      "ovlasceno_lice": self.ovlasceno_lice,
    }

  def __str__(self):
    return f"ime: {self.ime}\ndatum_rodjenja: {self.datum_rodjenja}\nmesto_rodjenja: {self.mesto_rodjenja}\ndrzava_rodjenja: {self.drzava_rodjenja}\nupisana_godina_studija: {self.upisana_godina_studija}\n"
