import requests as req
import time
# set_user = input("Enter your F2Pool Username: ")
# set_coin = input("Enter your desired coin in lowercase. E.g. bitcoin, conflux: ")
# set_url = "https://api.f2pool.com/" + set_coin + "/" + set_user

# response = req.get(set_url)
# getBalance = response.json()

# Dictionary mapping to API Url
f2pool_coins = {
    "1": "https://api.f2pool.com/bitcoin/",
    "1": "https://api.f2pool.com/bitcoin-cash/",
    "3": "https://api.f2pool.com/litecoin/",
    "4": "https://api.f2pool.com/ethereum/",
    "5": "https://api.f2pool.com/ethereum-classic/",
    "6": "https://api.f2pool.com/zec/",
    "7": "https://api.f2pool.com/zen/",
    "8": "https://api.f2pool.com/handshake/",
    "9": "https://api.f2pool.com/nervos/",
    "10": "https://api.f2pool.com/raven/",
    "11": "https://api.f2pool.com/conflux/",
    "12": "https://api.f2pool.com/ergo/",
    "13": "https://api.f2pool.com/eth/",
    "14": "https://api.f2pool.com/siacoin-new/",
    "15": "https://api.f2pool.com/dash/",
    "16": "https://api.f2pool.com/decred/",
    "17": "https://api.f2pool.com/zcoin/",
    "18": "https://api.f2pool.com/kadena/",
    "19": "https://api.f2pool.com/xaya/",
    "20": "https://api.f2pool.com/digibyte-sha256d/",
    "21": "https://api.f2pool.com/digibyte-scrypt/",
    "22": "https://api.f2pool.com/digibyte-skein/",
    "23": "https://api.f2pool.com/digibyte-qubit/",
    "24": "https://api.f2pool.com/digibyte-odo/",
    "25": "https://api.f2pool.com/verge-blake2s/",
    "26": "https://api.f2pool.com/verge-scrypt/",
    "27": "https://api.f2pool.com/verge-x17/",
    "28": "https://api.f2pool.com/verge-lyra/",
    "29": "https://api.f2pool.com/verge-groestl/",
    "30": "https://api.f2pool.com/ravenp/"
}


def init():
    print("   ___________________            __      __         __         .__                      ")    
    print("   \_   _____/\_____  \          /  \    /  \_____ _/  |_  ____ |  |__   ___________     ")
    print("    |    __)   /  ____/   ______ \   \/\/   /\__  \\   __\/ ___\|  |  \_/ __ \_  __ \    ")
    print("    |     \   /       \  /_____/  \        /  / __ \|  | \  \___|   Y  \  ___/|  | \/    ")
    print("    \___  /   \_______ \           \__/\  /  (____  /__|  \___  >___|  /\___  >__|       ")
    print("        \/            \/                \/        \/          \/     \/     \/           ")
    print("\n")
    print("                         Author: David Oraha        Version: 0.1                         ")
    print("\n")
    print("      1)  Bitcoin - F2Pool UserName             16) Decred - Decred Address              ")
    print("      2)  Bitcoin Cash - F2Pool Username        17) Firo - Firo Address                  ")
    print("      3)  Litecoin - F2Pool Username            18) Kadena - Kadena Address              ")
    print("      4)  Ethereum - F2Pool Username            19) CHI-Xaya - CHI-Xaya Address          ")
    print("      5)  Ethereum - Eth Address                20) DigiByte-SHA265 - SHA256 Address     ")
    print("      6)  Ethereum Classic - Eth Address        22) DigiByte-SCRYPT - SCRYPT Address     ")
    print("      7)  Zcash - F2Pool Username               23) DigiByte-SKIEN - SKIEN Address       ")
    print("      8)  Horizen - F2Pool UserName             24) DigiByte-ODOCRYPT - ODOCRYPT Address ")
    print("      9)  Handshake - F2Pool Username           25) Verge-BLACK2S - BLACK2S Address      ")
    print("      10) Nervos CKB - F2Pool Username          26) Verge-SCRYPT - SCRYPT Address        ")
    print("      11) Ravencoin - F2Pool Username           27) Verge-X17 - X17 Address              ")
    print("      12) Conflux -  F2Pool Username            28) Verge-LYRA2REV2 - LYRA2REV2 Address  ")
    print("      13) Ergo - F2Pool Username                29) Verge-GROESTL - GROESTL Address      ")
    print("      14) Siacoin - Saicoin Address             30) Ravencoin - Ravencoin Address        ")
    print("      15) Dash - Dash Address                                                            ")
    print("\n")

    coin_select = ""
    username_input = ""
    address_input = ""
    

    coin_select = input("Please enter selection number based on above options: ")
    set_url = f2pool_coins.get(coin_select)
    coin_select = int(coin_select)
    
    if coin_select < 1 or coin_select > 30:
        print("Error: Invalid Number. Needs to be between 1 - 30. Based on the coin options above. Exiting...")
        time.sleep(2)
        exit()
    elif coin_select <= 13:
        username_input = input("Please Enter your F2 Pool Username: ")
    else:
        address_input = input("Please enter your selected coin address: ")

    #Builds API Url
    str(set_url)
    if username_input == "":
        api_url = set_url + address_input
    else:
        api_url = set_url + username_input
    print(api_url)


def main():

   init()

if __name__ == "__main__":
    main()

# response = req.get(set_url)
# print("Current Balance: " + getBalance['balance'])
# time.sleep(5)