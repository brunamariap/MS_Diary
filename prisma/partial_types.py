from prisma.models import Gradle

Gradle.create_partial('CreateGradleBody', exclude=['id'], exclude_relational_fields=True)