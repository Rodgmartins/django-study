import pytest
from django.utils import timezone
from polls.models import Question


@pytest.mark.django_db
def test_question_was_published_recently():
    #GIVEN:
    question_text = "Teste_string?"
    pub_date = timezone.now() - timezone.timedelta(days=1)
    active = True
    #THEN:
    question = Question.objects.create(question_text=question_text, pub_date=pub_date, active=active)
    #WHEN:
    assert question.was_published_recently() is True