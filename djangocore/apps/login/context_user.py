# -*- coding: utf-8 -*-

from .models import Usuario

# Manter foto do perfil na sidebar


def foto_usuario(request):
    context_dict = {}
    # Foto do usuario
    try:
        user_foto = Usuario.objects.get(user=request.user).user_foto
        context_dict['user_foto_sidebar'] = user_foto
    except:
        pass

    # Empresa do usuario


    return context_dict
