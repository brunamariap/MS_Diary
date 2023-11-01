/*
  Warnings:

  - You are about to drop the `Gradle` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropTable
PRAGMA foreign_keys=off;
DROP TABLE "Gradle";
PRAGMA foreign_keys=on;

-- CreateTable
CREATE TABLE "Grade" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "score" INTEGER NOT NULL,
    "bimester" INTEGER NOT NULL,
    "disciplineId" TEXT NOT NULL,
    "attributedBy" TEXT NOT NULL,
    "studentId" TEXT NOT NULL,
    "diaryId" TEXT NOT NULL,
    CONSTRAINT "Grade_diaryId_fkey" FOREIGN KEY ("diaryId") REFERENCES "Diary" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);
