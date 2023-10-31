from prisma.models import Gradle, Diary

Gradle.create_partial('GradleRequest', exclude=['id'], exclude_relational_fields=True)
Gradle.create_partial('GradleResponse', exclude_relational_fields=True)

Diary.create_partial('DiaryRequest', exclude=['id'], exclude_relational_fields=True)
Diary.create_partial('DiaryResponse', exclude_relational_fields=True)