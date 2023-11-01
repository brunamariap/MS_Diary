from prisma.models import Grade, Diary

Grade.create_partial('GradeRequest', exclude=['id'], exclude_relational_fields=True)
Grade.create_partial('GradeResponse', exclude_relational_fields=True)

Diary.create_partial('DiaryRequest', exclude=['id'], exclude_relational_fields=True)
Diary.create_partial('DiaryResponse', exclude_relational_fields=True)