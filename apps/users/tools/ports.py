import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings

class Portkey:
    next = []
    def __init__(self, request):
        if 'next' in request.GET:
            self.next = request.GET['next'].split(',')
        if 'next' in request.POST:
            self.next = request.POST['next'].split(',')
        print(self.next, len(self.next))
    def add(self, dato):
        #en confeccion para mas adelante
        temp = [dato]
        self.next = temp + self.next
    def full(self) -> str:
        if len(self.next) == 0:
            return '/cuentas/me'
        else:
            text = ''
            for t in self.next:
                text += t+','
                text = text[0:-1]
            return text
    def redirect(self) -> str:
        if len(self.next) == 0:
            return ''
        return "?next="+self.full()
    
class PortMail:
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    plain_text = ''
    html_text = ''
    
    def __init__(self, To):
        self.To = To

    def send(self, subject):
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = settings.EMAIL_FROM
        message["To"] = self.To
        part1 = MIMEText(self.plain_text, "plain")
        part2 = MIMEText(self.html_text, "html")
        message.attach(part1)
        message.attach(part2)
        try:
            server = smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT, context=self.context)
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        except:
            print('Correo no entregado')
        else:
            server.sendmail(settings.EMAIL_HOST_USER, self.To, message.as_string())
            server.quit()
            print('enviando correo a: ', self.To)
        
        
            
    def Welcome(self):
        self.plain_text = """
            Bienvenido a la plataforma APALANKT, plataforma digital para desarrollar 
            el comercio electrónico, las 24 Horas del dia y llegar a más clientes
        """
        self.html_text = """
            <html>
                <body>
                    <p>Bienvenidos a la plataforma APALANKT, plataforma digital para desarrollar</p>
                    <p>el comercio electrónico, las 24 Horas del dia y llegar a más clientes</p>
                </body>
            </html>
        """
        self.send('Bienvenido a la plataforma de APALANKT')
    
    def Reset(self, verf):
        self.plain_text = '''
            Resetear la clave de su cuenta de APALANKT
            acceda mediante este enlace: 
            ''' +settings.URL_SITE+ '''/cuentas/verify/''' + verf + '''
            
            Tras completar el cambio de clave, elimine este correo, si usted no ha tenido problemas 
            con su cuenta de APALANKT ignore este correo o eliminelo para evitar problemas de seguridad
        '''
        self.html_text = '''
            <html>
                <body>
                    <p>Resetear la clave de su cuenta de APALANKT</p>
                    <p>acceda mediante este enlace:</p>
                    <br>
                    <p><a href="''' +settings.URL_SITE+ '''/cuentas/verify/''' + verf + '''">Enlace de acceso</a></p>
                    <br>
                    <p>de no funcionar el enlace copie y pegue en el navegador</p>
                    <br>
                    <p>''' +settings.URL_SITE+ '''/cuentas/verify/''' + verf + '''</p>
                    <br>
                    <p>Tras completar el cambio de clave, elimine este correo, si usted no ha tenido problemas 
                    con su cuenta de APALANKT ignore este correo o eliminelo para evitar problemas de seguridad</p>
                </body>
            </html>
        '''
        self.send('Resetear la clave de su cuenta de APALANKT')
        
    def Verf(self, verf):
        self.plain_text = '''
            Para poder entrar en la plataforma de APALANKT debe verificar su cuenta
            su token de acceso es:'''+ verf + ''' 
            o acceda mediante este enlace: 
            ''' +settings.URL_SITE+ '''/cuentas/verify/''' + verf + '''
            Al registrarce en la plataforma usted esta suscrito al boletin de informacion
            para que se mantenga informado de todos los cambios realizados
        '''
        self.html_text = '''
            <html>
                <body>
                    <p>Para poder entrar en la plataforma de APALANKT debe verificar su cuenta</p>
                    <p>su token de acceso es: ''' + verf + '''</p>
                    <p>o acceda mediante este enlace:</p>
                    <p><a href="''' +settings.URL_SITE+ '''/cuentas/verify/''' + verf + '''">Enlace de acceso</a></p>
                    <p>si no funciona el</p>
                    <p>''' +settings.URL_SITE+ '''/cuentas/verify/''' + verf + '''</p>
                    <p>Al registrarce en la plataforma usted esta suscrito al boletin de informacion para que se mantenga informado de todos los cambios realizados</p>
                </body>
            </html>
        '''
        self.send('Verifique su cuenta de APALANKT')
        
    def Notification(self, texto):
        self.plain_text = '''
            Para poder entrar en la plataforma de APALANKT debe verificar su cuenta
            acceda mediante este enlace: 
            ''' +settings.URL_SITE+ '''/cuentas/verify/''' + texto + '''
            
            Al registrarce en la plataforma usted esta suscrito al boletin de informacion
            para que se mantenga informado de todos los cambios realizados
        '''
        self.html_text = '''
            <html>
                <body>
                    <p>Para poder entrar en la plataforma de APALANKT debe verificar su cuenta</p>
                    <p>acceda mediante este enlace:</p>
                    <p><a href="''' +settings.URL_SITE+ '''/cuentas/verify/''' + texto + '''">Enlace de acceso</a></p>
                    <p>si no funciona el</p>
                    <p>''' +settings.URL_SITE+ '''/cuentas/verify/''' + texto + '''</p>
                    <p>Al registrarce en la plataforma usted esta suscrito al boletin de informacion para que se mantenga informado de todos los cambios realizados</p>
                </body>
            </html>
        '''
        self.send('Verifique su cuenta de APALANKT')
        
    def Suscription(self, texto):
        self.plain_text = '''
            Para poder entrar en la plataforma de APALANKT debe verificar su cuenta
            acceda mediante este enlace: 
            ''' +settings.URL_SITE+ '''/cuentas/verify/''' + texto + '''
            
            Al registrarce en la plataforma usted esta suscrito al boletin de informacion
            para que se mantenga informado de todos los cambios realizados
        '''
        self.html_text = '''
            <html>
                <body>
                    <p>Para poder entrar en la plataforma de APALANKT debe verificar su cuenta</p>
                    <p>acceda mediante este enlace:</p>
                    <p><a href="''' +settings.URL_SITE+ '''/cuentas/verify/''' + texto + '''">Enlace de acceso</a></p>
                    <p>si no funciona el</p>
                    <p>''' +settings.URL_SITE+ '''/cuentas/verify/''' + texto + '''</p>
                    <p>Al registrarce en la plataforma usted esta suscrito al boletin de informacion para que se mantenga informado de todos los cambios realizados</p>
                </body>
            </html>
        '''
        self.send('Verifique su cuenta de APALANKT')
        