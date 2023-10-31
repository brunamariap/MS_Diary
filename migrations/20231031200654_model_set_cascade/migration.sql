-- RedefineTables
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_Gradle" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "score" INTEGER NOT NULL,
    "bimester" INTEGER NOT NULL,
    "schoolReportId" TEXT NOT NULL,
    "disciplineId" TEXT NOT NULL,
    "attributedBy" TEXT NOT NULL,
    CONSTRAINT "Gradle_schoolReportId_fkey" FOREIGN KEY ("schoolReportId") REFERENCES "SchoolReport" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO "new_Gradle" ("attributedBy", "bimester", "disciplineId", "id", "schoolReportId", "score") SELECT "attributedBy", "bimester", "disciplineId", "id", "schoolReportId", "score" FROM "Gradle";
DROP TABLE "Gradle";
ALTER TABLE "new_Gradle" RENAME TO "Gradle";
CREATE TABLE "new_SchoolReport" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "diaryId" TEXT NOT NULL,
    "studentId" TEXT NOT NULL,
    CONSTRAINT "SchoolReport_diaryId_fkey" FOREIGN KEY ("diaryId") REFERENCES "Diary" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO "new_SchoolReport" ("diaryId", "id", "studentId") SELECT "diaryId", "id", "studentId" FROM "SchoolReport";
DROP TABLE "SchoolReport";
ALTER TABLE "new_SchoolReport" RENAME TO "SchoolReport";
PRAGMA foreign_key_check;
PRAGMA foreign_keys=ON;
