from django.db import models

# Create your models here.

class Villager(models.Model):
	GENDER = [
		('M', 'Male'),
		('F', 'Female')
	]

	PERSONALITY = [
		('LZY', 'Lazy'),
		('JOK', 'Jock'),
		('CKY', 'Cranky'),
		('SMG', 'Smug'),
		('NML', 'Normal'),
		('PPY', 'Peppy'),
		('STY', 'Snooty'),
		('SSY', 'Sisterly')
	]

	SPECIES = [
		('ALLIGATOR', 'Alligator'),
		('ANTEATER', 'Anteater'),
		('BEAR', 'Bear'),
		('BIRD', 'Bird'),
		('BULL', 'Bull'),
		('CAT', 'Cat'),
		('CHICKEN', 'Chicken'),
		('COW', 'Cow'),
		('CUB', 'Cub'),
		('DEER', 'Deer'),
		('DOG', 'Dog'),
		('DUCK', 'Duck'),
		('EAGLE', 'Eagle'),
		('ELEPHANT', 'Elephant'),
		('FROG', 'Frog'),
		('GOAT', 'Goat'),
		('GORILLA', 'Gorrilla'),
		('HAMSTER', 'Hamster'),
		('HIPPO', 'Hippo'),
		('HORSE', 'Horse'),
		('KANGAROO', 'Kangaroo'),
		('KOALA', 'Koala'),
		('LION', 'Lion'),
		('MONKEY', 'Monkey'),
		('MOUSE', 'Mouse'),
		('OCTOPUS', 'Octopus'),
		('OSTRICH', 'Ostrich'),
		('PENGUIN', 'Penguin'),
		('PIG', 'Pig'),
		('RABBIT', 'Rabbit'),
		('RHINO', 'Rhino'),
		('SHEEP', 'Sheep'),
		('SQUIRREL', 'Squirrel'),
		('TIGER', 'Tiger'),
		('WOLF', 'Wolf')
	]

	name = models.CharField(max_length = 32)
	gender = models.CharField(
		max_length = 32,
		choices = GENDER,
		default = 'M'
	)

	personality = models.CharField(
		max_length = 32,
		choices = PERSONALITY,
		default = 'Lazy'
	)

	species = models.CharField(
		max_length = 32,
		choices = SPECIES,
		default = 'ALLIGATOR'
	)

	birthday = models.DateField()
	catchphrase = models.CharField(max_length = 32)
	image = models.ImageField(blank=True, null=True)

	def __str__(self):
		return self.name

