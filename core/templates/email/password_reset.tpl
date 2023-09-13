{% extends "mail_templated/base.tpl" %}

{% block subject %}
Password reset
{% endblock %}

{% block html %}
Hello 
127.0.0.1:8000/accounts/api/v1/reset-password/confirm/{{token}}/
{% endblock %}