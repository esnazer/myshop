import json
import requests
import environ, os
env = environ.Env()
environ.Env.read_env()

from cuenta.models import Invoice

class Qvapay:
    
    payload = {
        'app_id': env('qvapay_app_id'),
        'app_secret': env('qvapay_app_secret')
    }
    
    headers = {}
    
    url_info = 'https://qvapay.com/api/v1/info'
    url_balance = 'https://qvapay.com/api/v1/balance'
    url_create_invoice = 'https://qvapay.com/api/v1/create_invoice'
    url_transactions = 'https://qvapay.com/api/v1/transactions'
    
    def __init__(self, invoice):
        try:
            self.invoice = Invoice.objects.get(pk=invoice)
        except:
            self.remove()
        else:
            self.info = self.ver_info()
    
    def __del__(self):
        print('proceso eliminado')
        
    def remove(self):
        print('auto eliminacion de proceso')
        del self
    
    def ver_info(self):
        response = requests.request("POST", self.url_info, headers=self.headers, data=self.payload)
        return json.loads(response.text)
    
    def balance(self):
        response = requests.request("POST", self.url_balance, headers=self.headers, data=self.payload)
        return json.loads(response.text)
    
    def create_invoice(self, id_product, description, amount):
        print('creando el pago para el producto')
        temp_payload = self.payload
        temp_payload['remote_id'] = id_product
        temp_payload['description'] = description
        temp_payload['amount'] = amount
        temp_payload['signed'] = 1
        response = requests.request("POST", self.url_create_invoice, headers=self.headers, data=temp_payload)
        info = json.loads(response.text)
        print('retorno del proceso',info)
        self.invoice.key = info['transation_uuid']
        self.invoice.asset = 'sqpay'
        self.invoice.ext_url = info['signedUrl']
        self.ext_url = info['signedUrl']
        self.save()

    def transactions(self):
        response = requests.request("POST", self.url_transactions, headers=self.headers, data=self.payload)
        return json.loads(response.text)
    
    def paystatus(self):
        print('estado del pago para el producto')
        response = requests.request("POST", self.url_transactions+'/'+self.invoice.key, headers=self.headers, data=self.payload)
        info = json.loads(response.text)
        if info['status'] == 'pending':
            self.invoice.status = 'proc'
        self.save()
            
    def save(self):
        print('guardando datos')
        self.invoice.save()
        
class Telepay:
    
    secret_me = env('qvapay_app_secret')
    
    headers = {
        "Accept": "application/json",
        "AUTHORIZATION": secret_me
    }
    
    url_getMe = "https://api.telepay.cash/rest/getMe"
    url_getBalance = "https://api.telepay.cash/rest/getBalance"
    url_getAssets = "https://api.telepay.cash/rest/getAssets"
    
    def __init__(self, invoice):
        try:
            self.invoice = Invoice.objects.get(pk=invoice)
        except:
            self.remove()
        else:
            self.info = self.ver_info()