from django.db import models
from stdimage.models import StdImageField
from ckeditor_uploader.fields import RichTextUploadingField


def get_file_path(_instance, filename):
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
        ('fa fa-instagram', 'Instagram'),
        ('fa fa-whatsapp', 'Whatsapp'),
    )

    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    imagem = StdImageField(
        'Imagem',
        upload_to=get_file_path,
    )
    social_icon_1 = models.CharField('Icone 1', max_length=50, choices=ICONES_CHOICES, default='')
    social_link_1 = models.CharField('Link 1', max_length=200, default='')
    social_icon_2 = models.CharField('Icone 2', max_length=50, choices=ICONES_CHOICES, default='')
    social_link_2 = models.CharField('Link 2', max_length=200, default='')
    social_icon_3 = models.CharField('Icone 3', max_length=50, choices=ICONES_CHOICES, default='')
    social_link_3 = models.CharField('Link 3', max_length=200, default='')

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
        ('lnr lnr-pencil', 'lápis'),
        ('lnr lnr-code', 'html'),
        ('lnr lnr-chart-bars', 'Gráfico'),
        ('lnr lnr-tablet', 'Tablet'),
        ('lnr lnr-earth', 'Planeta Terra'),
        ('lnr lnr-hourglass', 'Ampulheta(Relógio de areia)'),
        ('lnr lnr-screen', 'Monitor'),
        ('lnr lnr-envelope', 'E-mail'),
        ('lnr lnr-film-play', 'Video'),
        ('lnr lnr-picture', 'Imagem'),
        ('lnr lnr-store', 'Loja'),
        ('lnr lnr-pie-chart', 'Gráfico circular'),
        ('lnr lnr-smartphone', 'Celular'),
        ('lnr lnr-cart', 'Carrinho de Supermercado'),
        ('lnr lnr-camera-video', 'Camera de video'),
        ('lnr lnr-bullhorn', 'Megafone'),
        ('lnr lnr-thumbs-up', 'Positivo(joia)'),
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
    sub_title = models.CharField('Resumo', max_length=500)
    imagem = StdImageField(
        name='Imagem',
        upload_to=get_file_path,
    )
    text = RichTextUploadingField()

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
        ('lnr lnr-tablet', 'Tablet'),
        ('lnr lnr-earth', 'Planeta Terra'),
        ('lnr lnr-hourglass', 'Ampulheta(Relógio de areia)'),
        ('lnr lnr-rocket', 'Foguete'),
        ('lnr lnr-screen', 'Monitor'),
        ('lnr lnr-laptop-phone', 'Laptop'),
    )

    title = models.CharField('Titulo', max_length=100)
    icon = models.CharField('Icone', max_length=50, choices=SERVICES_CHOICES)
    description = models.CharField('Descrição', max_length=50)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.title


class Clientes(Base):
    nome = models.CharField('Cliente', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome


class Counter(Base):

    ICON_CHOICES = (
        ('lnr lnr-briefcase', 'Maleta'),
        ('lnr lnr-coffee-cup', 'Café'),
        ('lnr lnr-users', 'Usuarios'),
        ('lnr lnr-clock', 'Relógio'),
        ('lnr lnr-heart', 'Coração'),
        ('lnr lnr-chart-bars', 'Gráfico'),
        ('lnr lnr-tablet', 'Tablet'),
        ('lnr lnr-earth', 'Planeta Terra'),
        ('lnr lnr-hourglass', 'Ampulheta(Relógio de areia)'),
        ('lnr lnr-rocket', 'Foguete'),
        ('lnr lnr-screen', 'Monitor')
    )

    icon = models.CharField('Icone', max_length=50, choices=ICON_CHOICES)
    text = models.CharField('Título', max_length=80)
    number = models.IntegerField('Número', default=0)

    class Meta:
        verbose_name = 'Contador'
        verbose_name_plural = 'Contadores'

    def __str__(self):
        return self.text
