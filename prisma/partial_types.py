from prisma.models import Gradle

Gradle.create_partial('GradleRequest', exclude=['id'], exclude_relational_fields=True)
Gradle.create_partial('GradleResponse', exclude_relational_fields=True)