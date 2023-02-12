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


class QuestionMedia(models.Model):
    question = models.ForeignKey(
        Question,
        related_name='question_media',
        on_delete=models.DO_NOTHING,
    )
    media = models.FileField(
        upload_to='question_media/',
        null=False,
        blank=False,
        verbose_name=_("Question Media")
    )

    def __str__(self):
        return self.media.name

    class Meta:
        verbose_name = _("Question Media")
        verbose_name_plural = _("Question Media")
        ordering = ['id']
