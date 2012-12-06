from django.db import models


class Workshop(models.Model):
    STATUS_CHOICES = (
        ('AC','Active'),
        ('IA','Inactive'),)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='IA')
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=10)
    pin = models.IntegerField()
    mobile = models.BigIntegerField()
    workshop = models.CharField(max_length=50)
    branch =  models.CharField(max_length=50)

    def __unicode__(self):
        return "%s" % self.workshop


class Unit(models.Model):
    ACTION_CHOICES = (
        ('CH','Check'),
        ('RC','Re-Check'),
        ('AD','Assign Dealer'),
        ('AC','Activate Device'),
        ('DA','De-activate'),)
    serial_id = models.BigIntegerField()
    sim_id = models.BigIntegerField()
    action = models.CharField(max_length=20,choices=ACTION_CHOICES,default='CH')
    dealer = models.CharField(max_length=100)
#    owner = models.CharField(max_length=100)
    warning = models.CharField(max_length=100)
#    status = models.CharField(max_length=10)
    workshop = models.ForeignKey(Workshop)

    def __unicode__(self):
        return "%s" % self.serial_id
    def need_check(self):
        return self.status == 'CH'


class Owner(models.Model):
    STATUS_CHOICES = (
        ('AC','Active'),
        ('IA','Inactive'),)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='IA')
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=10)
    pin = models.IntegerField()
    mobile = models.BigIntegerField()
    unit = models.ForeignKey(Unit)
 
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
    def need_process(self):
        return self.status == 'IA'


