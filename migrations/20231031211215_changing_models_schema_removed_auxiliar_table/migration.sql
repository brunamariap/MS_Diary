/*
  Warnings:

  - You are about to drop the `SchoolReport` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the column `schoolReportId` on the `Gradle` table. All the data in the column will be lost.
  - Added the required column `diaryId` to the `Gradle` table without a default value. This is not possible if the table is not empty.
  - Added the required column `studentId` to the `Gradle` table without a default value. This is not possible if the table is not empty.

*/
-- DropTable
PRAGMA foreign_keys=off;
DROP TABLE "SchoolReport";
PRAGMA foreign_keys=on;

-- RedefineTables
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_Gradle" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "score" INTEGER NOT NULL,
    "bimester" INTEGER NOT NULL,
    "disciplineId" TEXT NOT NULL,
    "attributedBy" TEXT NOT NULL,
    "studentId" TEXT NOT NULL,
    "diaryId" TEXT NOT NULL,
    CONSTRAINT "Gradle_diaryId_fkey" FOREIGN KEY ("diaryId") REFERENCES "Diary" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO "new_Gradle" ("attributedBy", "bimester", "disciplineId", "id", "score") SELECT "attributedBy", "bimester", "disciplineId", "id", "score" FROM "Gradle";
DROP TABLE "Gradle";
ALTER TABLE "new_Gradle" RENAME TO "Gradle";
PRAGMA foreign_key_check;
PRAGMA foreign_keys=ON;
