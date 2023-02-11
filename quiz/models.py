from django.db import models
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert'))
    )

    TYPE = (
        (0, _('Multiple Choice')),
        (1, _('True or False')),
    )

    title = models.CharField(
        max_length=255, 
        verbose_name=_("Title")
    )
    description = models.TextField(
        verbose_name=_("Description")
    )
    difficulty = models.IntegerField(
        choices=SCALE,
        default=0, 
        verbose_name=_("Difficulty")
    )
    date_created = models.DateTimeField(
        auto_now_add=True, 
        verbose_name=_("Date Created")
    )
    is_active = models.BooleanField(
        default=False, 
        verbose_name=_("Active Status")
    )
    question_type = models.IntegerField(
        choices=TYPE,
        default=0,
        verbose_name=_("Question Type")
    )
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        related_name='answer',
        on_delete=models.DO_NOTHING,
    )
    answer_text = models.CharField(
        max_length=255,
        verbose_name=_("Answer Text")
    )
    is_right = models.BooleanField(
        default=False,
        verbose_name=_("Is Right")
    )
    
    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    def __str__(self):
        return self.answer_text