from django.db import models

from mydjango.common.models.base import CommonModelMeta, TimeStampedModel


class CodeGroup(TimeStampedModel):
    code_group = models.CharField(max_length=100, primary_key=True)  # 코드 그룹
    name = models.CharField(max_length=1000)  # 코드명

    class Meta(CommonModelMeta):
        db_table = "code_group"


class Code(TimeStampedModel):
    code_group = models.ForeignKey(CodeGroup, on_delete=models.CASCADE)  # 코드그룹
    code = models.CharField(max_length=1000)  # 코드명
    name = models.CharField(max_length=1000)  # 상세
    available = models.BooleanField(default=False)  # 이용가능
    display_order = models.PositiveIntegerField()  # 출력순서
    authority = models.PositiveIntegerField(default=999)  # 권한

    class Meta(CommonModelMeta):
        db_table = "code"
        unique_together = (("code_group", "code",),)
