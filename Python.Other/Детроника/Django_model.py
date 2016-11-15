
class User(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='First name')
    last_name = models.CharField(max_length=255, verbose_name='Last name')
    email = model.EmailField(max_length=75)

class Device(models.Model):
    title = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    description = models.TextField(default=’’, blank=True)
    user = model.ForeignKey(User)

