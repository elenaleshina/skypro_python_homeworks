from smartfone import smartfone
catalog = []
phone1 = smartfone("Apple", "IPhon7", "+38765338810")
phone2 = smartfone("Xiaomi", "Redmi_Note_8pro", "+79191098822")
phone3 = smartfone("Samsung", "Galaxy_s24", "+79121109921")
phone4 = smartfone("PACO", "F5_pro", "+4593908410")
phone5 = smartfone("ASUS", "Zenfone_10", "+79171110011")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f" {phone.марка} - {phone.модель}. {phone.номер_телефона}") 
    
