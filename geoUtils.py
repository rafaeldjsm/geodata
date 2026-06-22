def fix_geom(g):
    """
    Corrige geometria inválida de forma robusta.
    Usei na correção do primeiro arquivo br_states.json
    que acontecia em Carpina, Pernambuco:
    # Coordenada informada pelo erro
    x_erro = -35.225697852012971
    y_erro = -7.8286115532622551
    """
    if g is None or g.is_empty:
        return g
    # 1) make_valid (preferencial)
    try:
        g = make_valid(g)
    except Exception:
        # 2) fallback: buffer(0) (conserta muitas invalidades simples)
        try:
            g = g.buffer(0)
        except Exception:
            pass
    # 3) set_precision para snap em grid fino (reduz slivers/micro gaps)
    try:
        g = shapely.set_precision(g, 1e-7)  # ajuste o grid conforme necessário
    except Exception:
        pass
    # 4) buffer(0) novamente para consolidar após o snap
    try:
        g = g.buffer(0)
    except Exception:
        pass
    return g    
