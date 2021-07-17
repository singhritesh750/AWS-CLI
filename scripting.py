import os
os.system('gcloud config set account anmol-bigtable-test')
#os.system('ls -l')

#from google.oauth2 import service_account
#from google.cloud import language

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/home/joe/mainnet-beta-556ea120c673.json'
#credentials = service_account.Credentials.from_service_account_file("/home/joe/mainnet-beta-d57bfc12d441-anmol-bigtable-test.json")
#client = language.LanguageServiceClient(credentials=credentials)

fhand4 = os.popen('./solana-ledger-tool bigtable transaction-history -l . 3itU5ME8L6FDqtMiRoUiT1F7PwbkTtHBbW51YWD5jtjm')
output1 = fhand4.readlines()
fhand3 = open('list_of_signature.txt','a')

for sig in output1:
    #print(sig.split("\n")[0])
    fhand3.write(sig)

    sig = sig.split("\n")[0]
    fhand5 = os.popen('curl -X POST -H "Content-Type: application/json" -d \'{"jsonrpc":"2.0", "id":1, "method":"getConfirmedTransaction","params":["'+sig+'","json"]}\' https://api.mainnet-beta.solana.com')
    output2 = fhand5.readlines()
    fhand6 = open('signature_details.txt','a')
    #print(output)
    #output = fhand4.read()
    for detail_ in output2: 
        fhand6.write(detail_)

os.system('gcloud auth activate-service-account anmol-bigtable-test@mainnet-beta.iam.gserviceaccount.com --key-file=/home/joe/mainnet-beta-556ea120c673.json')

fhand5 = open('signature_details.txt')
output3 = fhand5.readlines()
fhandle = open('single_signature_detail.json','a')

for details_ in output3:
    details_ = details_.split("\n")[0]
    fhandle.write(details_)
    #print(details_)
    #os.system('gcloud auth activate-service-account anmol-bigtable-test@mainnet-beta.iam.gserviceaccount.com --key-file=/home/joe/mainnet-beta-556ea120c673.json')
    os.popen('bq load --autodetect --source_format=NEWLINE_DELIMITED_JSON bigtable.main /home/sol/.local/share/solana/install/releases/stable-337de510885eebe8ab045a1e322b1f77a959c29a/solana-release/bin/single_signature_detail.json /home/joe/load_bq.json')

#fhand8 | python3 pipefix.py
fhand4.close()
fhand3.close()
fhand5.close()
fhand6.close()
#fhand8.close()
fhandle.close()


'''fhand3 = open('list_of_signature.txt','a')
#print(output)
#output = fhand4.read()

for sig in output1:
    sig1 = sig.strip()
    sig2 = str(sig1.split())
#    for sig1 in sig:
#        fhand3.write(sig1)
#   test = 'curl -X POST -H "Content-Type: application/json" -d \'{"jsonrpc":"2.0", "id":1, "method":"getConfirmedTransaction","params":["'+sig+'","json"]}\' https://api.mainnet-beta.solana.com'
#   fhand5 = os.popen(test)
    fhand5 = os.popen('curl -X POST -H "Content-Type: application/json" -d \'{"jsonrpc":"2.0", "id":1, "method":"getConfirmedTransaction","params":["3YrKFHKBZLCxz8sKpoato48ZeE5JVrnnE3mcGgdqRqwsLtnu8iRWxCSwoooNYSLaLeRHK3a3xWyPvU6wq19NA9vq","json"]}\' https://api.mainnet-beta.solana.com')
#    fhand5 = os.popen('curl -X POST -H "Content-Type: application/json" -d \'{"jsonrpc":"2.0", "id":1, "method":"getConfirmedTransaction","params":["'+str(sig)+'","json"]}\' https://api.mainnet-beta.solana.com')
    output2 = fhand5.readlines()
    fhand6 = open('signature_details.txt','a')
        #print(output)
        #output = fhand4.read()
    for detail_ in output2:
        fhand6.write(detail_)
#        fhand7 = os.popen('bq load --autodetect --source_format=NEWLINE_DELIMITED_JSON bigtable.main gs://finance-289703/com.json ./save/bq_lo.json')

#fhand1.close()
#fhand2.close()
fhand4.close()
fhand3.close()
'''
