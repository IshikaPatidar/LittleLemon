from django.db import models


class Booking(models.Model):
    Name=models.CharField(max_length=255)
    No_of_guest=models.IntegerField()
    BookingDate=models.DateTimeField()
    
    
class Menu(models.Model):
    MenuId=models.IntegerField()
    Title=models.CharField(max_length=255)
    Price=models.DecimalField(max_digits=10, decimal_places=2)
    Inventory=models.IntegerField()
    
    def get_item(self):
        return f'{self.Title} : {str(self.Price)}'
    
    def __str__(self) -> str:
        return self.Title
    
    
class MenuItem(models.Model):
    title=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    inventory=models.IntegerField()
    
    def get_item(self):
        return f'{self.title} :{str(self.price)}'
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'