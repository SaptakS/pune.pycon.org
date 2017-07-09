from django.db import models
from symposion.conference.models import Conference

class Ticket(models.Model):

    conference = models.ForeignKey(Conference, verbose_name=_("conference"))
    name = models.CharField(_("name"), max_length=100)
    email = models.CharField(_("email"), max_length=100)
    ticket_type = models.CharField(_("type"), max_length=100)
    quantity = models.PositiveIntegerField(_("quantity"))

    class Meta:
        verbose_name = _("ticket")
        verbose_name_plural = _("tickets")
        ordering = ['name', 'conference', 'ticket_type']

    def __unicode__(self):
        return u"%s %s %s" % (self.name, self.ticket_type, self.quantity)
