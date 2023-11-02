from django import template

register = template.Library()

@register.filter
def get_selected_answer(result, question):
    selected_answer = result.selected_answers.get(question=question)
    return selected_answer.answer