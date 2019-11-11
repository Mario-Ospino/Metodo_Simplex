from django.http import HttpResponse
from django.template import Template, Context


def Home(request):  # primera vista

    doc_external_home = open(
        "/home/kmilo9713/Programacion/git_projects/Metodo_Simplex/proyecto_final/templates/Home.html")
    template_home = Template(doc_external_home.read())
    doc_external_home.close()
    ctx_home = Context()

    document_home=template_home.render(ctx_home)
    return HttpResponse(document_home)
