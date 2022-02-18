import master
first_loop2 = 0

def j_parser():
    import json
    import datetime
    # import FinalCrypto
    if (first_loop2 != 0):
        master.master_func()

    jasonfile = open('channel_messages.json', 'r')
    jasondata = jasonfile.read()
    obj = json.loads(str(jasondata))

    token_list = []
    for i in range(len(obj)-(len(obj)-2)):
        main_count = 0
        count2 = 0
        # del_useless_part = obj[i].get("message").split("\n")
        # del del_useless_part[8]
        print("\n",obj[i].get("message"))
        time = datetime.datetime.fromisoformat(obj[i].get("date"))
        print(f"\nTime when added: {time.hour}:{time.minute}:{time.second}    {time.day}-{time.month}-{time.year}") 
        elements_list = obj[i].get("message").split("\n")
        for j in range(len(elements_list)):
            if (elements_list[j].find("NEW TOKEN FOUND") != -1): #  -1 !=  -1 === False (coin market)  ////    any vale except -1 != -1 true (token found)
                main_count = 1
                for product in elements_list:
                    if (product.find("0x") != -1):
                        address_index = elements_list.index(product)
        if (main_count == 1):
            for product in elements_list:
                    if (product.find("0x") != -1): #coin market = false, count =0 ///// 0x = true, count =1
                        count2 = 1     # agar nahi mila 0x
            if (count2 == 1):
                token_list.append(elements_list[address_index]) #7 is the fixed token address index placement in the list

    # print(c)
    # global token_address
    token_address = token_list[0]
    print(f"\nThis is the latest token's address: {token_address}\n")

    return token_address

    # if (token_address != main_tk_address):
    #     main_tk_address = token_address
    #     if (first_time >= 1):
    #         main_tk_address = 0


    
    # "message": "\ud83d\udd35 COINMARKETCAP \ud83d\udd35 - NEW TOKEN FOUND\n\nName: MEMEFLATE ($MFLATE)\n
    # Platform: BSC\nLiquidity: 24.73 BNB\nSlippage: 2% (buy)\nSlippage: 2% (sell)
    # \n0xafe3321309a994831884fc1725f4c3236ac79f76\n\nThis token is not listed yet, but will appear in 5-15 
    # minutes in the \"recently added\" section. Use this Premium info with care.",

# new_token_address = token_address