from django.db import models
import uuid

# Create your models here.
class Test(models.Model):
    obj_id = models.UUIDField(default=uuid.uuid4, db_index=True, unique=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100,unique=True)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    
    
    def get_details(self):
        data = {
            "name":self.name,
            "email":self.email,
            "phone":self.phone,
            "gender":self.gender,
            "date_of_birth":self.date_of_birth
        }
        return data