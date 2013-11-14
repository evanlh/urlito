from django.db import models
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
base = len(alphabet)

# Create your models here.
class Url(models.Model):
    url = models.CharField(max_length=2000)
    short_url = models.CharField(max_length=8)
    create_date = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        result = super(Url, self).save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
        if self.id:
            self.short_url = Url.encode(self.id)
            super(Url, self).save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
            print self.short_url


    @staticmethod
    def encode(num):
        hash = ''
        while num != 0:
            hash = (alphabet[num % base]) + hash
            num = int(num / base)

        return hash

    @staticmethod
    def decode(hash):
        i, mul = 0, 1
        for letter in reversed(hash):
            i += mul * alphabet.index(letter)
            mul *= base
        return i
