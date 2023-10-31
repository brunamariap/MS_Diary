-- CreateTable
CREATE TABLE "Gradle" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "score" INTEGER NOT NULL,
    "bimester" INTEGER NOT NULL,
    "schoolReportId" TEXT NOT NULL,
    "disciplineId" TEXT NOT NULL,
    "attributedBy" TEXT NOT NULL,
    CONSTRAINT "Gradle_schoolReportId_fkey" FOREIGN KEY ("schoolReportId") REFERENCES "SchoolReport" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "Diary" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "referencePeriod" INTEGER NOT NULL,
    "referenceYear" INTEGER NOT NULL,
    "startDate" DATETIME NOT NULL,
    "endDate" DATETIME NOT NULL
);

-- CreateTable
CREATE TABLE "SchoolReport" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "diaryId" TEXT NOT NULL,
    "studentId" TEXT NOT NULL,
    CONSTRAINT "SchoolReport_diaryId_fkey" FOREIGN KEY ("diaryId") REFERENCES "Diary" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);
