from django.db import models
from django.conf import settings
from django.template import defaultfilters

from simple_history.models import HistoricalRecords

# Create your models here.
class BaseModel(models.Model):
    created = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    modified = models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)
    historical = HistoricalRecords(user_model=settings.AUTH_USER_MODEL, inherit=True)
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for BaseModel."""
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'

class Category(BaseModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=70, unique= True, editable=False)
    description = models.TextField(max_length=150)

    def save(self, **kwargs):
        if (self.slug == '') or (self.slug == None):       
            tslug = defaultfilters.slugify(self.name)
            tempp = Category.objects.filter(slug__startswith=tslug)
            if len(tempp) > 0:
                tslug = defaultfilters.slugify(self.name)+str(len(tempp))
            self.slug = tslug
        super().save(**kwargs)

    def __str__(self):
        return f'{self.slug}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit = models.CharField(max_length=10)
    brand = models.CharField(max_length=100)
    #description = models.CharField(max_length=150)
    short_description = models.TextField(max_length=150)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Multimedia(BaseModel):
    file = models.FileField('Archivo', upload_to='upload/')
    type = models.CharField('tipo', max_length=5)
    tag = models.CharField('tag', max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.file.name}'

    class Meta:
        verbose_name = 'Multimedia'
        verbose_name_plural = 'Multimedias'

class Store(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField('catidad', default=0)
    cost = models.DecimalField('costo', max_digits=10, decimal_places=2)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return "{0}-{1}".format(self.product.code,self.code)

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Store'

class Stock(BaseModel):
    store = models.OneToOneField(Store, on_delete=models.CASCADE)
    price = models.DecimalField('precio', max_digits=10, decimal_places=2)
    code = models.CharField(max_length=10, unique=True)
    cover = models.ForeignKey(Multimedia, on_delete=models.SET_NULL, related_name='cover', blank=True, null=True)
    thumbs = models.ManyToManyField(Multimedia, blank=True)

    def __str__(self):
        return "{0}-{1}".format(self.store,self.code)

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stock'
    