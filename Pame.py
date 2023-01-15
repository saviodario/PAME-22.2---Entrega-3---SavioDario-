class Sistema:
    
    logDados = {"Projetos":[],"Consultores":[],"Gerentes":[]} #Base dict que vai receber uma lista de obj classes para seres resgatadas depois
    logNomes = {"Projetos":[],"Consultores":[],"Gerentes":[]} #Titulos dos projetos e users
    
    @classmethod
    def criarProjeto(cls, nome, tipo, etapas=0):
        gerente = str(input('Quem será o gerente deste projeto? informe o user: '))
        consultor = str(input('Quem será o consultor deste projeto? informe o user, se nao tiver consultor somente precione enter: '))
        if consultor == '':
            consultor = None
        
        Sistema.logDados['Projetos'].append(cls(nome,tipo,consultor,gerente,etapas))
        Sistema.logNomes['Projetos'].append(nome)
        return cls(nome,tipo,consultor,gerente,etapas)
    
    def removerProjeto(cls):
        for i in Sistema.logDados['Projetos']:
            if i.nome == cls.nome:
                Sistema.logDados['Projetos'].remove(i)
        Sistema.logNomes['Projetos'].remove(cls.nome)
        pass
    
    @classmethod
    def criarConsulor(cls, id, user, senha, login =False):
        Sistema.logDados['Consultores'].append(cls(id, user, senha, login))
        Sistema.logNomes['Consultores'].append(user)
        return cls(id, user, senha, login)
    
    def removerConsultor(cls):
        for i in Sistema.logDados['Consultores']:
            if i.id == cls.id:
                Sistema.logDados['Consultores'].remove(i)
        Sistema.logNomes['Consultores'].remove(cls.user)
        pass
    
    @classmethod
    def criarGerente(cls, id, user, senha, login =False):
        Sistema.logDados['Gerentes'].append(cls(id, user, senha, login))
        Sistema.logNomes['Gerentes'].append(user)
        return cls(id, user, senha, login)

    def removerGerente(cls):
        for i in Sistema.logDados["Projetos"]: #verifica se existe projeto com o gerente
            if cls.user == i.gerente:
                print("Esse gerente está alocado em um projeto atualmente")
                pass
        for i in Sistema.logDados['Gerentes']:
            if i.id == cls.id:
                Sistema.logDados['Gerentes'].remove(i)
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
            self.user = str(input("Qual será o novo user?: "))
            for i in Sistema.logDados['Gerentes']:
                if i.id == self.id:
                    i.user = self.user
        else:
            print('precisa fazer login')
        pass
    
    def verificarProjetos(self):
        if self.login == True:
            for i in Sistema.logDados['Projetos']:
                if i.gerente == self.user:
                    print(f'O gerente {self.user} está alocado no projeto {i.nome}, faltam {i.etapas} etapas')
        else:
            print('precisa fazer login')
        pass
    
    def avancarProjeto(self):
        if self.login == True:
            nome = str(input('Qual o nome do projeto que deseja avançar? '))
            for i in Sistema.logDados['Projetos']:
                if i.nome == nome:
                    i.etapas = i.etapas - 1
                else:
                    print(f'Projeto {nome} nao consta no sistema')
        else:
            print('precisa fazer login')
        pass
    
    def darVal(self):
        if self.login == True:
            resp = str(input('aprovação concedida? sim ou nao?'))
            if resp == 'sim':
                return True
            if resp == 'nao':
                return False
        else:
            print('precisa de login')
        pass
    
    def passarProjeto(self):
        if self.login == True:
            projeto = str(input('Qual o nome do projeto que será repassado? '))
            consultor = str(input('Para qual consultor? '))
            for i in Sistema.logDados['Projetos']:
                if i.nome == projeto:
                    i.consultor = consultor 
        else:
            print('precisa fazer login')
        pass
    
    def entregarProjeto(self):
        if self.login == True:
            for i in Sistema.logDados['Projetos']:
                if i.etapas == 0:
                    print(f'Todas as etapas do projeto {i.nome} foram concluidas, projeto entregue')                
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
            self.user = str(input("Qual será o novo user?: "))
            for i in Sistema.logDados['Consultor']:
                if i.id == self.id:
                    i.user = self.user #altera o novo user no logDados
        else:
            print('precisa fazer login')
        pass
    
    def verificarProjetos(self):
        if self.login == True:
            for i in Sistema.logDados['Projetos']:
                if i.consultor == self.user:
                    print(f'O consulor {self.user} está alocado no projeto {i.nome}, faltam {i.etapas} etapas')
        else:
            print('precisa fazer login')
        pass
    
    def avancarProjeto(self):
        if self.login == True:
            nome = str(input('Qual o nome do projeto que deseja avançar? '))
            gerente = str(input('Quem é o gerente responsável? '))
            for i in Sistema.logDados['Projetos']:
                if i.nome == nome:
                    if gerente.darVal() == True:
                        i.etapas = i.etapas - 1
                    if gerente.darVal() == False:
                        print(f'Avanço de etapa negado pelo gerente {gerente}')
                else:
                    print(f'Projeto {nome} nao consta no sistema')
        else:
            print('precisa fazer login')
        pass
    
    def pedirRetirada(self):
        if self.login == True:
            gerente = str(input('Quem é o gerente responsável? '))
            if gerente.darVal() == True:
                for i in Sistema.logDados['Projetos']:
                    if i.consultor == self.user:
                        i.consultor = None
        else:
            print('precisa fazer login')     
        pass

class Projeto(Sistema):
    def __init__(self, nome:str, tipo:str, consultor, gerente, etapas:int = 0):
        self.nome = nome
        self.tipo = tipo
        self.__etapas = etapas
        self.gerente = gerente
        self.consultor = consultor
        self.etapas = self.tipo #ativação do setter de etapas por tipo de projeto
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
        
def main():
    "aqui terá uma função para manter o programa em loop + menus"
    pass

g1 = Gerente.criarGerente('sa123','savio',254560,True)
c1 = Consultor.criarConsulor('ca123','camilla',123456)
p1 = Projeto.criarProjeto('Entrega3','desenvolvimento')

