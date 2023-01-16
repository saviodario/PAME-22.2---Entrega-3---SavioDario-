class Main:
    logDados = {"Projetos":[],"Consultores":[],"Gerentes":[]} #Base dict que vai receber uma lista de obj classes para seres resgatadas depois
    logNomes = {"Projetos":[],"Consultores":[],"Gerentes":[]} #Titulos dos projetos e users
    '''derante todo o código, os dados serão resgatados de log dados na seguinte estrutura:
    for i in Sistema.logDados[*tipo de dado*]
        if i.*comparador* == comparador
            i -> objeto resgatado para uso e alerações'''
    @classmethod
    def criarProjeto(cls):
        nome = input('informe o nome do projeto: ')
        tipo = input('informe o tipo de projeto, desenvolvimento/concepção/identidade visual ? ')
        gerente = str(input('Quem sera o gerente deste projeto? informe o user: '))
        consultor = str(input('Quem sera o consultor deste projeto? informe o user, se nao tiver consultor somente pressione enter: '))
        if consultor == '':
            consultor = None
        if tipo == 'desenvolvimento':
            etapas = 4
        if tipo == 'concepção':
            etapas = 5
        if tipo == 'identidade visual':
            etapas = 6
        Main.logDados['Projetos'].append(cls(nome,tipo,consultor,gerente,etapas))
        Main.logNomes['Projetos'].append(nome)
        return cls(nome,tipo,consultor,gerente,etapas)
    
    def removerProjeto(cls):
        for i in Main.logDados['Projetos']:
            if i.nome == cls.nome:
                Main.logDados['Projetos'].remove(i)
        Main.logNomes['Projetos'].remove(cls.nome)
        pass
    
    @classmethod
    def criarConsulor(cls, login =False):
        id = input('Crie um id: ')
        user = input('Crie um nome de usuário: ')
        senha = input('Crie uma senha: ')
        Main.logDados['Consultores'].append(cls(id, user, senha, login))
        Main.logNomes['Consultores'].append(user)
        return cls(id, user, senha, login)
    
    def removerConsultor(cls):
        for i in Main.logDados['Consultores']:
            if i.id == cls.id:
                Main.logDados['Consultores'].remove(i)
        Main.logNomes['Consultores'].remove(cls.user)
        pass
    
    @classmethod
    def criarGerente(cls, login =False):
        id = input('Crie um id: ')
        user = input('Crie um nome de usuário: ')
        senha = input('Crie uma senha: ')
        Main.logDados['Gerentes'].append(cls(id, user, senha, login))
        Main.logNomes['Gerentes'].append(user)
        return cls(id, user, senha, login)

    def removerGerente(cls):
        for i in Main.logDados["Projetos"]: #verifica se existe projeto com o gerente alvo
            if cls.user == i.gerente:
                print("Esse gerente está alocado em um projeto atualmente")
                pass
        for i in Main.logDados['Gerentes']:
            if i.id == cls.id:
                Main.logDados['Gerentes'].remove(i)
        Main.logNomes['Gerentes'].remove(cls.user)
        pass
    
    def listar():
        for chave in Main.logNomes.keys():
            print(f'{chave} atuais -> {Main.logNomes[chave]}')
        pass
    
    def sairPrograma():
        exit()
    
    
class Gerente(Main):
    def __init__(self,id:str, user:str, senha:str, login:bool = False):
        self.id = id
        self.user = user
        self.__senha = senha
        self.login = login
        pass
    
    def logar(self):
        user = str(input('nome de usuário: '))
        senha = str(input('senha: '))
        if user == self.user and senha == self.__senha:
            self.login = True
            print('Login feito')
        return False
    
    def verDados(self):
        if self.login == True:
            print(f'Seu id e {self.id}')
            print(f'Seu user e {self.user}')
        pass
    
    def modificarDados(self):
        if self.login == True:
            self.user = str(input("Qual sera o novo user?: "))
            for i in Main.logDados['Gerentes']:
                if i.id == self.id:
                    i.user = self.user
        else:
            print('precisa fazer login')
        pass
    
    def verificarProjetos(self):
        if self.login == True:
            for i in Main.logDados['Projetos']:
                if i.gerente == self.user:
                    print(f'O gerente {self.user} esta alocado no projeto {i.nome}, faltam {i.etapas} etapas')
        else:
            print('precisa fazer login')
        pass
    
    def avancarProjeto(self):
        if self.login == True:
            nome = str(input('Qual o nome do projeto que deseja avancar? '))
            for i in Main.logDados['Projetos']:
                if i.nome == nome:
                    i.avancarEtapa()
        else:
            print('precisa fazer login')
        pass
    
    def darVal(self):
        if self.login == True:
            resp = str(input('aprovacao concedida? sim ou nao?'))
            if resp == 'sim':
                return True
            if resp == 'nao':
                return False
        else:
            print('precisa de login')
        pass
    
    def passarProjeto(self):
        if self.login == True:
            projeto = str(input('Qual o nome do projeto que sera repassado? '))
            consultor = str(input('Para qual consultor? '))
            for i in Main.logDados['Projetos']:
                if i.nome == projeto:
                    i.consultor = consultor 
        else:
            print('precisa fazer login')
        pass
    
    def entregarProjeto(self):
        if self.login == True:
            for i in Main.logDados['Projetos']:
                if i.etapas == 0:
                    print(f'Todas as etapas do projeto {i.nome} foram concluidas, projeto entregue')                
        pass

class Consultor(Main):
    def __init__(self, id:str, user:str, senha:int, login:bool = False):
        self.id = id
        self.user = user
        self.__senha = senha
        self.login = login
        pass
    
    def logar(self):
        user = str(input('nome de usuário: '))
        senha = str(input('senha: '))
        if user == self.user and senha == self.__senha:
            self.login = True
            print('Login feito')
        return False
    
    def verDados(self):
        if self.login == True:
            print(f'Seu id e {self.id}')
            print(f'Seu user e {self.user}')
        pass
    
    def modificarDados(self):
        if self.login == True:
            self.user = str(input("Qual sera o novo user?: "))
            for i in Main.logDados['Consultor']:
                if i.id == self.id:
                    i.user = self.user #altera o novo user no logDados
        else:
            print('precisa fazer login')
        pass
    
    def verificarProjetos(self):
        if self.login == True:
            for i in Main.logDados['Projetos']:
                if i.consultor == self.user:
                    print(f'O consulor {self.user} esta alocado no projeto {i.nome}, faltam {i.etapas} etapas')
        else:
            print('precisa fazer login')
        pass
    
    def avancarProjeto(self):
        if self.login == True:
            nome = str(input('Qual o nome do projeto que deseja avancar? '))
            gerente = str(input('Quem e o gerente responsavel? '))
            for i in Main.logDados['Projetos']:
                if i.nome == nome:
                    for j in Main.logDados['Gerentes']:
                        if j.user == gerente:
                            val = j.darVal()
                            if val == True:
                                i.avancarEtapa()
                            if val == False:
                                print(f'Avanco de etapa negado pelo gerente {gerente}') 
        else:
            print('precisa fazer login')
        pass
    
    def pedirRetirada(self):
        if self.login == True:
            gerente = str(input('Quem e o gerente responsavel? '))
            for j in Main.logDados['Gerentes']:
                if j.user == gerente:
                    if j.darVal() == True:
                        for i in Main.logDados['Projetos']:
                            if i.consultor == self.user:
                                i.consultor = None
        else:
            print('precisa fazer login')     
        pass

class Projeto(Main):
    def __init__(self, nome:str, tipo:str, consultor:str, gerente:str, etapas:int):
        self.nome = nome
        self.tipo = tipo
        self.etapas = etapas
        self.gerente = gerente
        self.consultor = consultor
        pass 
    
    def avancarEtapa(self):
        self.etapas = self.etapas-1
        print(f'Faltam {self.etapas} etapas')
        if self.etapas == 0:
            print(f'Projeto {self.nome} está pronto pra entrega')
        
    
class Sistema(Main): 
    def menuPrincipal():
        while True:
            print('''
            
                    ----------------------------MENU PRINCIPAL----------------------------

                    Selecione uma das opções abaixo:

                    1 - Fazer login
                    2 - Criar conta gerente 
                    3 - Criar conta consultor 
                    4 - Remover conta gerente
                    5 - Remover conta consultor
                    6 - Criar projeto
                    7 - Remover Projeto
                    8 - Listar Projetos/Gerentes/Consultores
                    9 - Sair do programa\n''')

            r = input('\n\t\tO que você quer fazer? ')
            while r!='1' and r!='2' and r!='3' and r!='4' and r!='5' and r!='6' and r!='7' and r!='8' and r!='9':
                r = input('\n\t\tEssa opção é inválida, o que você quer fazer? ')

            if r == '1':
                tipo = str(input('Login gerente ou consultor? '))
                while tipo!='consultor' and tipo!='gerente':
                    tipo = input('\n\t\tEssa opção é inválida, gerente ou consultor? ')
                if tipo == 'consultor':
                    id = input('informe o id do usuário: ')
                    for i in Main.logDados['Consultores']:
                        if i.id==id:
                            i.logar()
                    Sistema.telaConsultor(id) #inicia o menu consultor para o objeto o resgatando pelo id
                    
                if tipo == 'gerente':
                    id = input('informe o id do usuário: ')
                    for i in Main.logDados['Gerentes']:
                        if i.id==id:
                            i.logar()
                    Sistema.telaGerente(id) #inicia o menu gerente para o objeto o resgatando pelo id
                    
                
            elif r == '2':
                Gerente.criarGerente()
            elif r == '3':
                Consultor.criarConsulor()
            elif r == '4':
                nome = input('Qual o user do gerente a ser removido: ')
                for i in Main.logDados['Gerentes']:
                    if i.user == nome:
                        cls =i
                cls.removerGerente()
            elif r == '5':
                nome = input('Qual o user do consultor a ser removido: ')
                for i in Main.logDados['Consultores']:
                    if i.user == nome:
                        cls =i
                cls.removerConsultor()
            elif r == '6':
                Projeto.criarProjeto()
            elif r=='7':
                nome = input('Qual o nome do projeto a ser removido: ')
                for i in Main.logDados['Projetos']:
                    if i.nome == nome:
                        cls =i
                cls.removerProjeto()
            elif r=='9':
                Main.sairPrograma()
            elif r=='8':
                Main.listar()
    def telaConsultor(id):
        for i in Main.logDados['Consultores']:
            if i.id == id:
                cls = i
        while True:
            print('''
            
                    ----------------------------CONSULTOR----------------------------

                    Selecione uma das opções abaixo:

                    1 - Ver dados
                    2 - Modificar dados
                    3 - Verificar projeto
                    4 - Avançar projeto
                    5 - Pedir retirada
                    6 - Voltar ao menu principal\n''')

            r = input('\n\t\tO que você quer fazer? ')
            while r!='1' and r!='2' and r!='3' and r!='4' and r!='5' and r!='6':
                r = input('\n\t\tEssa opção é inválida, o que você quer fazer? ')
            if r=='1':
                cls.verDados()
            if r=='2':
                cls.modificarDados()
            if r=='3':
                cls.verificarProjetos()
            if r=='4':
                cls.avancarProjeto()
            if r=='5':
                cls.pedirRetirada()
            if r=='6':
                Sistema.menuPrincipal()
    def telaGerente(id):
        for i in Main.logDados['Gerentes']:
            if i.id == id:
                cls = i
        while True:
            print('''
            
                    ----------------------------GERENTE----------------------------

                    Selecione uma das opções abaixo:

                    1 - Ver dados
                    2 - Modificar dados
                    3 - Verificar projeto
                    4 - Avançar projeto
                    5 - Dar val
                    6 - Passar projeto
                    7 - Entregar projeto
                    8 - Voltar menu principal\n''')

            r = input('\n\t\tO que você quer fazer? ')
            while r!='1' and r!='2' and r!='3' and r!='4' and r!='5' and r!='6' and r!='7' and r!='8':
                r = input('\n\t\tEssa opção é inválida, o que você quer fazer? ')
            if r=='1':
                cls.verDados()
            if r=='2':
                cls.modificarDados()
            if r=='3':
                cls.verificarProjetos()
            if r=='4':
                cls.avancarProjeto()
            if r=='5':
                cls.darVal()
            if r=='6':
                cls.passarProjeto()
            if r=='7':
                cls.entregarProjeto()
            if r=='8':
                Sistema.menuPrincipal()


Sistema.menuPrincipal()


