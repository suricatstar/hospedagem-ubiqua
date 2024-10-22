from django.db import models

class TipoAcomodacao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome
    
class Estrela(models.Model):
    quantidade = models.IntegerField()
    
    def __str__(self):
        return str(self.quantidade) + ' estrelas'
    

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome
    
class Acomodacao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    capacidade = models.IntegerField()
    imagem = models.ImageField(upload_to='acomodacao/%Y/%m/%d', blank=True)
    local = models.CharField(max_length=100)
    servicos = models.ManyToManyField(Servico)
    tipo = models.ForeignKey(TipoAcomodacao, on_delete=models.CASCADE)
    estrelas = models.ForeignKey(Estrela, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class TipoQuarto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome
    
class AcomodacaoQuarto(models.Model):
    numero = models.IntegerField()
    quantidade_pessoas = models.IntegerField()
    descricao = models.TextField()
    diaria = models.DecimalField(max_digits=8, decimal_places=2)
    tipo = models.ForeignKey(TipoQuarto, on_delete=models.CASCADE)
    acomodacao = models.ForeignKey(Acomodacao, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.acomodacao.nome + ' - Quarto ' + str(self.numero)
    

class Reserva(models.Model):
    acomodacao = models.ForeignKey(Acomodacao, on_delete=models.CASCADE)
    quartos = models.ManyToManyField(AcomodacaoQuarto)
    data_inicio = models.DateField()
    hora_inicio = models.TimeField(default='14:00:00', blank=True)
    data_fim = models.DateField()
    hora_final = models.TimeField(default='11:00:00', blank=True)
    quantidade_pessoas = models.IntegerField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.acomodacao.nome + ' - ' + self.data_inicio.strftime('%d/%m/%Y') + ' - ' + self.data_fim.strftime('%d/%m/%Y')