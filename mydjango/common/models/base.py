from django.db import models


class UnsignedAutoField(models.AutoField):
    def db_type(self, connection):
        return "integer UNSIGNED AUTO_INCREMENT"

    def rel_db_type(self, connection):
        return "integer UNSIGNED"


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)
    updated_by = models.CharField(max_length=100, blank=True)

    class Meta:
        abstract = True


class IdAndTimeStampedModel(models.Model):
    """
    an abstract base class that provides "id" and event-timestamp("created", "updated")
      - "id" range: from 1 to 4294967295
      - "id" mysql integer type: int(10) unsinged 
    """

    id = UnsignedAutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class BigIdAndTimeStampedModel(models.Model):
    """
    an abstract base class that provides "id" and event-timestamp("created", "updated")
      - "id" range in django: from 1 to 9223372036854775807
      - "id" integer type in mysql: bigint(20)
    """

    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class IdAndAdminEditedModel(models.Model):
    """
    an abstract base class that provides "id", event-timestamp("created", "updated"), event-owner("created_by", "updated_by")
      - "id" range: from 1 to 4294967295
      - "id" mysql integer type: int(10) unsinged
    """

    id = UnsignedAutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)
    updated_by = models.CharField(max_length=100, blank=True)

    class Meta:
        abstract = True


class BigIdAndAdminEditedModel(models.Model):
    """
    an abstract base class that provides "id", event-timestamp("created", "updated"), event-owner("created_by", "updated_by")
      - "id" range in django: from 1 to 9223372036854775807
      - "id" integer type in mysql: bigint(20)
    """

    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)
    updated_by = models.CharField(max_length=100, blank=True)

    class Meta:
        abstract = True


class CommonModelMeta:
    """
    default_permissions = ()
        기본 permission 들인 ('add', 'change', 'delete', 'view') 생성을 방지한다.
        https://docs.djangoproject.com/en/2.1/ref/models/options/#default-permissions
    """

    default_permissions = ()
