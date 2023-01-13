class Sistema:
    
    logDados = {"Projetos":[],"Consultores":[],"Gerentes":[]} #Base dict que vai receber uma lista de obj classes para seres resgatadas depois
    logNomes = {"Projetos":[],"Consultores":[],"Gerentes":[]} #Titulos dos projetos e users
    
    @classmethod
    def criarProjeto(cls, nome, tipo, consultor = None, etapas=0):
        Sistema.logDados['Projetos'].append(cls(nome,tipo,consultor,etapas))
        Sistema.logNomes['Projetos'].append(nome)
        return cls(nome,tipo,consultor,etapas)
    
    def removerProjeto(cls):
        Sistema.logDados['Projetos'].remove(cls)
        Sistema.logNomes['Projetos'].remove(cls.nome)
        pass
    
    @classmethod
    def criarConsulor(cls, id, user, senha, login =False):
        Sistema.logDados['Consultores'].append(cls(id, user, senha, login))
        Sistema.logNomes['Consultores'].append(user)
        return cls(id, user, senha, login)
    
    def removerConsultor(cls):
        Sistema.logDados['Consultores'].remove(cls)
        Sistema.logNomes['Consultores'].remove(cls.user)
        pass
    
    @classmethod
    def criarGerente(cls, id, user, senha, login =False):
        Sistema.logDados['Gerentes'].append(cls(id, user, senha, login))
        Sistema.logNomes['Gerentes'].append(user)
        return cls(id, user, senha, login)

    def removerGerente(cls):
        Sistema.logDados['Gerentes'].remove(cls)
        Sistema.logNomes['Gerentes'].remove(cls.user)
        pass
    
    def listar():
        for chave in Sistema.logNomes.keys():
            print(f'{chave} atuais -> {Sistema.logNomes[chave]}')
        pass
    
    def sairPrograma():
        exit()
    
    
class Gerente(Sistema):
    def __init__(self,id:str, user:str, senha:int, login:bool = False):
        self.id = id
        self.user = user
        self.__senha = senha
        self.login = login
        pass
    
    def logar(self):
        user = str(input('nome de usuário: '))
        senha = int(input('senha: '))
        if user in Sistema.logNomes['Gerentes'] and senha == self.__senha:
            self.login = True
            print('Login feito')
        else:
            print('Usuário ou senha incorretos')
    
    def verDados(self):
        if self.login == True:
            print(f'Seu id é {self.id}')
            print(f'Seu user é {self.user}')
        pass
    
    def modificarDados(self):
        if self.login == True:
            i = str(input('Deseja mudar o user ou o id?: '))
            if i == 'user':
                self.user = str(input("Qual será o novo user?: "))
            if i == 'id':
                self.id = str(input("Qual será o novo id?: "))
        pass
    
    def verificarProjetos():
        #if self.login == True:
        pass
    
    def avancarProjeto():
        #if self.login == True:
        pass
    
    def darVal():
        #if self.login == True:
        pass
    
    def passarProjeto():
        #if self.login == True:
        pass
    
    def entregarProjeto():
        #if self.login == True:
        pass

class Consultor(Sistema):
    def __init__(self, id:str, user:str, senha:int, login:bool = False):
        self.id = id
        self.user = user
        self.__senha = senha
        self.login = login
        pass
    
    def logar(self):
        user = str(input('nome de usuário: '))
        senha = int(input('senha: '))
        if user in Sistema.logNomes['Consultores'] and senha == self.__senha:
            self.login = True
            print('Login feito')
        else:
            print('Usuário ou senha incorretos')
        pass
    
    def verDados(self):
        if self.login == True:
            print(f'Seu id é {self.id}')
            print(f'Seu user é {self.user}')
        pass
    
    def modificarDados(self):
        if self.login == True:
            i = str(input('Deseja mudar o user ou o id?: '))
            if i == 'user':
                self.user = str(input("Qual será o novo user?: "))
            if i == 'id':
                self.id = str(input("Qual será o novo id?: "))
        pass
    
    def verificarProjetos():
        #if self.login == True:
        pass
    
    def avancarProjeto():
        #if self.login == True:
        pass
    
    def pedirRetirada():
        #if self.login == True:
        pass

class Projeto(Sistema):
    def __init__(self, nome:str, tipo:str, consultor = None, gerente = str(input('Quem será o gerente deste projeto? informe o user: ')), etapas:int = 0):
        #garantia que sempre terá gerente quando definido projeto no init
        self.nome = nome
        self.tipo = tipo
        self.__etapas = etapas
        self.gerente = gerente
        self.__consultor = consultor
        self.etapas = self.tipo #ativação do setter de etapas por tipo de projeto
        self.consultor = str(input('Quem será o consultor deste projeto? informe o user, se nao tiver consultor somente precione enter: '))
        #ativação do setter de consultor
        pass 
    
    @property
    def etapas(self):
        return self.__etapas
    
    @etapas.setter
    def etapas(self,tipo):
        n = 0
        if tipo == 'desenvolvimento':
            n = 4
        if tipo == 'concepcao':
            n = 5
        if tipo == 'identidade visual':
            n = 6
        self.__etapas = n

    @property
    def consultor(self):    
        return self.__consultor
    
    @consultor.setter
    def consultor(self, i):
        self.__consultor = i
        if i == '':
            self.__consultor = None
        
def main():
    "aqui terá uma função para manter o programa em loop + menus"
    pass
