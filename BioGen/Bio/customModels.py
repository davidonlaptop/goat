from django.db.models.fields import (SmallIntegerField,
	                                     PositiveSmallIntegerField,
	                                     AutoField)
	
from django.conf import settings
	
class TinyIntegerField(SmallIntegerField):
    def db_type(self, connection):
	if connection.settings_dict['ENGINE'] == 'django.db.backends.mysql':
	    return "tinyint"
	else:
	    return super(TinyIntegerField, self).db_type(connection)
	
	
class PositiveTinyIntegerField(PositiveSmallIntegerField):
    def db_type(self, connection):
	if connection.settings_dict['ENGINE'] == 'django.db.backends.mysql':
	    return "tinyint unsigned"
	else:
	    return super(PositiveTinyIntegerField, self).db_type(connection)
	
	
class PositiveSmallAutoField(AutoField):       
    def db_type(self):
	if settings.DATABASE_ENGINE == 'mysql':
            return "smallint unsigned AUTO_INCREMENT"
	else:
	    return super(AutoField, self).db_type(connection)
    def get_internal_type(self):
	return "PositiveSmallAutoField"
	
	
class PositiveTinyAutoField(AutoField):       
    def db_type(self):
	if settings.DATABASE_ENGINE == 'mysql':
	    return "tinyint unsigned AUTO_INCREMENT"
	else:
	    return super(AutoField, self).db_type(connection)
    def get_internal_type(self):
	return "PositiveTinyAutoField"
	           
	
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^liveview\.livedata\.custommodels\.PositiveTinyIntegerField"])
add_introspection_rules([], ["^liveview\.livedata\.custommodels\.TinyIntegerField"])
add_introspection_rules([], ["^liveview\.livedata\.custommodels\.PositiveSmallAutoField"])
add_introspection_rules([], ["^liveview\.livedata\.custommodels\.PositiveTinyAutoField"])