from f import*

while True:
    entrada = int(input("""
1) Para se cadastrar
2) Para mostrar a lista de professores
3) Para mostrar a lista de alunos
4) Para fazer login

Digite sua opção: """))

    if entrada == 1:
        nome=input("Digite o seu nome: ")
        email=input("Digite o seu e-mail: ")
        login=input("Digite o seu login: ")
        senha=input("Digite a sua senha: ")
        tipo=int(input("""
Você é:

1) Aluno
2) Professor


Digite sua opção: """))

        if tipo != 1 and tipo != 2:

            print("Entrada inválida, por favor tente novamente.")

        if tipo == 1:
            adicionar(usuario(nome,email,login,senha), alunos)
            adicionar(usuario2(nome,email), alunos2)
            

        if tipo == 2:
            adicionar(usuario(nome,email,login,senha), professores)
            disci=int(input("""
Disciplinas disponíveis para ministrar:

1) Para Inglês
2) Para Espanhol

Digite sua opção: """))
        
            if disci == 1:
                adicionar(colocar_disciplina(nome,'Inglês'),disciplinas)
                adicionar(usuario2(nome,email),professores2)
            if disci == 2:
                adicionar(colocar_disciplina(nome,'Espanhol'),disciplinas)
                adicionar(usuario2(nome,email),professores2)
        

    if entrada == 2:
        mostra(professores2)

    if entrada == 3:
        mostra(alunos2)

    if entrada == 4:
        sou= int(input("""
1) Se você é Aluno
2) Se você é Professor

Digite sua opção: """))

        if sou == 1:
            if login_a() == True:
                while True:
                    entrada1 = int(input("""
1) Cadastrar e consultar a lista de Idiomas e Horários
2) Cadastrar e consultar a lista de locais disponíveis
3) Para deslogar

Digite sua opção: """))

                    if entrada1 == 1:
                        print("Os horários disponíveis são:")
                        print(40*"=")
                        print("""
Inglês: Segunda a Quarta - 7:00 às 8:30
        Terça a Quinta - 19:00 às 20:30
        
Espanhol: Segunda a Quarta - 7:00 às 8:30
          Terça a Quinta - 19:00 às 20:30 """)
                        print(40*"=")
                        idioma= int(input("""
1) Para se cadastrar em Inglês
2) Para se cadastrar em Espanhol

Digite sua opção: """))
                        if idioma == 1:
                             h=int(input("""
1) Para a aula de Segunda a Quarta, das 7:00 às 8:30
2) Para a aula de Terça a Quinta, das 19:00 às 20:30

Digite sua opção: """))
                             if h == 1:
                                 nome=input("Digite o seu nome:")
                                 adicionar(cadastrar_g(nome,'Segunda a Quarta','7:00 às 8:30'),ingles)

                             if h == 2:
                                 nome=input("Digite seu nome:")
                                 adicionar(cadastrar_g(nome,'Terça a Quinta','19:00 às 20:30'),ingles)      

                        if idioma == 2:
                            h=int(input("""
1) Para a aula de Segunda a Quarta, das 7:00 às 8:30
2) Para a aula de Terça a Quinta, das 19:00 às 20:30

Digite sua opção: """))

                            if h == 1:
                                nome=input("Digite o seu nome:")
                                adicionar(cadastrar_g(nome,'Segunda a Quarta','7:00 às 8:30'),espanhol)

                            if h == 2:
                                nome=input("Digite seu nome:")
                                adicionar(cadastrar_g(nome,'Terça a Quinta','19:00 às 20:30'),espanhol)      
                            

                    if entrada1 == 2:
                        print("Os locais disponíveis são:")
                        print(40*"=")
                        print("No RN: Natal e Mossoró")
                        print("No CE: Fortaleza e Aracati")
                        print(40*"=")
                        local = int(input("""
1) Para se cadastrar no RN
2) Para se cadastrar no CE

Digite sua opção: """))
                        if local == 1:
                            cidade = int(input("""
As cidades disponíveis são:

1) Mossoró
2) Natal

Digite sua opção: """))
                            if cidade ==1:
                                nome = input("Digite o seu nome:")
                                adicionar(cadastrar_local(nome,'RN','Mossoró'),locais)

                            if cidade == 2:
                                nome = input("Digite o seu nome:")
                                adicionar(cadastrar_local(nome,'RN','Natal'),locais)

                        if local == 2:
                            cidade = int(input("""
As cidades disponíveis são:

1) Fortaleza
2) Aracati

Digite sua opção: """))
                            if cidade == 1:
                                nome = input("Digite seu nome:")
                                adicionar(cadastrar_local(nome,'CE','Fortaleza'),locais)

                            if cidade == 2:
                                nome = input("Digite seu nome:")
                                adicionar(cadastrar_local(nome,'CE','Aracati'),locais)

                    if entrada1 == 3:
                        break
                                        

        if sou == 2:
            if login_p() == True:
                while True:
                    entrada2 = int(input("""
1) Cadastrar nota de alunos
2) Adicionar faltas
3) Mostra número de faltas dos alunos
4) Mostra as notas dos alunos
5) Mostrar disciplinas ministradas
6) Para deslogar
       
Digite a opção desejada: """))
                    if entrada2 == 1:
                        nome = input("Digite o nome do aluno:")
                        nota = input("Digite a nota do aluno:")
                        adicionar(colocar_notas(nome,nota),notas)

                    if entrada2 == 2:
                        nome = input("Digite o nome do aluno:")
                        falta = input("Digite a quantidade de faltas:")
                        adicionar(colocar_faltas(nome,falta),faltas)

                    if entrada2 == 3:
                        mostra(faltas)

                    if entrada2 == 4:
                        mostra(notas)

                    if entrada2 == 5:
                        mostra_disciplina()

                    if entrada2 == 6:
                        break
                        
                        
                        

                        

        

