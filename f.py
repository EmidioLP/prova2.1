def adicionar(x,l):
    l.append(x)
    return l

def usuario(n, e, l, s):
    return {'Nome': n,
    'e-mail': e,
    'login': l,
    'senha': s}

def usuario2(n, e):
    return {'Nome': n,
            'e-mail': e}

def cadastrar_local(no,e,c):
    return {'Nome': no,
            'Estado': e,
            'Cidade': c}

def cadastrar_g(n,d,h):
    return {'Nome': n,
            'Dia': d ,
            'Horário': h}
            
    
def mostra(l):
    for x in l:
        print(40*"=")
        for k,v in x.items():
            print('{}: {}'.format(k.capitalize(),v))
    print(40*"=")


def mostra_idioma(l):
    print("Cadastrados na Lista:")
    for x in l:
        print(40*"=")
        print(x)
    print(40*"=")

def check_user(l,s):
    res = False
    for a in alunos:
        if a["login"] == l:
            if a["senha"] == s:
                res = True
                return res, "Login realizado com sucesso"
            else:
                return res, "Senha errada"
    return res, "Login não encontrado"


def check_user2(l,s):
    res = False
    for a in professores:
        if a["login"] == l:
            if a["senha"] == s:
                res = True
                return res, "Login realizado com sucesso"
            else:
                return res, "Senha errada"
    return res, "Login não encontrado"        
        

                    

def login_a():
    l = read_string(m="Digite o login: ")
    s = read_string(m="Digite a senha: ")
    r,m = check_user(l,s)
    print(m)
    return r
def login_p():
    l = read_string(m="Digite o login: ")
    s = read_string(m="Digite a senha: ")
    r,m = check_user2(l,s)
    print(m)
    return r

def read_string(*,m=''):
    s = input(m)
    return s            

disciplinas = [{'Nome': 'Alysson' ,
               'disciplinas': 'Inglês'}]

faltas = []

notas = []

locais = []

espanhol = []

ingles = []           

alunos = [{'Nome': 'Emidio',
                 'e-mail': 'emidio551@gmail.com',
                 'login': 'emidiolegal',
                 'senha': '123'}]

professores= [{'Nome': 'Alysson',
                     'e-mail': 'alyssonoliveira@uern.br',
                     'login': 'Alysson',
                     'senha': '456'}]

alunos2 = [{'Nome': 'Emidio',
            'e-mail': 'emidio551@gmail.com'}]

professores2=[{'Nome': 'Alysson',
               'e-mail': 'alyssonoliveira@uern.br'}]


def colocar_notas(no,nt):
    for a in alunos:
        if a["Nome"] == no:
            return{"Nome": no,
                   "Nota": nt}
            
def colocar_faltas(no,ft):
    for a in alunos:
        if a["Nome"] == no:
            return{"Nome": no,
                   "Faltas": ft}



def colocar_disciplina(no,dis):
    return {'Nome': no,
            'disciplinas': dis}


def mostra_disciplina():
    nomm= input("Digite o seu nome: ")
    aux = 0
    while aux < 10:
        for a in disciplinas:
            if a['Nome'] == nomm:
                print(40*"=")
                return print(disciplinas[aux]['disciplinas'])
                break
                
            else:
                aux+=1

