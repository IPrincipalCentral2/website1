










































































































'''



from 10.01 EUR to 1_490.49 DZD .




'''










import os

import sys

import time


from pathlib import Path





cwd = os.path.dirname(os.path.abspath(__file__))


i_path_0_i = os.path.dirname(cwd)


i_folder_of_work_0_i = os.path.join(i_path_0_i, "page_2")







i_content_of_json_0_i = r"""
















{
  "invoice_number": "_____year_____-_____number_____",
  "date": "_____date_____",

  "company": {
    "name": "Billal Debouci Entreprise individual",
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
        "reason": "تسديد الفاتورة رقم _____year_____-_____number_____",
        "from_rib": "_____from_rib_0_____",
        "to_rib": "_____to_rib_0_____"
        
   
    }
    
    
    
  
  
  
}



















"""








i_amount_of_from_0_i = 1_490.49






i_semaphore_of_from_EUR_0_i = False










account_EUR = "00100 946 0310 000 040/26"


account_DZD = "001 00946 0300 001 732/28"


    




if (i_semaphore_of_from_EUR_0_i == True):
    
    
    from_currency = "EUR"
    
    
    currency = "DZD"
    
    
    description_1 = "Acces to Cloud"
    
    
    account_from = account_EUR
    
    
    account_to = account_DZD

    
    
    
    
else:
    
    
    
    from_currency = "DZD"
    
    
    currency = "EUR"
    
    
    description_1 = "Publicity"
    
    
    
    account_from = account_DZD
    
    
    account_to = account_EUR
    
    
    





'''


1;EUR;152.15;DZD;bank;136.94;DZD;extract-ed;15.22

1;DZD;0.01;EUR;bank;0.01;EUR;extract-ed;0.00


'''




exchange_rate = ""


if (from_currency == "EUR"):
    
    
    exchange_rate_1 = 0.01
    
    exchange_rate_2 = 136.94
    
    exchange_rate = "0.01"
    
    
else:
    
    
    exchange_rate_1 = 136.94
    
    exchange_rate_2 = 0.01
    
    exchange_rate = "136.94"
    
    
    






i_amount_0_i = 0.0

i_amount_2_i = 0.0


while (i_amount_2_i < i_amount_of_from_0_i):


    i_amount_2_i = i_amount_0_i * exchange_rate_1


    i_amount_0_i += 0.001






i_amount_0_i -= 0.01    


print(f"i_hello_0_i . i_amount_2_i = {i_amount_2_i} . i_amount_0_i = {i_amount_0_i} .")



#i_amount_0_i = i_amount_of_from_0_i * exchange_rate_2



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


i_content_of_json_1_i = i_content_of_json_1_i.replace("_____from_rib_0_____", account_from)


i_content_of_json_1_i = i_content_of_json_1_i.replace("_____to_rib_0_____", account_to)





print(f"i_content_of_json_1_i = \"\"\"{i_content_of_json_1_i}\"\"\" .")







i_amount_2_i = i_amount_0_i * exchange_rate_1


print(f"1 . from => {i_amount_2_i} {from_currency} . to ==> {i_amount_0_i} {currency} .")



i_result_0_i = i_amount_of_from_0_i * exchange_rate_2

print(f"2 . from : i_amount_of_from_0_i = {i_amount_of_from_0_i} {from_currency} . to : i_result_0_i = {i_result_0_i} {currency} .")



i_file_of_json_1_i = os.path.join(i_folder_of_work_0_i, "i_facture_0_i.json")



with open(i_file_of_json_1_i, "w") as f_:
    
    
    f_.write(i_content_of_json_1_i)
    
    



i_file_of_html_1_i = os.path.join(i_folder_of_work_0_i, "i_Page_of_Facture_0_i.html")



i_folder_of_work_1_i = os.path.join(cwd)



i_file_of_json_2_i = os.path.join(i_folder_of_work_1_i, "i_facture_0_i.json")


i_file_of_html_2_i = os.path.join(i_folder_of_work_1_i, "index.html")






i_d_0_i = Path(i_file_of_json_1_i)

i_d_1_i = Path(i_file_of_json_2_i)


i_d_1_i.write_bytes(i_d_0_i.read_bytes())





i_d_0_i = Path(i_file_of_html_1_i)

i_d_1_i = Path(i_file_of_html_2_i)


i_d_1_i.write_bytes(i_d_0_i.read_bytes())




































