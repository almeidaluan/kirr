import random
import string

#Gera a url
def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#Salva a url recebendo a instancia para gerar o shorturl
def create_shortcode(instance,size=6):
    new_code = code_generator(size=size)
    print(instance)
    print(instance.__class__)
    print(instance.__class__.__name__)
    Klass = instance.__class__

    qs_exists = Klass.objects.filter(shorturl=new_code).exists()

    if  qs_exists:
        return create_shortcode(size=size)
    return new_code