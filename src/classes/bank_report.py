class BankReport:
    name_surname = ""
    jmbg = '1123456789999'
    address = ""
    identity_card = '111111111'
    identity_card_city = ""
    job_title = ""
    company = ""
    start_date = '01-01-2000'
    permanent_start_date = '01-01-2000'
    work_place = ""
    phone = 0
    work_year = 0
    work_month = 0
    bruto = '0,000.00'
    neto = '0,000.00'
    suspension = '0,000.00'
    bank_account = '000-0000000000000-00'
    bank = ""
    company_address = ""
    company_id_number = 0
    pib = 0
    work_field = ""
    contact_person = ""
    authorized_person =""

    def __init__(self, block):
        self.name_surname = block.name_surname
        self.jmbg = block.jmbg
        self.address = block.address
        self.identity_card = block.identity_card
        self.identity_card_city = block.identity_card_city
        self.job_title = block.job_title
        self.company = block.company
        self.start_date = block.start_date
        self.permanent_start_date = block.permanent_start_date
        self.work_place = block.work_place
        self.phone = block.phone
        self.work_year = block.work_year
        self.work_month = block.work_month
        self.bruto = block.bruto
        self.neto = block.neto
        self.suspension = block.suspension
        self.bank_account = block.bank_account
        self.bank = block.bank
        self.company_address = block.company_address
        self.company_id_number = block.company_id_number
        self.pib = block.pib
        self.work_field = block.work_field
        self.contact_person = block.contact_person
        self.authorized_person = block.authorized_person

    def getJSON(self):
        return {
            "name_surname": self.name_surname,
            "jmbg": self.jmbg,
            "address": self.address,
            "identity_card": self.identity_card,
            "identity_card_city": self.identity_card_city,
            "job_title": self.job_title,
            "company": self.company,
            "start_date": self.start_date,
            "permanent_start_date": self.permanent_start_date,
            "work_place": self.work_place,
            "phone": self.phone,
            "work_year": self.work_year,
            "work_month": self.work_month,
            "bruto": self.bruto,
            "neto": self.neto,
            "suspension": self.suspension,
            "bank_account": self.bank_account,
            "bank": self.bank,
            "company_address": self.company_address,
            "company_id_number": self.company_id_number,
            "pib": self.pib,
            "work_field": self.work_field,
            "contact_person": self.contact_person,
            "authorized_person": self.authorized_person,
        }
    