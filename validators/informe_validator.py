def validate_sex(args_dict):
    if "sexo" in args_dict:
        return args_dict["sexo"] if args_dict["sexo"] in ("M", "F") else None
    else:
        return "ambos"
