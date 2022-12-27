def get_profile(*,name:str = "julian", profession:str = "programmer") -> str :
    return f"{name} is a {profession}"
    
    
    
print(get_profile(name="manolo", profession="wannabe programmer"))
