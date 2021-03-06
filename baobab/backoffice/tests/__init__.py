# -*- coding: utf-8 -*-

"""
django only look for test in app_name.tests.py or app_name.tests/__init__.py
add the tests classes here to make them visible to django
"""

from .test_event import TestEvent
from .test_status import TestStatus
from .test_event_trigger import TestEventTrigger
from .test_eventlog_trigger import TestEventLogTrigger
