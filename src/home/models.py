from django.db import models

class Variable(models.Model):
	key		 	= models.CharField(max_length=250)
	val		 	= models.TextField(blank=True)
	is_encrypted= models.BooleanField(default=False)

	def __str__(self):
		return self.key

	class Meta:
		managed = False
		db_table = "variable"


class TaskInstance(models.Model):
	task_id			= models.CharField(max_length=250, primary_key=True)
	dag_id			= models.CharField(max_length=250, unique=True)
	execution_date	= models.DateTimeField()
	start_date		= models.DateTimeField()
	end_date		= models.DateTimeField()
	state 			= models.CharField(max_length=20)
	try_number		= models.IntegerField(blank=True)
	queue 			= models.CharField(max_length=50)

	def __str__(self):
		return self.task_id

	class Meta:
		managed = False
		unique_together = (("task_id", "dag_id","execution_date"),)
		db_table = "task_instance"


