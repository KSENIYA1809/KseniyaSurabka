from datetime import time
from .schemas import swagger_doc
from rest_framework.views import APIView

from .enums import LessonType
from .models import Group
from .models import GroupCRM
from .models import Lesson

@swagger_doc
class RefreshPoint(APIView):
    class LessonRefresh:

        def object_create(self, lesson_crm):
            if lesson_crm.final_time.time() > time(22, 0):
                final_time = lesson_crm.final_time.replace(
                    hour=22, minute=0, second=0, microsecond=0
                )
            else:
                final_time = lesson_crm.final_time
            new_lesson = Lesson(
                lesson_name=lesson_crm.lesson_name,
                class_id=lesson_crm.class_id,
                lesson_date=lesson_crm.lesson_date,
                start_time=lesson_crm.start_time,
                final_time=final_time,
                teacher_id=lesson_crm.teacher_id,
                lesson_topic=lesson_crm.lesson_topic,
                group_id=lesson_crm.group_id,
                status=lesson_crm.status,
                notes=lesson_crm.notes,
                buzy=lesson_crm.buzy,
                remote=lesson_crm.remote,
                school_year=lesson_crm.school_year,
                id_crm=lesson_crm.id,
            )
            group_crm = GroupCRM.objects.get(id=lesson_crm.group_id)
            if group_crm.status_group == "Выпущена":
                new_lesson.lesson_type = LessonType.RELEASED_GROUP.value
            if group_crm.status_group == "Набирается":
                new_lesson.lesson_type = LessonType.FORMING_GROUP.value
            return new_lesson

        def upgrade_lesson_type(self, lesson_crm, lesson_journal):
            group_journal = Group.objects.get(id_crm=lesson_crm.group_id)
            group_crm = GroupCRM.objects.get(id=lesson_crm.group_id)
            lesson_type = LessonType.SCHEDULED.value

            if group_crm.status_group == "Выпущена":
                lesson_type = LessonType.RELEASED_GROUP.value
            if group_crm.status_group == "Набирается":
                lesson_type = LessonType.FORMING_GROUP.value
            if (
                group_crm.status_group == "Обучается"
                or group_crm.status_group == ""
            ):
                lesson_type = LessonType.SCHEDULED.value

            if (
                lesson_journal.lesson_date != lesson_crm.lesson_date
                or lesson_journal.start_time != lesson_crm.start_time
                or lesson_journal.class_id != lesson_crm.class_id
                or lesson_journal.status != lesson_crm.status
                or lesson_journal.teacher_id != lesson_crm.teacher_id
                or group_journal.teacher_id != group_crm.teacher_id
            ) and group_crm.status_group == "Выпущена":
                lesson_type = LessonType.RELEASED_GROUP.value

            if (
                lesson_journal.lesson_date != lesson_crm.lesson_date
                or lesson_journal.start_time != lesson_crm.start_time
                or lesson_journal.class_id != lesson_crm.class_id
                or lesson_journal.status != lesson_crm.status
                or lesson_journal.teacher_id != lesson_crm.teacher_id
                or group_journal.teacher_id != group_crm.teacher_id
            ) and group_crm.status_group == "Набирается":
                lesson_type = LessonType.FORMING_GROUP.value
            return lesson_type

        def object_upgrade(self, lesson_crm, lesson_journal):
            lesson_journal.lesson_name = lesson_crm.lesson_name
            lesson_journal.class_id = lesson_crm.class_id
            lesson_journal.lesson_date = lesson_crm.lesson_date
            lesson_journal.start_time = lesson_crm.start_time
            lesson_journal.start_time = lesson_crm.start_time
            if lesson_crm.final_time.time() > time(22, 0):
                lesson_journal.final_time = lesson_crm.final_time.replace(
                    hour=22, minute=0, second=0, microsecond=0
                )
            else:
                lesson_journal.final_time = lesson_crm.final_time
            lesson_journal.teacher_id = lesson_crm.teacher_id
            if not lesson_journal.lesson_topic:
                lesson_journal.lesson_topic = lesson_crm.lesson_topic
            lesson_journal.group_id = lesson_crm.group_id
            lesson_journal.notes = lesson_crm.notes
            lesson_journal.buzy = lesson_crm.buzy
            lesson_journal.remote = lesson_crm.remote
            lesson_journal.school_year = lesson_crm.school_year
            return lesson_journal

        def check_equality(self, lesson_journal, lesson_crm):
            group_journal = Group.objects.get(id_crm=lesson_crm.group_id)
            inequality += lesson_journal.lesson_name != lesson_crm.lesson_name
            inequality += lesson_journal.class_id != lesson_crm.class_id
            inequality += lesson_journal.lesson_date != lesson_crm.lesson_date
            inequality += lesson_journal.start_time != lesson_crm.start_time
            inequality += lesson_journal.final_time != lesson_crm.final_time
            if (
                group_journal.status_group == "Выпущена"
                or group_journal.status_group == "Набирается"
                or group_journal.status_group == "Обучается"
                or group_journal.status_group == ""
            ):
                inequality += 1
            if group_journal.status_group in [
                "Обучается",
                "",
            ] and lesson_journal.lesson_type in [
                LessonType.MOVED.value,
                LessonType.REPLACE.value,
            ]:
                inequality -= 1
            inequality += lesson_journal.group_id != lesson_crm.group_id
            inequality += lesson_journal.notes != lesson_crm.notes
            inequality += lesson_journal.buzy != lesson_crm.buzy
            inequality += lesson_journal.remote != lesson_crm.remote
            inequality += lesson_journal.school_year != lesson_crm.school_year
            return not inequality

        def synchronize(self):
            pass