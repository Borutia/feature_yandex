from django.test import TestCase

from . import data_report_test
from .data_email_test import GOOD_EMAIL
from reports.utils import get_email_link


class ReportPostTestCase(TestCase):
    """Тестирование POST запроса"""
    def setUp(self):
        """Инициализация данных"""
        self.client.post(
            '/email',
            data=GOOD_EMAIL,
            content_type='application/json',
        )

    def test_missing_data(self):
        """Обращение к обработчику с пустым телом, проверка статуса 400"""
        response = self.client.post(
            '/report',
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 400)

    def test_wrong_user_id(self):
        """Запрос с несуществующим user_id, проверка статуса 404"""
        response = self.client.post(
            '/report',
            data=data_report_test.BAD_REPORT,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 404)

    def test_not_confirmed_email(self):
        """Запрос с неподтвержденным email, проверка статуса 400"""
        response = self.client.post(
            '/report',
            data=data_report_test.GOOD_REPORT,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 400)

    def test_report_good(self):
        """Загрузка данных, проверка статуса 201"""
        self.client.get(
            get_email_link(
                email=GOOD_EMAIL['email'],
                user_id=GOOD_EMAIL['user_id'],
            )
        )
        response = self.client.post(
            '/report',
            data=data_report_test.GOOD_REPORT,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 201)


class ReportPeriodTestCase(TestCase):
    """Тестирование POST запроса"""
    def setUp(self):
        """Инициализация данных"""
        self.client.post(
            '/email',
            data=GOOD_EMAIL,
            content_type='application/json',
        )

    def test_missing_data(self):
        """Обращение к обработчику с пустым телом, проверка статуса 400"""
        response = self.client.post(
            '/report/period',
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 400)

    def test_wrong_user_id(self):
        """Запрос с несуществующим user_id, проверка статуса 404"""
        response = self.client.post(
            '/report/period',
            data=data_report_test.BAD_REPORT_PERIOD,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 404)

    def test_not_confirmed_email(self):
        """Запрос с неподтвержденным email, проверка статуса 400"""
        response = self.client.post(
            '/report/period',
            data=data_report_test.GOOD_REPORT_PERIOD,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 400)

    def test_report_period_good(self):
        """Загрузка данных, проверка статуса 201"""
        self.client.get(
            get_email_link(
                email=GOOD_EMAIL['email'],
                user_id=GOOD_EMAIL['user_id'],
            )
        )
        response = self.client.post(
            '/report/period',
            data=data_report_test.GOOD_REPORT_PERIOD,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 201)

    def test_missing_date(self):
        """Запрос с невалидной датой, проверка статуса 400"""
        self.client.get(
            get_email_link(
                email=GOOD_EMAIL['email'],
                user_id=GOOD_EMAIL['user_id'],
            )
        )
        response = self.client.post(
            '/report/period',
            data=data_report_test.BAD_REPORT_PERIOD_DATE,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 400)
