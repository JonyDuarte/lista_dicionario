# tupla
atributos = ("Nome", "E-mail", "Profissão")

# lista de dicionários
usuarios = [
    {
        atributos[0]: "Fulano de tal",
        atributos[1]:"fulano@gmail.com",
        atributos[2]: "Programador"
    },
    {
        atributos[0]: "Ciclano da Silva",
        atributos[1]: "ciclano@gmail.com",
        atributos[2]: "Gestor"
    },
    {
        atributos[0]: "Beltrano Silvestre",
        atributos[1]: "beltrano@gmail.com",
        atributos[2]: "Administrador"
    }
]

usuario = {}
for atributo in atributos:
        usuario[atributo] = input(f"Informe o valor do campo {atributo}: ")
usuarios.append(usuario)


# exibir dados dos usuários
for usuario in usuarios:
        print("")
        for atributo in atributos:
                print(f"{atributo}: {usuario.get(atributo)}")
print("")



