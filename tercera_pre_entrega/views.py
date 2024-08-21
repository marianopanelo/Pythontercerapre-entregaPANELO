from django.shortcuts import render,HttpResponse,redirect
from tercera_pre_entrega.models import Comentarios,Reservas ,Usuario
import random
from tercera_pre_entrega.forms import ReservaForm , LoguinForm


def index(req):
    return render (req , 'index.html')

def loguin(req):
    if req.method == 'POST': 
        usuario = LoguinForm(req.POST)
        if usuario.is_valid():
            edad_usuario = usuario.cleaned_data.get('edad')
            if edad_usuario > 17:
                info = usuario.cleaned_data
                agregar_usuario = Usuario(nombre=info['nombre'], apellido=info['apellido'],edad=info['edad'],telefono=info['telefono'],direccion=info['direccion'])
                agregar_usuario.save()
                return render (req , 'fin_registro.html')
            else:
                respuesta = "al ser menor de 18 no puede registrarce"
                return HttpResponse(respuesta)
        else: 
            respuesta = "puso mal algun dato , vuelva a intentarlo"
            return HttpResponse(respuesta)
    else: 
        loguin = LoguinForm()

    return render (req , 'loguin.html',{"loguin": loguin})
    


def cabanas(req):
    return render (req , 'cabanas.html')


def reservar(req):

    if req.method == 'POST': 
        reservacion = ReservaForm(req.POST)
        if reservacion.is_valid():
            nombre_cabaña = reservacion.cleaned_data.get('cabana')
            noches_hospedado = reservacion.cleaned_data.get('noches_de_estadia')
            cabañas = ["El Refugio del Cóndor", "El Mirador de las Sierras", "El Abrazo de la Montaña", "Piedra del Águila"]

            if nombre_cabaña in cabañas:
                if nombre_cabaña == "El Refugio del Cóndor":
                    total_a_pagar = (noches_hospedado * 250000)
                elif nombre_cabaña == "El Mirador de las Sierras":
                    total_a_pagar = (noches_hospedado * 200000)
                elif nombre_cabaña == "El Abrazo de la Montaña":
                    total_a_pagar = (noches_hospedado * 180000)
                elif nombre_cabaña == "Piedra del Águila":
                    total_a_pagar = (noches_hospedado * 300000)
                

                codigo_de_reserva = random.randint(1, 100000)
                info = reservacion.cleaned_data
                reserva = Reservas(nombre=info['nombre'], fecha_ingreso=info['fecha_ingreso'],cabaña=info['cabana'],noches_de_estadia=info['noches_de_estadia'],total_a_pagar=total_a_pagar,codigo_de_reserva= codigo_de_reserva)
                reserva.save()#tengo q pasar por metodo get , por sistema el id de una ahora q lo tiene , ahora veo como lo paso x sistema
                return redirect(f'/codigo/?codigo={codigo_de_reserva}')
            else: 
                respuesta = "esa cabaña no existe , ver bien cual cabaña quiere reservar"
                return HttpResponse(respuesta)
    else: 
        formulario = ReservaForm()

    return render (req , 'reservar.html',{"formulario": formulario})


def mis_reservas(req):
    return render (req , 'tus_reservas.html')#tengo q pasarle un formulario para q me pase el codigo de reserva 


def resultado_busqueda_reserva(req):
    codigo = req.GET.get('codigo', '')
    if codigo:
        datos = Reservas.objects.filter(codigo_de_reserva=codigo)
        if datos.exists():
            return render(req, "datos_reserva.html", {"reservas": datos})
        else:
            return HttpResponse("No se encontró ninguna reserva con ese código.")
    else:
        return HttpResponse("No enviaste el código de reserva.")



def comentanos(req):
    if req.method == 'POST':
        cabañas = ["El Refugio del Cóndor", "El Mirador de las Sierras", "El Abrazo de la Montaña", "Piedra del Águila"]
        cabaña_hospedado = req.POST.get('cabaña_hospedado')  

        if cabaña_hospedado in cabañas:
            comentario =Comentarios(nombre=req.POST.get('nombre'),cabaña_hospedado=req.POST.get('cabaña_hospedado'),dia_en_el_que_se_hospedo=req.POST.get('dia_en_el_que_se_hospedo'),comentario=req.POST.get('comentario'))    
            comentario.save()
            return render(req, "index.html")
        else: 
            respuesta = "esa cabaña no existe , ver bien en cual cabaña se quedo"
            return HttpResponse(respuesta)
        
    return render (req , 'comentanos.html')


