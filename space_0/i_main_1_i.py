















































































































import os

import sys

import time





cwd = os.path.dirname(os.path.abspath(__file__))


i_path_0_i = os.path.dirname(cwd)


i_folder_of_work_0_i = os.path.join(i_path_0_i, "page_2")







i_content_of_json_0_i = r"""
















{
  "invoice_number": "_____year_____-_____number_____",
  "date": "_____date_____",

  "company": {
    "name": "IEntreprise0I Entreprise individual",
    "address": "Ouargla, Algeria",
    "phone": "+213 561 577 437",
    "email": "deboubil24@gmail.com"
  },

  "client": {
    "name": "_____name_of_client_____",
    "address": "_____address_of_client_____"
  },

  "items": [
    {
      "description": "Vbox Marcketing",
      "quantity": 1,
      "unit_price": 2
    },
    {
      "description": "_____description_1_____",
      "quantity": _____quantity_of_product_1_____,
      "unit_price": 1
    },
    {
      "description": "Control Browzering",
      "quantity": 1,
      "unit_price": 4
    }
  ],

  "currency": "_____currency_____",

  "transfer_request": {
    "from_currency": "_____from_currency_____",
    "to_currency": "_____currency_____",
    "exchange_rate": _____exchange_rate_____,
    "reason": "تسديد الفاتورة رقم _____year_____-_____number_____"
  }
}



















"""








i_amount_of_from_0_i = 50.0






i_semaphore_of_from_EUR_0_i = True








    




if (i_semaphore_of_from_EUR_0_i == True):
    
    
    from_currency = "EUR"
    
    
    currency = "DZD"
    
    
    description_1 = "Acces to Cloud"
    
    
else:
    
    
    
    from_currency = "DZD"
    
    
    currency = "EUR"
    
    
    description_1 = "Publicity"
    
    
    







exchange_rate = ""


if (from_currency == "EUR"):
    
    
    exchange_rate_1 = 0.01
    
    exchange_rate = "0.01"
    
    
else:
    
    
    exchange_rate_1 = 135.00
    
    
    exchange_rate = "135.00"
    
    
    




i_amount_0_i = 1.0


i_counter_0_i = 0.0


i_counter_1_i = 0.0


while (i_counter_1_i < i_amount_of_from_0_i):
    
    
    i_counter_1_i = ( i_amount_0_i + i_counter_0_i ) * exchange_rate_1
    
    i_counter_0_i += 1
    
    
    


i_amount_0_i = i_amount_0_i + i_counter_0_i

    


year = time.strftime("%Y")



i_number_0_i = ( ( ( int(time.strftime("%m")) - 1 ) * 31 ) + int(time.strftime("%d")) + int(time.strftime("%H")) + int(time.strftime("%M")) )



number = str(i_number_0_i)




date = time.strftime("%Y/%m/%d")






i_amount_1_i = i_amount_0_i - 6




quantity_of_product_1 = str(i_amount_1_i)






name_of_client = ""

address_of_client = ""


if (from_currency == "EUR"):
    
    name_of_client = "Bilal Benali"
    
    address_of_client = "Oran , Algeria"
    
else:
    
    
    name_of_client = "Steve Arnault"
    
    address_of_client = "Paris , France"
    
    
    
    
    







i_content_of_json_1_i = i_content_of_json_0_i


i_content_of_json_1_i = i_content_of_json_1_i.replace("_____year_____", year)


i_content_of_json_1_i = i_content_of_json_1_i.replace("_____number_____", number)


i_content_of_json_1_i = i_content_of_json_1_i.replace("_____date_____", date)


i_content_of_json_1_i = i_content_of_json_1_i.replace("_____name_of_client_____", name_of_client)


i_content_of_json_1_i = i_content_of_json_1_i.replace("_____address_of_client_____", address_of_client)


i_content_of_json_1_i = i_content_of_json_1_i.replace("_____description_1_____", description_1)


i_content_of_json_1_i = i_content_of_json_1_i.replace("_____quantity_of_product_1_____", quantity_of_product_1)


i_content_of_json_1_i = i_content_of_json_1_i.replace("_____currency_____", currency)


i_content_of_json_1_i = i_content_of_json_1_i.replace("_____from_currency_____", from_currency)


i_content_of_json_1_i = i_content_of_json_1_i.replace("_____exchange_rate_____", exchange_rate)





print(f"i_content_of_json_1_i = \"\"\"{i_content_of_json_1_i}\"\"\" .")







i_amount_2_i = i_amount_0_i * exchange_rate_1


print(f"from => {i_amount_2_i} {from_currency} . to ==> {i_amount_0_i} {currency} .")





i_file_of_json_1_i = os.path.join(i_folder_of_work_0_i, "i_facture_0_i.json")



with open(i_file_of_json_1_i, "w") as f_:
    
    
    f_.write(i_content_of_json_1_i)
    
    




















