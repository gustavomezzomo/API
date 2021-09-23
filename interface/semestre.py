from banco import Banco

class Semestres(object):


    def __init__(self, semestre):
        self.info = {}
        self.semestre = semestre


def insertSemestre(self):

  banco = Banco()
  try:

      c = banco.conexao.cursor()

      c.execute("insert into semestre (semestre) values ('" + self.semestre + "')" )

      banco.conexao.commit()
      c.close()

      return "semestre cadastrado com sucesso!"
  except:
      return "Ocorreu um erro na inserção do semestre"

def deleteSemestre(self):

  banco = Banco()
  try:

      c = banco.conexao.cursor()

      c.execute("delete from Semestre where senestre = " + self.semestre + " ")

      banco.conexao.commit()
      c.close()

      return "semestre excluído com sucesso!"
  except:
      return "Ocorreu um erro na exclusão do semestre"

def selectSemestre(self, semestre):
  banco = Banco()
  try:

      c = banco.conexao.cursor()

      c.execute("select * from Semestre where semestre = " + semestre + "  ")

      for linha in c:
          self.semestre = linha[0]

      c.close()

      return "Busca feita com sucesso!"
  except:
      return "Ocorreu um erro na busca do semestre"