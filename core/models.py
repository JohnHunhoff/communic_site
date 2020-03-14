from django.db import models
from stdimage.models import StdImageField
import uuid


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


# team section init
class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=50)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):

    ICONES_CHOICES = (
        ('fa fa-facebook', 'Facebook'),
        ('fa fa-twitter', 'Twitter'),
        ('fa fa-linkedin', 'Linkedin'),
        ('fa fa-instagram', 'Instagram')
    )

    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    imagem = StdImageField(
        'Imagem',
        upload_to=get_file_path,
        variations={'thumb': {'width': 480, 'height': 480, 'crop': True}}
    )
    facebook_icon = models.CharField('Facebook', max_length=50, choices=ICONES_CHOICES, default='')
    twitter_icone = models.CharField('Twitter', max_length=50, choices=ICONES_CHOICES, default='')
    linkedin_icone = models.CharField('Linkedin', max_length=50, choices=ICONES_CHOICES, default='')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


# team section end
# Features section init 'features.html'
class Features(Base):
    FEATURES_CHOICES = (
        ('lnr lnr-rocket', 'Foguete'),
        ('lnr lnr-laptop-phone', 'Laptop'),
        ('lnr lnr-layers', 'Layer'),
        ('lnr lnr-cog', 'Cog'),
        ('lnr lnr-magnifier', 'Lupa'),
        ('lnr lnr-pencil', 'lápis')
    )

    title = models.CharField('Titulo', max_length=100)
    icone = models.CharField('Icone', max_length=100, choices=FEATURES_CHOICES, default='')
    texto = models.TextField('Texto', max_length=500, default='')

    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return self.title


# Features section end
# blog features init
class Publicacoes(Base):
    title = models.CharField('Titulo', max_length=100)
    sub_title = models.CharField('Subtitulo', max_length=500)
    imagem_publicacao = StdImageField(
        name='Imagem',
        upload_to=get_file_path,
        variations={'thumb': {'width': 480, 'height': 480, 'crop': True}}
    )
    text = models.TextField('Texto', max_length=4000)

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    def __str__(self):
        return self.title


# blog features end
# services init
class Services(Base):
    SERVICES_CHOICES = (
        ('lnr lnr-pencil', 'Lápis'),
        ('lnr lnr-code', 'html'),
        ('lnr lnr-mustache', 'Emote: Bigode'),
        ('lnr lnr-chart-bars', 'Gráfico'),
        ('lnr lnr-tablet', 'Tablete'),
        ('lnr lnr-earth', 'Planeta Terra'),
        ('lnr lnr-hourglass', 'Ampulheta(Relógio de areia)'),
        ('lnr lnr-rocket', 'Foguete'),
        ('lnr lnr-screen', 'Monitor')
    )

    title = models.CharField('Titulo', max_length=100)
    icon = models.CharField('Icone', max_length=50, choices=SERVICES_CHOICES)
    description = models.CharField('Descrição', max_length=50)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.title
